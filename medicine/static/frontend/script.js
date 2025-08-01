const API_URL = "/api/medicines/";
let medicines = [], currentSort = { key: null, asc: true };

window.onload = () => {
  fetchMedicines();

  document.getElementById("medicine-form")
    .addEventListener("submit", async e => {
      e.preventDefault();
      const payload = {
        name: document.getElementById("name").value,
        article_number: document.getElementById("article_number").value,
        description: document.getElementById("description").value,
        type: document.getElementById("type").value,
        quantity: parseInt(document.getElementById("quantity").value, 10),
        unit_price: parseFloat(document.getElementById("unit_price").value)
      };

      const res = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      if (res.ok) {
        showStatus("✅ Medicine created successfully!");
        e.target.reset();
        e.target.style.display = "none";
        fetchMedicines();
      } else {
        showStatus("❌ Failed to create medicine", false);
      }
    });
};

function showStatus(msg, ok = true) {
  const box = document.getElementById("status-message");
  box.textContent = msg;
  box.style.color = ok ? "green" : "red";
  setTimeout(() => box.textContent = "", 3000);
}

function toggleForm() {
  const f = document.getElementById("medicine-form");
  f.style.display = (f.style.display === "none") ? "block" : "none";
}

async function fetchMedicines() {
  const res = await fetch(API_URL);
  medicines = await res.json();
  renderTable(medicines);
}

function renderTable(data) {
  const tbody = document.getElementById("table-body");
  tbody.innerHTML = "";
  data.forEach(m => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${m.id}</td>
      <td contenteditable="false">${m.name}</td>
      <td contenteditable="false">${m.article_number}</td>
      <td contenteditable="false">${m.description}</td>
      <td contenteditable="false">${m.type}</td>
      <td contenteditable="false">${m.quantity}</td>
      <td contenteditable="false">${m.unit_price}</td>
      <td>
        <button onclick="modifyRow(this, ${m.id})">✏️ Modify</button>
        <button onclick="deleteMedicine(${m.id})">❌ Delete</button>
      </td>
    `;
    tbody.appendChild(row);
  });
}

function modifyRow(btn, id) {
  const row = btn.closest("tr");
  const cells = row.querySelectorAll("td[contenteditable]");

  if (btn.textContent.includes("Modify")) {
    cells.forEach(c => c.contentEditable = "true");
    btn.textContent = "💾 Save";
  } else {
    const [name, article_number, description, type, quantity, unit_price] =
      [...cells].map(c => c.textContent.trim());

    const payload = {
      name,
      article_number,
      description,
      type,
      quantity: parseInt(quantity, 10),
      unit_price: parseFloat(unit_price)
    };

    fetch(`${API_URL}${id}/`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    }).then(res => {
      if (res.ok) {
        showStatus("✅ Medicine updated!");
        cells.forEach(c => c.contentEditable = "false");
        btn.textContent = "✏️ Modify";
        fetchMedicines();
      } else {
        showStatus("❌ Update failed", false);
      }
    });
  }
}

function deleteMedicine(id) {
  if (!confirm("Are you sure you want to delete this medicine?")) return;

  fetch(`${API_URL}${id}/`, { method: "DELETE" })
    .then(res => {
      if (res.ok) {
        showStatus("🗑️ Deleted successfully!");
        fetchMedicines();
      } else {
        showStatus("❌ Delete failed", false);
      }
    });
}

function sortTable(key) {
  if (currentSort.key === key) currentSort.asc = !currentSort.asc;
  else currentSort = { key, asc: true };

  const sorted = [...medicines].sort((a, b) => {
    const vA = a[key] ?? "", vB = b[key] ?? "";
    return typeof vA === "number"
      ? (currentSort.asc ? vA - vB : vB - vA)
      : (currentSort.asc ? String(vA).localeCompare(String(vB)) : String(vB).localeCompare(String(vA)));
  });

  renderTable(sorted);
}

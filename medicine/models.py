from django.db import models

class Medicine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    article_number = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    # total_price = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False  # Tells Django not to try creating or migrating this table
        db_table = 'medicines'

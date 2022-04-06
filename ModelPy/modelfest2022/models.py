from django.db import models

# Create your models here.

class Category(models.Model):
	category_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=60)

class SubCategory(models.Model):
	subcategory_id = models.IntegerField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	name = models.CharField(max_length=60)

	class Meta:
		unique_together = (('category', 'subcategory_id'),)


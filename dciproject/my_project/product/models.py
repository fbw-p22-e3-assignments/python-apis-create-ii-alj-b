from django.db import models
from sanitizer.models import SanitizedCharField, SanitizedTextField

# Create your models here.
class Product(models.Model): #new
    name = models.SanitizedCharField("Name", max_length=240, allowed_tags=['a', 'p', 'input'])
    description = models.SanitizedTextField(default="Some description", allowed_tags=['a', 'p', 'input'])
    id = models.UUIDField(primary_key=True)
    created = models.DateField(auto_now_add=True)
    image = models.URLField(default="https://jsonplaceholder.typicode.com/")
    category = models.SanitizedCharField(default="Some Category", max_length=240, allowed_tags=['a', 'p', 'input'])

    def __str__(self):
        return self.name
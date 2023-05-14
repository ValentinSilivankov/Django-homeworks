from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    price = models.IntegerField()
    image = models.ImageField()
    release_date = models.DateField(auto_now_add=False)
    lte_exists = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def save(self,  *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Phone, self).save(*args, **kwargs)
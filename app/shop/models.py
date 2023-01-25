from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("shop:category", kwargs={"slug_cat": self.slug})
    

class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=120, db_index=True, verbose_name='Название')
    slug = models.CharField(max_length=120, db_index=True, unique=True,verbose_name='Ссылка')
    image = models.ImageField(upload_to="product/%Y/%m/%d", blank=True)
    description = models.TextField(max_length=1500, blank=True,verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Цена')
    available = models.BooleanField(default=True,verbose_name='Наличие')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Добавление')
    uploaded = models.DateTimeField(auto_now=True,verbose_name='Изменение')
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)
        
    def __str__(self) -> str:
        return self.name
        
    def get_absolute_url(self):
        return reverse("shop:product", kwargs={"slug_product": self.slug})
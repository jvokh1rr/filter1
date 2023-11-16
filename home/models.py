from django.db import models


class Product(models.Model):
    STATUS = (
        ('New', 'Yangi'),
        ('Old', 'Eski'),
        ('Broken', 'Buzilgan'),
        ('Used', 'Ishlatilgan'),
    )
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS, default='New')
    def __str__(self):
        return self.title
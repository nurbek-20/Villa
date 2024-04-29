from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=125)

    def __str__(self):
        return self.title


class Material(models.Model):
    title = models.CharField(max_length=125)

    def __str__(self):
        return self.title


class PaymentMethod(models.Model):
    title = models.CharField(max_length=125)

    def __str__(self):
        return self.title


class Villa(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/villa_images/')
    area = models.PositiveSmallIntegerField(help_text='Метр в квадрате')
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    security = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Охраняемая территория'),
            (2, 'Не охраняемая территория')
        )
    )
    description = models.TextField()
    floor_number = models.PositiveSmallIntegerField()
    bedroom = models.PositiveSmallIntegerField()
    bathroom = models.PositiveSmallIntegerField()
    parking_space_capacity = models.PositiveSmallIntegerField()
    price = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        default=0.00,
    )
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    address = models.CharField(max_length=225)
    zip_code = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.address}, {self.region} {self.zip_code}"


class Storage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    villa = models.ForeignKey(Villa, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.PositiveSmallIntegerField(
        choices=(
            (1, 'В обработке'),
            (2, 'Отклонен'),
            (3, 'Принят')
        ),
        default=1
    )













# Generated by Django 5.0.3 on 2024-04-28 13:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_villa_created_date_alter_villa_update_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'В обработке'), (2, 'Отклонен'), (3, 'Принят')], default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('villa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.villa')),
            ],
        ),
    ]

# Generated by Django 4.2 on 2023-04-26 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portbackend', '0002_alter_testimonial_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(upload_to='backend/portbackend/assets/testimonials'),
        ),
    ]

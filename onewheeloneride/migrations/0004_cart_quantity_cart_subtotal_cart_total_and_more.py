# Generated by Django 4.0 on 2023-07-22 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onewheeloneride', '0003_category_name_model_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='cart',
            name='subtotal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.TextField(default='No Comment Given'),
        ),
        migrations.AddField(
            model_name='group',
            name='description',
            field=models.TextField(default='No Description Given'),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='No Description Given'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='qantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='productreview',
            name='rating',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='productreview',
            name='review',
            field=models.TextField(default='No Review Given'),
        ),
        migrations.AddField(
            model_name='trail',
            name='difficulty',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='trailreview',
            name='rating',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='trailreview',
            name='review',
            field=models.TextField(default='No Review Given'),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-11 22:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=45)),
                ('title', models.CharField(max_length=45)),
                ('price', models.CharField(max_length=45)),
                ('amount', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=45)),
                ('page_amount', models.CharField(max_length=45)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=45)),
                ('books_amount', models.CharField(max_length=45)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('surname', models.CharField(max_length=45)),
                ('birthdate', models.DateField()),
                ('address', models.CharField(max_length=45)),
                ('phone_number', models.CharField(max_length=9)),
                ('bank_account', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
            ],
            options={
                'ordering': ('surname',),
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=45)),
                ('type', models.CharField(max_length=45)),
                ('time', models.CharField(max_length=45)),
                ('priority', models.CharField(choices=[('T', 'True'), ('F', 'False')], default='F', max_length=2)),
            ],
            options={
                'ordering': ('priority',),
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scale_points', models.CharField(max_length=45)),
                ('read_date', models.DateField()),
                ('advantages', models.CharField(max_length=45)),
                ('disadvantages', models.CharField(max_length=45)),
                ('recommend', models.BooleanField()),
                ('read_again', models.BooleanField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='products.book')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='products.client')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=45)),
                ('price', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=45)),
                ('phone', models.CharField(max_length=45)),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=45)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='products.client')),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='products.delivery')),
            ],
            options={
                'ordering': ('client',),
            },
        ),
        migrations.CreateModel(
            name='BookHasOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookhasorders', to='products.book')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookhasorders', to='products.order')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='products.category'),
        ),
        migrations.AddField(
            model_name='book',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL),
        ),
    ]

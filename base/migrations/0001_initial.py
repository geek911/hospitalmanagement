# Generated by Django 3.1.2 on 2022-05-05 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('baseentity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.baseentity')),
                ('name', models.CharField(max_length=90, unique=True)),
                ('category_image', models.ImageField(blank=True, null=True, upload_to='category/%Y/%m/%d')),
                ('is_active', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_category', to='base.category')),
            ],
            bases=('base.baseentity',),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('baseentity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.baseentity')),
                ('full_name', models.CharField(blank=True, max_length=60, null=True)),
                ('phn_number', models.CharField(blank=True, max_length=14, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
            ],
            bases=('base.baseentity',),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('baseentity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.baseentity')),
                ('name', models.CharField(max_length=70)),
            ],
            bases=('base.baseentity',),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('baseentity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.baseentity')),
                ('title', models.CharField(max_length=180)),
                ('description', models.TextField()),
                ('price', models.IntegerField(default=0)),
                ('product_image', models.ImageField(upload_to='product')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='base.category')),
            ],
            bases=('base.baseentity',),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('baseentity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.baseentity')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('orderItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='base.order')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='base.product')),
            ],
            bases=('base.baseentity',),
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('baseentity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.baseentity')),
                ('name', models.CharField(max_length=120)),
                ('short_description', models.CharField(max_length=250)),
                ('full_description', models.TextField()),
                ('current_stock', models.IntegerField(default=0)),
                ('purchase_price', models.IntegerField(default=0)),
                ('sales_price', models.IntegerField(default=0)),
                ('promotional_price', models.IntegerField(default=0)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='inventory/%Y/%m/%d')),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productCategory', to='base.category')),
                ('tags', models.ManyToManyField(blank=True, related_name='inventory_tag', to='base.Tag')),
            ],
            bases=('base.baseentity',),
        ),
    ]
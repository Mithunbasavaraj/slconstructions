# Generated by Django 5.2 on 2025-05-09 18:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_inventory_name_alter_inventory_use_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='material_shifting_received',
            name='vehicle',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(blank=True, choices=[('Puducherry', 'Puducherry'), ('Delhi', 'Delhi'), ('Uttarakhand', 'Uttarakhand'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Tripura', 'Tripura'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Punjab', 'Punjab'), ('Dadra & Nagar Haveli & Daman & Diu', 'Dadra & Nagar Haveli & Daman & Diu'), ('TamilNadu', 'TamilNadu'), ('Sikkim', 'Sikkim'), ('Assam', 'Assam'), ('Lakshadweep', 'Lakshadweep'), ('Ladakh', 'Ladakh'), ('Odisha', 'Odisha'), ('Manipur', 'Manipur'), ('Andaman & Nicobar', 'Andaman & Nicobar'), ('West Bengal', 'West Bengal'), ('Chandigarh', 'Chandigarh'), ('Nagaland', 'Nagaland'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Chhattisgarh', 'Chhattisgarh'), ('Telangana', 'Telangana'), ('Jharkhand', 'Jharkhand'), ('Bihar', 'Bihar'), ('Haryana', 'Haryana'), ('Gujarat', 'Gujarat'), ('Mizoram', 'Mizoram'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Goa', 'Goa'), ('Karnataka', 'Karnataka'), ('Rajasthan', 'Rajasthan'), ('Maharashtra', 'Maharashtra'), ('Meghalaya', 'Meghalaya'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Kerala', 'Kerala')], default='', max_length=155),
        ),
        migrations.CreateModel(
            name='Project_investor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

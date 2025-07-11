# Generated by Django 5.2 on 2025-04-23 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_rename_punch_end_lat_attendance_lunch_end_lat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='lunch_in_photo',
            field=models.ImageField(blank=True, upload_to='attendance/'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='lunch_out_photo',
            field=models.ImageField(blank=True, upload_to='attendance/'),
        ),
        migrations.AlterField(
            model_name='material_shifting',
            name='Material_name',
            field=models.CharField(blank=True, choices=[('GI Pipes', 'GI Pipes'), ('RMC', 'RMC'), ('LED Street light', 'LED Street light'), ('Borewell Pumpset Materials', 'Borewell Pumpset Materials'), ('Concrete Solid Blocks 8', 'Concrete Solid Blocks 8'), ('Sanitary Item', 'Sanitary Item'), ('School desk and furniture', 'School desk and furniture'), ('Bricks', 'Bricks'), ('Stone - 20mm', 'Stone - 20mm'), ('Aluminum Window', 'Aluminum Window'), ('Electric Item', 'Electric Item'), ('Green Board and Notice Board', 'Green Board and Notice Board'), ('Granite', 'Granite'), ('Stone - 60mm', 'Stone - 60mm'), ('Stone - 40mm', 'Stone - 40mm'), ('Stones', 'Stones'), ('P Sand', 'P Sand'), ('PVC Pipes', 'PVC Pipes'), ('Steel', 'Steel'), ('M Sand', 'M Sand'), ('ACP', 'ACP'), ('Debris', 'Debris'), ('Concrete Solid Blocks 6', 'Concrete Solid Blocks 6'), ('Street light High Mast Poles', 'Street light High Mast Poles'), ('UPS and Batteries', 'UPS and Batteries'), ('Cement', 'Cement'), ('Concrete Solid Blocks 4', 'Concrete Solid Blocks 4')], default='', max_length=225),
        ),
        migrations.AlterField(
            model_name='material_shifting',
            name='vehicle',
            field=models.CharField(blank=True, choices=[('Canter', 'Canter'), ('Tipper', 'Tipper'), ('Tractor', 'Tractor'), ('Lorre', 'Lorre'), ('Auto', 'Auto'), ('JCB', 'JCB'), ('Tata-ace', 'Tata-ace')], default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Others', 'Others'), ('Female', 'Female')], default='', max_length=55),
        ),
        migrations.AlterField(
            model_name='profile',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('Married', 'Married'), ('Single', 'Single')], default='', max_length=155),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(blank=True, choices=[('Chandigarh', 'Chandigarh'), ('Karnataka', 'Karnataka'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Manipur', 'Manipur'), ('Uttarakhand', 'Uttarakhand'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('West Bengal', 'West Bengal'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Lakshadweep', 'Lakshadweep'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Maharashtra', 'Maharashtra'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Chhattisgarh', 'Chhattisgarh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Andaman & Nicobar', 'Andaman & Nicobar'), ('Bihar', 'Bihar'), ('Puducherry', 'Puducherry'), ('Dadra & Nagar Haveli & Daman & Diu', 'Dadra & Nagar Haveli & Daman & Diu'), ('Tripura', 'Tripura'), ('Kerala', 'Kerala'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('TamilNadu', 'TamilNadu'), ('Telangana', 'Telangana'), ('Jharkhand', 'Jharkhand'), ('Sikkim', 'Sikkim'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Rajasthan', 'Rajasthan'), ('Assam', 'Assam'), ('Nagaland', 'Nagaland'), ('Haryana', 'Haryana'), ('Delhi', 'Delhi'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Ladakh', 'Ladakh')], default='', max_length=155),
        ),
    ]

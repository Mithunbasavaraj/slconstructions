# Generated by Django 5.2 on 2025-04-22 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_project_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material_shifting',
            name='vehicle',
            field=models.CharField(blank=True, choices=[('Lorre', 'Lorre'), ('JCB', 'JCB'), ('Canter', 'Canter'), ('Tractor', 'Tractor'), ('Tata-ace', 'Tata-ace'), ('Auto', 'Auto'), ('Tipper', 'Tipper')], default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='project_daily_work_details',
            name='project_work_status',
            field=models.CharField(blank=True, default='', max_length=225),
        ),
    ]

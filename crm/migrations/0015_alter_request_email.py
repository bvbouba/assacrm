# Generated by Django 5.1.2 on 2024-10-13 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0014_alter_lead_company_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='email',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
    ]

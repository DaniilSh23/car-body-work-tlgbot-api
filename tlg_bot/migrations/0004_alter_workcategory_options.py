# Generated by Django 4.0.4 on 2022-05-25 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tlg_bot', '0003_alter_applications_application_text_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workcategory',
            options={'ordering': ['-id'], 'verbose_name': 'Категория работ', 'verbose_name_plural': 'Категории работ'},
        ),
    ]

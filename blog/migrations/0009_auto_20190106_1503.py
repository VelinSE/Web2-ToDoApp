# Generated by Django 2.1.3 on 2019-01-06 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20181229_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='recepie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='blog.Post'),
            preserve_default=True
        ),
    ]
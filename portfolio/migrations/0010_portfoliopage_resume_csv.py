# Generated by Django 2.0 on 2019-02-25 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0007_merge'),
        ('portfolio', '0009_remove_portfoliopage_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliopage',
            name='resume_csv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document'),
        ),
    ]

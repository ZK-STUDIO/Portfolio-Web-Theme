# Generated by Django 2.0 on 2019-02-25 19:41

from django.db import migrations, models
import wagtailmd.utils


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_portfoliopage_resume_csv'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliopage',
            name='header_content',
            field=wagtailmd.utils.MarkdownField(blank=True, verbose_name='Header Content'),
        ),
        migrations.AddField(
            model_name='portfoliopage',
            name='header_title',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]

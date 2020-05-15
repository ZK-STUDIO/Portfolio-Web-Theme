# Generated by Django 2.0 on 2019-03-12 20:51

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_auto_20190312_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliopage',
            name='project',
            field=wagtail.core.fields.StreamField((('project', wagtail.core.blocks.StructBlock((('name', wagtail.core.blocks.CharBlock(classname='full title')), ('menu_title', wagtail.core.blocks.CharBlock(classname='full title')), ('project_url', wagtail.core.blocks.CharBlock(classname='full title'))))),), blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portfoliopage',
            name='project_title',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]

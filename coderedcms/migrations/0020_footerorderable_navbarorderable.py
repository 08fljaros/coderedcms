# Generated by Django 3.1.7 on 2021-03-12 19:53

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('coderedcms', '0019_spelling_corrections'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavbarOrderable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('navbar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coderedcms.navbar')),
                ('navbar_chooser', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='site_navbar', to='coderedcms.layoutsettings', verbose_name='Site Navbars')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FooterOrderable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('footer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coderedcms.footer')),
                ('footer_chooser', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='site_footer', to='coderedcms.layoutsettings', verbose_name='Site Footers')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
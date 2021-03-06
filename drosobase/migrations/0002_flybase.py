# Generated by Django 2.0.5 on 2018-05-25 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drosobase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flybase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FBst_idx', models.CharField(default='', max_length=12)),
                ('collection_name', models.CharField(default='', max_length=12)),
                ('stock_type_cv', models.TextField()),
                ('species', models.CharField(default='', max_length=10)),
                ('FB_genotype', models.TextField()),
                ('description', models.TextField()),
                ('stock_number', models.CharField(default='', max_length=12)),
            ],
            options={
                'db_table': 'flybase',
            },
        ),
    ]

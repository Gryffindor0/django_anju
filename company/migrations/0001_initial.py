# Generated by Django 2.1.7 on 2019-03-31 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='companyImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='companyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('contact_tel', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('case_num', models.IntegerField()),
                ('work_site_num', models.IntegerField()),
                ('favorable_rate', models.CharField(max_length=30)),
                ('bond', models.IntegerField()),
                ('mouth_value', models.IntegerField()),
                ('company_icon', models.CharField(max_length=100)),
                ('price', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='search.price')),
            ],
        ),
        migrations.CreateModel(
            name='companyStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.companyInfo')),
                ('style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.style')),
            ],
        ),
        migrations.CreateModel(
            name='district',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='companyimg',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='company.companyInfo'),
        ),
    ]

# Generated by Django 2.1.7 on 2019-03-20 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_status', models.CharField(default='正在预约', max_length=30)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.companyInfo')),
            ],
        ),
        migrations.CreateModel(
            name='houseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('area', models.IntegerField()),
                ('village', models.CharField(max_length=30, null=True)),
                ('address', models.CharField(max_length=30)),
                ('house_status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='houseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='identifyingCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_code', models.CharField(max_length=255)),
                ('code_content', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='sex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='userIcon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=255)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(max_length=30, unique=True)),
                ('nickname', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=255)),
                ('QQ', models.CharField(max_length=30, null=True)),
                ('address', models.CharField(max_length=30, null=True)),
                ('regist_data', models.DateTimeField(auto_now_add=True)),
                ('sex', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.sex')),
                ('userIcon', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.userIcon')),
            ],
        ),
        migrations.AddField(
            model_name='houseinfo',
            name='houseType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.houseType'),
        ),
        migrations.AddField(
            model_name='houseinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.userInfo'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.houseInfo'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.userInfo'),
        ),
    ]

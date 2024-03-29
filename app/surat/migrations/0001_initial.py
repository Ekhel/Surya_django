# Generated by Django 2.2.4 on 2019-09-24 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='surat_masuk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asal_surat', models.CharField(max_length=100)),
                ('kode', models.CharField(max_length=30)),
                ('perihal', models.CharField(max_length=150)),
                ('tgl_surat', models.DateTimeField()),
                ('tgl_terima', models.DateTimeField()),
                ('file', models.FileField(upload_to='documents/')),
                ('keterangan', models.CharField(max_length=225)),
            ],
        ),
    ]

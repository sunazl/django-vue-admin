# Generated by Django 3.0.7 on 2020-06-15 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from apps.system import fileds


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_auto_20200609_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicaldict',
            name='enabled',
        ),
        migrations.AddField(
            model_name='dict',
            name='other',
            field=fileds.JSONField(blank=True, null=True, verbose_name='其它信息'),
        ),
        migrations.AddField(
            model_name='historicaldict',
            name='other',
            field=fileds.JSONField(blank=True, null=True, verbose_name='其它信息'),
        ),
        migrations.AlterField(
            model_name='dict',
            name='name',
            field=models.CharField(max_length=100, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='file',
            name='create_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='file_create_by', to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='file',
            name='update_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='file_update_by', to=settings.AUTH_USER_MODEL, verbose_name='最后编辑人'),
        ),
        migrations.AlterField(
            model_name='historicaldict',
            name='name',
            field=models.CharField(max_length=100, verbose_name='名称'),
        ),
        # migrations.AlterUniqueTogether(
        #     name='dict',
        #     unique_together={('name', 'code', 'type')},
        # ),
        migrations.RemoveField(
            model_name='dict',
            name='enabled',
        ),
    ]

# Generated by Django 4.2.9 on 2024-01-28 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_celery_results', '0011_taskresult_periodic_task_name'),
        ('app', '0002_delete_taskresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('webhook_url', models.URLField()),
                ('message_id', models.IntegerField()),
                ('celery_task_result', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='django_celery_results.taskresult')),
            ],
        ),
    ]

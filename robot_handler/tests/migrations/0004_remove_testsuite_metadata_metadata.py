# Generated by Django 4.1.3 on 2022-12-07 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_remove_testcase_tags_remove_testsuite_force_tags_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testsuite',
            name='metadata',
        ),
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.CharField(blank=True, max_length=50, null=True)),
                ('test_suite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.testsuite')),
            ],
        ),
    ]

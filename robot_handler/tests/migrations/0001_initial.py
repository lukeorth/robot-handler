# Generated by Django 4.1.3 on 2022-12-08 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileLocations',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('location', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='TestCategory',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TestSuite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('documentation', models.TextField(blank=True)),
                ('suite_setup', models.CharField(blank=True, max_length=200, verbose_name='suite setup')),
                ('suite_teardown', models.CharField(blank=True, max_length=200, verbose_name='suite teardown')),
                ('test_setup', models.CharField(blank=True, max_length=200, verbose_name='test setup')),
                ('test_teardown', models.CharField(blank=True, max_length=200, verbose_name='test teardown')),
                ('test_timeout', models.CharField(blank=True, max_length=200, verbose_name='test timeout')),
                ('source', models.FileField(upload_to='')),
                ('test_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tests.testcategory')),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('documentation', models.TextField(blank=True)),
                ('setup', models.CharField(blank=True, max_length=200)),
                ('teardown', models.CharField(blank=True, max_length=200)),
                ('timeout', models.CharField(blank=True, max_length=200)),
                ('body', models.TextField(blank=True)),
                ('source', models.FileField(upload_to='')),
                ('test_suite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.testsuite')),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('test_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.testcase')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('test_case', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tests.testcase')),
                ('test_suite', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tests.testsuite')),
            ],
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
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('test_suite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.testsuite')),
            ],
        ),
    ]

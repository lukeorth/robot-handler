import os
from django.conf import settings
from django.db import models
from django.urls import reverse 


class FileLocations(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    location = models.FileField()

    def __str__(self):
        return self.name

class TestCategory(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class TestSuite(models.Model):
    name = models.CharField(max_length=200)
    test_category = models.ForeignKey(TestCategory, blank=True, null=True, on_delete=models.CASCADE)
    documentation = models.TextField(blank=True)
    suite_setup = models.CharField('suite setup', blank=True, max_length=200)
    suite_teardown = models.CharField('suite teardown', blank=True, max_length=200)
    test_setup = models.CharField('test setup', blank=True, max_length=200)
    test_teardown = models.CharField('test teardown', blank=True, max_length=200)
    test_timeout = models.CharField('test timeout', blank=True, max_length=200)
    source = models.FileField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tests:test_suite', args=[str(self.id)])

class TestCase(models.Model):
    test_suite = models.ForeignKey(TestSuite, on_delete=models.CASCADE)
    name = models.CharField(blank=True, max_length=200)
    documentation = models.TextField(blank=True)
    setup = models.CharField(blank=True, max_length=200)
    teardown = models.CharField(blank=True, max_length=200)
    timeout = models.CharField(blank=True, max_length=200)
    body = models.TextField(blank=True)
    source = models.FileField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tests:test_case', args=[str(self.test_suite.id), str(self.id)])

class Tag(models.Model):
    test_suite = models.ForeignKey(TestSuite, blank=True, null=True, on_delete=models.SET_NULL)
    test_case = models.ForeignKey(TestCase, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Metadata(models.Model):
    test_suite = models.ForeignKey(TestSuite, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    value = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Library(models.Model):
    test_suite = models.ForeignKey(TestSuite, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Template(models.Model):
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
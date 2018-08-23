from __future__ import unicode_literals

from django.db import models

class Job(models.Model):
	employer = models.CharField(max_length=32)
	title = models.CharField(max_length=32)
	summary = models.TextField(max_length=5000)
	start_date = models.DateField(auto_now=False)
	end_date = models.DateField(auto_now=False)

	def __str__(self):
		return self.employer


class Education(models.Model):
	university = models.CharField(max_length=64)
	location = models.CharField(max_length=32)
	major = models.CharField(max_length=64)
	minor = models.CharField(max_length=64, blank=True, null=True)
	start_semester = models.CharField(max_length=32, blank=True, null=True)
	start_year = models.DateField(auto_now=False, blank=True, null=True)
	semester = models.CharField(max_length=32, blank=True, null=True)
	year = models.DateField(auto_now=False)

	def __str__(self):
		return self.university

	class Meta:
		verbose_name_plural = "Education"


class GeneralInfo(models.Model):
	about = models.TextField(max_length=5000)
	executive_summary = models.TextField(max_length=5000)
	skills = models.TextField(max_length=5000)
	privacy_policy = models.TextField(max_length=10000)

	def __str__(self):
		return "General Info"

	class Meta:
		verbose_name_plural = "General Info"

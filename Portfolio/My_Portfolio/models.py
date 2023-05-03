from django.db import models
from datetime import datetime

class Certificates(models.Model):
    cert = models.ImageField(upload_to = 'certificates/', null = True)

class Projects(models.Model):
    name = models.CharField(max_length = 50, null = True)
    description = models.TextField()
    image = models.ImageField(upload_to = 'projects/', null = True)

class Education(models.Model):
    course = models.CharField(max_length = 100, null=True)
    start_year = models.PositiveSmallIntegerField(null=True)
    end_year =models.CharField(max_length = 10, null = True)
    school = models.CharField(max_length = 100, null = True)
    city = models.CharField(max_length = 50, null = True)

class Languages(models.Model):
    language = models.CharField(max_length = 50, null = True)
    level = models.IntegerField(null=True, blank=True)

class Technical_Skills(models.Model):
    skill = models.CharField(max_length = 100, null = True)

# class Soft_Skills(models.Model):
#     skill = models.CharField(max_length = 100, null = True)
#     desc = models.CharField(max_length = 100, null = True, blank = True)

class Experience(models.Model):
    position = models.CharField(max_length = 50, null = True)
    start_year = models.PositiveSmallIntegerField(null=True)
    end_year = models.CharField(max_length = 10, null = True)
    description = models.TextField(null = True)
    company = models.CharField(max_length = 100, null = True)
    city = models.CharField(max_length = 50, null = True)

class PersonalInfo(models.Model):
    name = models.CharField(max_length = 50, null = True)
    about = models.TextField()
    tag_line = models.TextField()
    address = models.CharField(max_length = 50, null = True)
    city = models.CharField(max_length = 50, null = True)
    email = models.EmailField()
    # language = models.ManyToManyField(Languages)
    # tech_skill = models.ManyToManyField(Technical_Skills)
    # soft_skill = models.ManyToManyField(Soft_Skills)
    # experience = models.ManyToManyField(Experience)
    # certificate = models.ManyToManyField(Certificates)
    # project = models.ManyToManyField(Projects)
    statement = models.TextField(null=True, blank=True)
    # education = models.ManyToManyField(Education)
    facebook = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    contact = models.CharField(max_length=20, null=True)
    image = models.ImageField (upload_to = 'pics/', null = True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length = 100, null = True, blank = True)
    email = models.EmailField()
    message = models.TextField()
    subject = models.CharField(max_length = 100, null = True, blank = True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    # @property
    # def Date(self):
    #     date = self.date.strftime("%B %m, %Y")
    #     return date


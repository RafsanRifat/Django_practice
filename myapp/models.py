from django.db import models
from django.utils.timezone import now
from PIL import Image
from django.utils.text import slugify
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Class_in(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    CATEGORY = (
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    )
    MEDIUM = (
        ('Bangla', 'Bangla'),
        ('English', 'English'),
        ('Urdu', 'Urdu'),
        ('Turkey', 'Turkey'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, default=title)
    email = models.EmailField()
    salary = models.FloatField()
    details = models.TextField()
    available = models.BooleanField()
    category = models.CharField(max_length=100, choices=CATEGORY)
    created_at = models.DateTimeField(default=now)
    image = models.ImageField(default='/myapp/images/default.jpg', upload_to='myapp/images')
    medium = MultiSelectField(max_length=150, choices=MEDIUM, max_choices=5, default='Bangla')
    subject = models.ManyToManyField(Subject, related_name='subject_set')
    class_in = models.ManyToManyField(Class_in, related_name='class_set')

    def save(self):
        self.slug = slugify(self.title)
        super().save()  # saving image first
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (500, 320)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return self.title

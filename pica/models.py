from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
# from ckeditor.fields import RichTextField
from django.utils import timezone

from .validators import validate_empty
from ckeditor_uploader.fields import RichTextUploadingField


class Company(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Company Code")
    description = models.CharField(max_length=100, blank=True, null=True, verbose_name="Company Name")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('create-company')


class Departemen(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Nama Divisi/Departemen")
    description = models.CharField(max_length=100, blank=True, null=True, verbose_name="Description")
    dir_in_charge = models.CharField(max_length=50, blank=True, null=True)
    email_dir_in_charge = models.EmailField(blank=True, null=True)
    dept_head_in_charge = models.CharField(max_length=50, blank=True, null=True)
    email_dept_head_in_charge = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name


class Peserta(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nama Peserta", null=True,
                            blank=True)
    email = models.EmailField(null=True, blank=True, verbose_name="Email address")
    peserta2company = models.ForeignKey(Company, on_delete=models.SET_NULL, related_name="company2peserta", null=True,
                                        verbose_name="Company")
    peserta2departemen = models.ForeignKey(Departemen, on_delete=models.CASCADE, verbose_name="Departemen",
                                           null=True, blank=True)
    bod = models.BooleanField(default=False, verbose_name="Apakah masuk dalam list BOD?")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('create-peserta')


class Forum(models.Model):
    nama_forum = models.CharField(max_length=100, null=True, blank=True, validators=[validate_empty])
    keterangan = models.CharField(max_length=200, null=True, blank=True)
    forum2company = models.ForeignKey(Company, null=True, on_delete=models.CASCADE, related_name="company2forum")

    def __str__(self):
        return self.nama_forum


class Meeting(models.Model):
    meeting2forum = models.ForeignKey(Forum, on_delete=models.CASCADE, blank=True, null=True,
                                      related_name="forum2meeting", verbose_name="Forum")
    title = models.CharField(max_length=100, null=True, blank=True)
    meeting_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    organizer = models.CharField(max_length=50, blank=True, null=True)
    notulen = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    meeting2peserta = models.ManyToManyField(Peserta, related_name="peserta2meeting", verbose_name="Peserta meeting")

    def __str__(self):
        return self.title


class Topik(models.Model):
    STATUS = (
        ('OPEN', 'OPEN'),
        ('HOLD', 'HOLD'),
        ('PROGRESS', 'PROGRESS'),
        ('CLOSE', 'CLOSE')
    )
    topik2meeting = models.ForeignKey(Meeting, verbose_name="Meeting", null=True,
                                      related_name="meeting2topik", on_delete=models.SET_NULL)
    topik2departemen = models.ForeignKey(Departemen, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name="departemen2topik", verbose_name="Function/Divisi/Departemen")
    topik2company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True,
                                      related_name="company2topik",
                                      verbose_name="Problem Owner")
    nama_topik = models.CharField(max_length=100, null=True, blank=True, verbose_name="Topik")
    problem = RichTextUploadingField(blank=True, null=True, verbose_name="Problem")
    action = RichTextUploadingField(blank=True, null=True, verbose_name="Action")
    date_created = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=False, verbose_name="Due date")
    topik2user = models.ManyToManyField(User, verbose_name="Person in charge",
                                        related_name="user2topik")
    status = models.CharField(max_length=8, choices=STATUS, default="OPEN")
    expired = models.BooleanField(default=False)

    def __str__(self):
        return self.nama_topik

    def get_absolute_url(self):
        return reverse('list_topik')


class Activity(models.Model):
    STATUS = (
        ('OPEN', 'OPEN'),
        ('HOLD', 'HOLD'),
        ('PROGRESS', 'PROGRESS'),
        ('CLOSE', 'CLOSE')
    )
    activity2topik = models.ForeignKey(Topik, on_delete=models.CASCADE, null=True, related_name="topik2activity")
    date_activity = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True,
                                     verbose_name="Date Activity", default=timezone.now)
    keterangan = models.CharField(max_length=255)
    activity2user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user2activity",
                                      verbose_name="PIC")
    due_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True,
                                verbose_name="Due Date")
    expired = models.BooleanField(default=False)
    status = models.CharField(max_length=8, choices=STATUS, default="OPEN")

    def __str__(self):
        return self.keterangan[:50]

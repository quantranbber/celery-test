from django.db import models


class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    store_id = models.IntegerField()
    name = models.CharField(max_length=50)


class LogData(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now_add=True, blank=True)
    store_id = models.IntegerField()
    user_id = models.IntegerField()
    content = models.CharField(max_length=255)

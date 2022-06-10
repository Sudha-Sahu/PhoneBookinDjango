from django.db import models


class Contact(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_num = models.CharField(max_length=10, unique=True)
    address = models.TextField(max_length=300)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

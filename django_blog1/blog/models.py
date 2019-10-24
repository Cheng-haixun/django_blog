from django.db import models

# Create your models here.

class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=20)
    u_email = models.CharField(max_length=20)

class Blog(models.Model):
    b_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    detail = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now=True, null=True)
    photo = models.CharField(max_length=100)
    commentcount = models.IntegerField()
    userobj = models.ForeignKey(to="User",to_field="u_id",on_delete=models.CASCADE)

class Comment(models.Model):
    c_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=300,null=True)
    date = models.DateTimeField(auto_now=True,null=True)
    # count = models.IntegerField(max_length=100)
    userobj = models.ForeignKey(to="User",to_field="u_id",on_delete=models.CASCADE)
    blogobj = models.ForeignKey(to="Blog",to_field="b_id",on_delete=models.CASCADE)

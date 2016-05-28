from django.db import models

class Page(models.Model):
    url = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)




class Sentence(models.Model):
    page = models.ForeignKey(Page)
    body = models.TextField(max_length=1024,null=True,default="")
    comment = models.TextField(null=True,default="")
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)

class Term(models.Model):
    sentence = models.ForeignKey(Sentence)
    body = models.CharField(max_length=128,null=True,default="")
    term_class = models.CharField(max_length=30)
    result =  models.TextField(null=True,default="")
    comment = models.TextField(null=True,default="")
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)


class DragonHistory(models.Model):
    age = models.IntegerField()
    event = models.TextField(null=True,default="")
    comment = models.TextField(null=True,default="")

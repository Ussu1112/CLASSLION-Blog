from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summery(self):
        return self.body[:100]

class BuyItem(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summery(self):
        return self.body[:100]

class SellItem(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    sell_image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summery(self):
        return self.body[:100]
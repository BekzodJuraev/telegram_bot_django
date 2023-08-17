from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Add_item(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    id= models.AutoField(primary_key=True)
    image=models.ImageField(verbose_name='Иконки')
    price=models.IntegerField()
    name=models.CharField(max_length=200)
    file_tgs=models.FileField(null=True)
    created=models.DateTimeField(auto_now_add=True)
    desc=models.CharField(max_length=200,null=True)


    def __str__(self):
        return f'{self.name}'



    class Meta:
        ordering=['created']







class Bot(models.Model):
    #diary = models.ForeignKey(Diary, on_delete=models.CASCADE,related_name='related_diaries', null=True)
    id = models.AutoField(primary_key=True)
    order_choice=models.CharField(max_length=200,null=True)
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    id_user = models.IntegerField(null=True)
    comment=models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    adress=models.CharField(max_length=200,blank=True,null=False)
    phone=models.IntegerField(null=True)
    latitude = models.FloatField(blank=True,null=True)
    longitude = models.FloatField(blank=True,null=True)








    def __str__(self):
        return self.name



    class Meta:
        ordering=['created']







class OrderItem(models.Model):
    order=models.ForeignKey(Bot,on_delete=models.CASCADE,related_name="related_diaries",null=True)
    add_item=models.ForeignKey(Add_item, on_delete=models.CASCADE, null=True)
    count=models.IntegerField()

    def __str__(self):
        return f'{self.add_item.name}'

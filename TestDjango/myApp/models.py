from django.db import models

# Create your models here.
class Grades(models.Model):
    gname = models.CharField(max_length=30)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum  = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.gname

#学生
class Students(models.Model):
    sname = models.CharField(max_length=30)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length=30)  #简介
    isDelete = models.BooleanField(default=False)
    # 关联外键,一对多设计　多方持有一方的外键
    sgrade = models.ForeignKey('Grades',on_delete=models.CASCADE)
    def __str__(self):
        return self.sname
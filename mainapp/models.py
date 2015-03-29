from django.db import models

# Create your models here.
class Appeal(models.Model):
    # id default by inherit
    title = models.CharField(max_length=50)
    context = models.TextField()
    
    postUser_id = models.PositiveIntegerField()
    department = models.CharField(max_length=2,
                                  default = 'NA') # NA is non-defined
    grade = models.CharField(max_length=1,
                             default = '0')
    process_status = models.CharField(max_length=1, 
                                      default='N')
    # 'N' is non-process
    # 'P' is processing
    # 'D' us done

    subscribe_num = models.PositiveIntegerField(default=0)

    public = models.BooleanField(default=True)
    
    visible = models.BooleanField(default=True)
    # visible/nonvisible to the front-end

class Reply(models.Model):
    appeal = models.ForeignKey(Appeal)
    reply_user_id = models.PositiveIntegerField()
    content = models.TextField()
    pub_date = models.DateTimeField()

class Subscribe(models.Model):
    appeal = models.ForeignKey(Appeal)
    subscribe_user_id = models.PositiveIntegerField()
    

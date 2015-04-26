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
    pub_date = models.DateTimeField()
    
    public = models.BooleanField(default=True)
    visible = models.BooleanField(default=True)
    # visible/nonvisible to the front-end

    def __str__(self):
        return 'Pk:{0},title:{1}'.format(self.pk,self.title)

    
class Reply(models.Model):
    appeal = models.ForeignKey('Appeal', related_name='appeal_replys')

    reply_user_id = models.PositiveIntegerField()
    content = models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return 'Pk:{0},title:{1}'.format(self.pk,self.title)


class Subscribe(models.Model):
    appeal = models.ForeignKey('Appeal', related_name='appeal_subscribes')
    subscribe_user_id = models.PositiveIntegerField()

    def __str__(self):
        return 'Pk:{0},title:{1}'.format(self.pk,self.title)

   

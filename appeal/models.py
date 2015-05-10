# 2015/05/04 edit by Lego
# add postUser_name field to every models


# 2015/05/01 edit by Lego
# update Appeal.__str__
# change visiable to is_delete and
# change type bool to datetime
# chage integer field to char
# not use subscribe_num, just count the model subscribe num

# 2015/04/01 edit by lego
from django.db import models
from django.core.urlresolvers import reverse # in order to use get_absolute_url

# Create your models here.
class Appeal(models.Model):
    # id default by inherit
    title = models.CharField(max_length=50)
    context = models.TextField()
    
    postUser_id = models.CharField(max_length=50)
    
    postUser_name = models.CharField(default='', max_length=50)

    department = models.CharField(max_length=2,
                                  default = 'NA') # NA is non-defined
    grade = models.CharField(max_length=1,
                             default = '0')
    process_status = models.CharField(max_length=1, 
                                      default='N')
    # 'N' is non-process
    # 'P' is processing
    # 'D' us done

    # subscribe_num = models.PositiveIntegerField(default=0)

    pub_date = models.DateTimeField(auto_now_add=True)
    
    is_public = models.BooleanField(default=True)

    is_delete = models.DateTimeField(null=True)
    # visible/nonvisible to the front-end
    
    def get_absolute_url(self):
        return reverse('appeal:detail' ,kwargs={'pk':self.pk})

    def __str__(self):
        return \
        'pk:{}\n'.format(self.pk) + \
        'title:{}\n'.format(self.title) + \
        'context:{}\n'.format(self.context) + \
        'postUser_id:{}\n'.format(self.postUser_id) + \
        'department:{}\n'.format(self.department) + \
        'grade:{}\n'.format(self.grade) + \
        'process_status:{}\n'.format(self.process_status) + \
        'pub_date:{}\n'.format(self.pub_date) + \
        'is_public:{}\n'.format(self.is_public) + \
        'is_delete:{}\n'.format(self.is_delete)

    
class Reply(models.Model):

    appeal = models.ForeignKey('Appeal', related_name= 'apeal_reply', default='')

    postUser_id = models.CharField(max_length=50)
    postUser_name = models.CharField(default='',max_length=50)

    context = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Pk:{0},title:{1}'.format(self.pk,self.title)

# ERROR : EDIT IT
# CHANGE IT TO SUBSCRIBE TO USER
class Subscribe(models.Model):
    appeal = models.ForeignKey('Appeal', related_name='appeal_subscribes')
    subscribe_user_id = models.CharField(max_length=50)
    # chage integer field to char
    # 2015/04/01 edit by lego
    def __str__(self):
        return 'Pk:{0},title:{1}'.format(self.pk,self.title)


# TODO:
#   appeal.getSubscribeNum()
#   appeal.get_replyNum()
#   appeal.get_backend_url()
# DONE:
#   appeal.get_process_status()
# NOTE:
#   1. username is the id of a person
#
# 2015/08/06 edit by Lego
#   --BIG CHANGE OF MODEL.PY--
#   skip the describe of change just see the source
#
# 2015/06/22 edit by Lego
#   Change department to CharField
#
# 2015/05/04 edit by Lego
#   add postUser_name field to every models
#
# 2015/05/01 edit by Lego
#   update Appeal.__str__
#   change visiable to is_delete and
#   change type bool to datetime
#   chage integer field to char
#   not use subscribe_num, just count the model subscribe num
#
# 2015/04/01 Create by lego

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse # in order to use get_absolute_url

from base.refrence import GradeChoice, DepartChoice, ProcessStatusChoice
class Appeal(models.Model):
    username = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True)

    name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        default='')
    sid = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        default='')
    department = models.CharField(
        max_length=5,
        null=True,
        blank=True,
        default='',
        choices=DepartChoice)
    grade = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        default='',
        choices=GradeChoice)

    process_status = models.CharField(
        verbose_name='申訴狀態',
        max_length=1,
        default='N',
        choices=ProcessStatusChoice)

    title = models.CharField(
        max_length=50,
        default='',
        blank=False)
    context = models.TextField(
        blank=False)


    pub_date = models.DateTimeField(
        auto_now_add=True)
    is_public = models.BooleanField(
        default=True)
    is_delete = models.DateTimeField(
        null=True,
        blank=True)
    # visible/nonvisible to the front-end

    def get_absolute_url(self):
        return reverse('appeal:detail' ,
            kwargs={'pk':self.pk})
    def get_absolute_admin_url(self):
        return reverse(3)
#TODO
    def get_backend_url(self):
        pass
        #return reverse('', kwargs={'pk':self.pk})
    @property
    def process_status_str(self):
        for data, str in ProcessStatusChoice:
            if data is self.process_status:
                return str
        return ''
    @property
    def grade_str(self):
        for data, str in GradeChoice:
            if data is self.grade:
                return str
        return ''
    @property
    def department_str(self):
        for data, str in DepartChoice:
            if data is self.department:
                return str
        return ''
#TODO 
    def get_subscribeNum(self):
        pass
#TODO
    def get_replyNum(self):
        pass

    def __str__(self):
        return self.title


class Reply(models.Model):
    username = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True)
    context = models.TextField()
    pub_date = models.DateTimeField(
        auto_now_add=True)

    appeal = models.ForeignKey(
        'Appeal',
        related_name= 'reply', 
        default='')

    def __str__(self):
        return '{} reply {}'.format(self.username,
            self.appeal.title)

# ERROR : EDIT IT
# CHANGE IT TO SUBSCRIBE TO USER
class Subscribe(models.Model):
    appeal = models.ForeignKey(
        'Appeal',
         related_name='appeal_subscribes')
    subscribe_username = models.CharField(
        max_length=50,
        default='')
    # chage integer field to char
    # 2015/04/01 edit by lego
    def __str__(self):
        return '{} subscribe {}'.format(self.subscribe_username,
            self.appeal.title)

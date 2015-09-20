from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from base.refrence import GradeChoice, DepartChoice
# Create your models here.

class AppealUserManager(BaseUserManager):
  def create_user(self, 
    email, name, nick, sid,
    department, grade,
    password=None):
    
    if not email:
      raise ValueError('Users must have an email address')

    user = self.model(
      email = self.normalize_email(email),
      name = name,
      nick = nick,
      sid = sid,
      department = department,
      grade = grade,
    )

    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self,
    email, name, nick, sid,
    department, grade,
    password):
    user = self.create_user(
      email = email,
      name = name,
      nick = nick, 
      sid = sid,
      department = department,
      grade = grade,
      password=password)
    user.is_admin = True
    user.is_superuser = True
    user.save(using=self._db) 
    print('create_superuser is execute!')
    return user

class AppealUser(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(
    verbose_name = '電子信箱',
    max_length = 255,
    unique=True,
    blank=False)  

  name = models.CharField(
    verbose_name = '名字',
    max_length = 30,
    blank=False)  
  nick = models.CharField(
    verbose_name = '暱稱', 
    max_length = 30,
    blank=False)
  sid = models.CharField(
    verbose_name = '學號',
    max_length = 30,
    default='',
    blank=False)
  department = models.CharField(
    verbose_name = '系所',
    max_length = 5,
    default = '',
    blank=False,
    choices=DepartChoice)
  grade = models.CharField(
    verbose_name = '年級',
    max_length = 1,
    blank=False,
    choices=GradeChoice)

  date_of_birth = models.DateTimeField(
    auto_now_add=True)
  is_active = models.BooleanField(
    default=True)
  is_admin = models.BooleanField(
    default=False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = [
    'name','nick','sid','department','grade',
    ]

  objects = AppealUserManager()

  def get_full_name(self):
    return self.email
  def get_short_name(self):
    return self.email.split('@')[0]

  def has_perm(self, perm, obj=None):
    return True

  def has_module_perms(self, app_label):
    return True

  @property
  def is_staff(self):
    return self.is_admin

  @property
  def grade_str(self):
    for data, str in GradeChoice:
      if data == self.grade:
        return str
    return ''

  @property
  def department_str(self):
    print(self.department)
    for data, str in DepartChoice:
      if data == self.department:
        return str
    return ''

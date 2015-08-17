from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .refrence import GradeChoice, DepartChoice

class AppealUserManager(BaseUserManager):
	def create_user(self, 
		email, name, nick,
		department, grade,
		password=None):
		
		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
			email = self.normalize_email(email),
			name = name,
			nick = nick,
			department = department,
			grade = grade,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,
		email, name, nick,
		department, grade,
		password):
		user = self.create_user(
			email, name, nick, 
			department, grade,
			password=password)
		user.is_admin = True
		user.save(using=self._db)	
		return user

class AppealUser(AbstractBaseUser):
	email = models.EmailField(
		verbose_name = 'email address',
		max_length = 255,
		unique=True)	

	name = models.CharField(
		max_length = 30)	
	nick = models.CharField(
		max_length = 30)
	department = models.CharField(
		max_length = 5,
		default = '',
		choices=DepartChoice)
	grade = models.CharField(
		max_length = 1,
		choices=GradeChoice)

	date_of_birth = models.DateTimeField(
		auto_now_add=True)
	is_active = models.BooleanField(
		default=True)
	is_admin = models.BooleanField(
		default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = [
		'name','nick','department','grade',
		]

	objects = AppealUserManager()
	
	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	def is_staff(self):
		return self.is_admin
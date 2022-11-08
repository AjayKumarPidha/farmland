from distutils.command.upload import upload
import email
from email.mime import image
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from django.views import View

####### Custom Model Manager ########
######

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name , last_name, phone_number, password):

        if not email:
            raise ValueError("The Email must be set")

        if not first_name:
            raise ValueError("The first_name must be set")

        if not last_name:
            raise ValueError("The last_name must be set")

        user  = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number
        )
        user.set_password(password)
        user.save(using = self._db)
        return user 

########## Super User ##########

    def create_superuser(self, email, first_name,phone_number,last_name,password):
        """
        Creates and saves a superuser with the given email, name, and password.
        """
        user = self.create_user(
            email,
            first_name= first_name,
            last_name=last_name,
            phone_number = phone_number,
            password=password,
      
        )
        user.is_admin = True
        user.save(using=self._db)
        return user   

########### Custom User Model ###########

class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="Email", max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin





########### Contact us Model ############

class FarmerContactUs(models.Model):
    full_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    email_address = models.EmailField(unique=True)
    message = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)


######### Request An Estimate Model ###########

class ServiceType(models.Model):
    service_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.service_name


class RequestAnEstimate(models.Model):
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null= True)
    phone_number = models.CharField(max_length=40, blank= True, null=True)
    massage = models.CharField(max_length=400, blank=True,null=True)


######### Frequently Ask Question Services Model ###########

class AskQuestions(models.Model):
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class AnswerList(models.Model):
    ask = models.ForeignKey(AskQuestions, on_delete=models.CASCADE, related_name='questionby')
    answer = models.CharField(max_length=250)

    def __str__(self):
        return self.answer

class ServiceView(models.Model):
    headding = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField()

    def __str__(self):
        return self.headding


class EmailSubscribers(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class ProjectView(models.Model):
    headding = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.headding

class ContactImage(models.Model):
    image = models.ImageField()


######### Explore Project Model ##########

class ExploreProject(models.Model):
    headding = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.headding

######### Completed Project Model ##########

class CompletedProject(models.Model):
    headding = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return self.headding


######### Blog Model ##########

class BlogModel(models.Model):
    image = models.ImageField()
    headding = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.headding





    








# Create your models here.

# class FarmlandBlog(models.Model):
#     heading = models.CharField(max_length=200)
#     description = models.CharField(max_length=400)
#     image = models.ImageField(upload_to = None)
#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         self.heading

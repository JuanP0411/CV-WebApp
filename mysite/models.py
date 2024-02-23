from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'
    
    name = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to="skills")
    is_key_skill = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class Projects(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=10000)
    link = models.CharField(max_length=100)
    skills = models.ManyToManyField(Skill)
    slug = models.SlugField(unique=True,null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio")
    #various project uses various skills * 
    def __str__(self) -> str:
        return self.name

class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")
    age = models.IntegerField(null=True)
    email = models.CharField(max_length=100,null=True)
    github = models.CharField(max_length=100,null=True)
    linkedin = models.CharField(max_length=100,null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Experience(models.Model):
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    workplace_name = models.CharField(max_length=30)
    jobtitle = models.CharField(max_length=30)
    person = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    thumbnail = models.ImageField(blank=True, null=True, upload_to="experiences")

    #one experience can have many acomplishments * 
    
    def __str__(self) -> str:
        return self.jobtitle

class Acomplishment(models.Model):
    description = models.CharField(max_length=100)
    experience = models.ForeignKey(Experience,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.description


class Certificate(models.Model):

    class Meta:
        verbose_name_plural = 'Certificates'
        verbose_name = 'Certificate'

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    person = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
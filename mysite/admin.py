from django.contrib import admin

from .models import Experience, Acomplishment, Skill, Projects,UserProfile,Certificate
admin.site.register(Experience)
admin.site.register(Acomplishment)
admin.site.register(Skill)
admin.site.register(Projects)
admin.site.register(UserProfile)
admin.site.register(Certificate)
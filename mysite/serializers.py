from rest_framework import serializers
from .models import Experience
from .models import Acomplishment
from .models import Skill
from .models import Projects


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model= Experience
        fields = ['id', 'start_date','end_date','workplace_name','jobtitle','person']

class AcomplishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acomplishment
        fields = ['id', 'description', 'experience']

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id','skill_name','person']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id','name','description','link','skills']


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from mysite.models import Experience, Acomplishment, Skill, Projects, Certificate
from mysite.serializers import ExperienceSerializer, AcomplishmentSerializer, SkillsSerializer, ProjectSerializer
from django.shortcuts import render
from django.views import generic


@api_view(['GET'])
def experience_list(request, format=None):
     if request.method == 'GET':

        person = Experience.objects.all()
        person_serializer = ExperienceSerializer(person, many=True)
        return Response(person_serializer.data)
     
@api_view(['GET'])
def acomplishment_list(request, format=None):
    if request.method == 'GET':

        person = Acomplishment.objects.all()
        acomplishment_serializer = AcomplishmentSerializer(person, many=True)
        return Response(acomplishment_serializer.data)

@api_view(['GET'])
def skills_list(request, format=None):
    if request.method == 'GET':

        person = Skill.objects.all()
        skills_serializer = SkillsSerializer(person, many=True)
        return Response( skills_serializer.data)   
    
@api_view(['GET'])
def project_list(request, format=None):
    if request.method == 'GET':

        person = Projects.objects.all()
        project_serializer = ProjectSerializer(person, many=True)
        return Response(project_serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def experience_detail(request, id, format=None):
    try:
       experience =  Experience.objects.get(pk=id)
    except Experience.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        Experience_serializer = ExperienceSerializer(experience)
        return Response(Experience_serializer.data, status=status.HTTP_200_OK)
    
    # elif request.method == 'PUT':
    #     Experience_serializer = ExperienceSerializer(experience)
    #     if Experience_serializer.is_valid():
    #         Experience_serializer.save()
    #         return Response(Experience_serializer.data,status=status.HTTP_201_CREATED)
    #     else :
    #         return Response(Experience_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # elif request.method == 'DELETE':
    #     experience.delete()
    # return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def acomplishment_detail(request, id, format=None):
    try:
       acomplishment =  Acomplishment.objects.get(pk=id)
    except Acomplishment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        Acomplishment_serializer = AcomplishmentSerializer(acomplishment)
        return Response(Acomplishment_serializer.data, status=status.HTTP_200_OK)
    
    # elif request.method == 'PUT':
    #     Acomplishment_serializer = AcomplishmentSerializer(acomplishment)
    #     if Acomplishment_serializer.is_valid():
    #         Acomplishment_serializer.save()
    #         return Response(Acomplishment_serializer.data,status=status.HTTP_201_CREATED)
    #     else :
    #         return Response(Acomplishment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # elif request.method == 'DELETE':
    #     acomplishment.delete()
    # return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def skills_detail(request, id, format=None):
    try:
       skills =  Skill.objects.get(pk=id)
    except Skill.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        Skills_serializer = SkillsSerializer(skills)
        return Response(Skills_serializer.data, status=status.HTTP_200_OK)
    
    # elif request.method == 'PUT':
    #     Skills_serializer = SkillsSerializer(skills)
    #     if Skills_serializer.is_valid():
    #         Skills_serializer.save()
    #         return Response(Skills_serializer.data,status=status.HTTP_201_CREATED)
    #     else :
    #         return Response(Skills_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # elif request.method == 'DELETE':
    #     skills.delete()
    # return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def project_list(request, id, format=None):
    try:
       project =  Projects.objects.get(pk=id)
    except Projects.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        Projects_serializer = ProjectSerializer(project)
        return Response(Projects_serializer.data, status=status.HTTP_200_OK)
    
    # elif request.method == 'PUT':
    #     Projects_serializer = ProjectSerializer(project)
    #     if Projects_serializer.is_valid():
    #         Projects_serializer.save()
    #         return Response(Projects_serializer.data,status=status.HTTP_201_CREATED)
    #     else :
    #         return Response(Projects_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # elif request.method == 'DELETE':
    #     project.delete()
    # return Response(status=status.HTTP_204_NO_CONTENT)

def home (request):
    return render(request, 'home.html')


class IndexView(generic.TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		# testimonials = Testimonial.objects.filter(is_active=True)
		# certificates = Certificate.objects.filter(is_active=True)
		experience = Experience.objects.filter()
		project = Projects.objects.filter()
		certificates = Certificate.objects.filter()
		
		context["experience"] = experience
		context["certificates"] = certificates
		# context["blogs"] = blogs
		context["projects"] = project
		return context


# class ContactView(generic.FormView):
# 	template_name = "contact.html"




class PortfolioView(generic.ListView):
	template_name = "portfolio.html"
	paginate_by = 10
	model = Projects
	slug_url_kwargs = 'slug'

	def get_queryset(self):
		return super().get_queryset().filter()



class PortfolioDetailView(generic.DetailView):
	template_name = "portfolio-detail.html"
	model = Projects

# class BlogView(generic.ListView):
# 	template_name = "blog.html"
# 	paginate_by = 10
	
# 	def get_queryset(self):
# 		return super().get_queryset().filter(is_active=True)


# class BlogDetailView(generic.DetailView):
# 	template_name = "blog-detail.html"

"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import mysite.views as views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import include, re_path
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('experience/',views.experience_list),
    path('acomplishment/', views.acomplishment_list),
    path('skills/',views.skills_list),
    path('projects/',views.project_list),
    path('experience/<int:id>',views.experience_detail),
    path('',views.IndexView.as_view(),name="home"),
    path('portfolio/',views.PortfolioView.as_view(),name="portfolios"),
    path('portfolio/<slug:slug>/',views.PortfolioDetailView.as_view(),name="portfolio"),
    # path('contact/',views.ContactView.as_view(),name="contact"),
    # path('blog/',views.BlogView.as_view(),name="blogs"),
    # path('blog/<slug:slug>',views.BlogDetailView.as_view(),name="blog"),
        re_path(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
    
]

urlpatterns=format_suffix_patterns(urlpatterns)
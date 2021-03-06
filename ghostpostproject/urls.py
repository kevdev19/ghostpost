"""ghostpostproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from ghostpostapp.views import index_view, boast_view, roast_view, up_vote_view, down_vote_view, create_post_view, sort_view

urlpatterns = [
    path('', index_view, name='homepage'),
    path('boasts/', boast_view, name='boasts'),
    path('roasts/', roast_view, name='roasts'),
    path('upvote/<int:upvote_id>/', up_vote_view, name='upvote'),
    path('downvote/<int:downvote_id>/', down_vote_view, name='downvote'),
    path('sorted/', sort_view, name='sorted'),
    path('createpost/', create_post_view, name='createpost'),
    path('admin/', admin.site.urls),
]

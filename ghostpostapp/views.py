from django.shortcuts import render
from ghostpostapp.models import RoastBoastModel


def index_view(request):
    posts = RoastBoastModel.objects.filter().order_by('submit_time')
    return render(request, 'index.html', {"posts": posts})

from django.shortcuts import render, HttpResponseRedirect, reverse
from ghostpostapp.models import RoastBoastModel
from .forms import NewPostForm


def index_view(request):
    posts = RoastBoastModel.objects.filter().order_by('submit_time')
    return render(request, 'index.html', {"posts": posts})


def create_post_view(request):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            RoastBoastModel.objects.create(
                content=data.get('content'),
                is_boast=data.get('is_boast')
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = NewPostForm()
    return render(request, 'create_post.html', {"form": form})


def boast_view(request):
    return render(request, 'boasts.html', {})


def roast_view(request):
    return render(request, 'roasts.html', {})


def up_vote_view(request):
    pass


def down_vote_view(request):
    pass


def sort_view(request):
    pass


def posts_view(request):
    pass

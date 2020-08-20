from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from ghostpostapp.models import RoastBoastModel
from .forms import NewPostForm


def index_view(request):
    posts = RoastBoastModel.objects.all().order_by('submit_time')
    up_vote_total = request.POST.get('up_vote')
    return render(request, 'index.html', {"posts": posts, "up_vote_total": up_vote_total})


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
    posts = RoastBoastModel.objects.filter(is_boast=True)
    return render(request, 'boasts.html', {"posts": posts})


def roast_view(request):
    posts = RoastBoastModel.objects.filter(is_boast=False)
    return render(request, 'roasts.html', {"posts": posts})


def up_vote_view(request, upvote_id):
    post = RoastBoastModel.objects.get(id=upvote_id)
    post.up_vote = post.up_vote + 1
    post.save()
    return redirect('/')


def down_vote_view(request, downvote_id):
    post = RoastBoastModel.objects.get(id=downvote_id)
    post.down_vote = post.down_vote - 1
    post.save()
    return redirect('/')


def sort_view(request):
    pass


def posts_view(request, post_id):
    pass

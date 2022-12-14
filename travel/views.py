from django.shortcuts import render, get_object_or_404
from .models import Comment, AttractionPost
from .forms import CommentForm


def comment_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post, 'comment_form': comment_form})

def index(request): 
    attractions = AttractionPost.objects.all()
    return render(request, 'travel/index.html', {'attractions': attractions})
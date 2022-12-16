from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify
from .models import Comment, AttractionPost
from .forms import CommentForm, AttractionPostForm
from rest_framework import generics
from taggit.models import Tag
from .serializers import AttractionPostSerializer


def comment_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(AttractionPost, slug=slug)
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


def tag_home(request):
    posts = AttractionPost.objects.order_by('-published')
    # Show most common tags
    common_tags = AttractionPost.tags.most_common()[:4]
    form = AttractionPostForm(request.POST)
    if form.is_valid():
        newpost = form.save(commit=False)
        newpost.slug = slugify(newpost.title)
        newpost.save()
        form.save_m2m()

    
    context = {
        'posts':posts,
        'common_tags':common_tags,
        'form':form,
    }
    return render(request,'index.html', context)


def tag_detail(request, slug):
    post = get_object_or_404(AttractionPost, slug=slug)
    return render(request, 'detail.html', {'post':post})


def tagged(request,slug):
    tag = get_object_or_404(Tag, slug=slug)
    # filter posts by tag name
    posts = AttractionPost.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'posts':posts,
    }
    return render(request, 'index.html', context)

def index(request): 
    attractions = AttractionPost.objects.all()
    return render(request, 'travel/index.html', {'attractions': attractions})


class AttractionPostView(generics.ListCreateAPIView):
    queryset = AttractionPost.objects.all()
    order_fields = ['created_at']
    serializer_class = AttractionPostSerializer


class AttractionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AttractionPost.objects.all()
    serializer_class = AttractionPostSerializer
    
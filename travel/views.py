from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import slugify
from .models import AttractionPost, Following, Favorite, Comment, Profile
from .forms import CommentForm, AttractionPostForm, FavoriteForm, ProfileForm
from django.contrib.auth.decorators import login_required
from taggit.models import Tag
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied







@login_required
def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        user = request.user
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect("index")
    else: 
        form = ProfileForm()
    return render(request, 'travel/profile_form.html', {'form': form})




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


def attractions_by_favorite(request):
     favorites=Favorite.objects.filter(user=request.user)
#.get is for one .filter is for many
#literally saying get the favorites for the specific user
     return render(request, 'travel/attractions_by_favorite.html', {"favorites":favorites} )


def attraction_details(request, pk):
    attraction = get_object_or_404(AttractionPost, pk=pk)
    comments = Comment.objects.filter(attraction=attraction)
    user = request.user
    
    if request.method == 'POST':
        
        form = FavoriteForm(data=request.POST)
        if form.is_valid():
            favorite = form.save(commit=False)
            favorite.attraction = attraction
            favorite.user = user
            favorite.save()
            return redirect(to='attraction_details', pk=pk)
    elif request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.attraction = attraction
            comment.save()
    else:
        form = FavoriteForm()
        attraction = AttractionPost.objects.get(pk=pk)
        
    return render(request, "travel/attraction_details.html", {"attraction": attraction, 'form': form, "comments":comments})     
    
def add_comment(request,pk):
    attraction = get_object_or_404(AttractionPost, pk=pk)
    comment = Comment.objects.filter(attraction=attraction)
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.attraction = attraction
            comment.save()
            return redirect(to='attraction_details', pk=pk)
    return render(request, "travel/add_comment.html", {"form":form, "attraction":attraction})

def add_attraction(request):
    if request.method == 'GET':
        form = AttractionPostForm()
    else:
        form = AttractionPostForm(data=request.POST)
        if form.is_valid():
            attraction = form.save(commit=False)
            attraction.user = request.user
            attraction.save()
            return redirect(to='index')

    return render(request, "travel/add_attraction.html", {"form":form})

def logout(request):
    return render(request,'accounts/login/')

def login(request):
    return render(request, 'accounts/login/')

def Following(request):
    queryset = Following.objects.all()

    def get_queryset(self):
        queryset = Following.objects.filter(current_user=self.request.user.id)
        return queryset

    def perform_create(self):
        Following.save(current_user=self.request.user)

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)

        except IntegrityError:
            error_data = {
                "error": "You are already following this profile."
            }
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)  

def Followee(request):
    queryset = AttractionPost.objects.all()

    def get_queryset(self):
        return AttractionPost.objects.filter(owner=self.kwargs['pk'])

@login_required
def attraction_delete(request, pk):
    attraction = get_object_or_404(AttractionPost, pk=pk)
    user = request.user
    if attraction.user != request.user:
            return redirect('index')
    if request.method == "POST":
        attraction.delete()
        return redirect('index')
    return render(request, 'travel/delete_attraction.html')


   
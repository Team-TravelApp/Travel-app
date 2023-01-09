from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import slugify
from .models import AttractionPost, Following, Favorite, Comment, Profile, CustomUser
from .forms import CommentForm, AttractionPostForm, FavoriteForm, ProfileForm
from taggit.models import Tag
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import HttpResponse
from django.views.generic import ListView




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



@login_required
def profile_detail(request, pk):
    user = CustomUser.objects.get(pk=pk)
    profile = get_object_or_404(Profile, user=user)
    attractions = AttractionPost.objects.filter(user=user)
    #posts = AttractionPost.objects.filter(tags=tag)
    context = {
        'profile': profile, 
        'user': user,
        'attractions': attractions,
        'pk': pk
    }
    return render(request, 'travel/profile_detail.html', context) 


@login_required
def ListFollowers(request, pk):
    profile = Profile.objects.get(pk=pk)
    followers = profile.followers.all()
    context = {
        'profile': profile,
        'followers': followers,
        }
    return render(request, 'travel/followers_list.html', context)


@login_required
def profile_edit(request, pk):
    user = CustomUser.objects.get(pk=pk)
    profile = get_object_or_404(Profile, user=user)
    
    if profile.user != request.user:
            return redirect('index')
    elif request.method == 'GET':
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=True)
            profile.save()
            return redirect('index')
    return render(request, "travel/profile_edit.html", {"form":form, "profile":profile})


@login_required
def profile_delete(request, pk):
    user = CustomUser.objects.get(pk=pk)
    profile = get_object_or_404(Profile, user=user)
    if profile.user != request.user:
            return redirect('index')
    if request.method == "POST":
        profile.delete()
        return redirect('index')
    return render(request, 'travel/profile_delete.html')


'''
def search_tags(request):
    if request.method == "POST": 
        searched = request.POST['searched']
        attraction = AttractionPost.objects.filter(user__contains='searched')
        filtered_posts = AttractionPost.objects.filter(Q(content__contains=searched) | Q(title__contains=searched))
        return render(request, 'travel/search_tags.html', {'searched': searched, 'attraction': attraction})
    else:
        return render(request, 'travel/search_tags.html', {})
'''

def search(request):
    query = request.GET.get('q')
    search = AttractionPost.objects.filter(Q(country__icontains=query) | Q(tags__icontains=query) | Q(title__icontains=query)| Q(continent__icontains=query))

    return render(request, 'travel/search.html', {'search': search})




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
    user = request.user
    form = AttractionPostForm()
    return render(request, 'travel/index.html', {'attractions': attractions, 'user': user, 'form': form})


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
            return redirect(to='attractions_by_favorite')
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

@login_required
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
        form = AttractionPostForm(request.POST, request.FILES)
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

@login_required
def attraction_edit(request, pk):
    attraction = AttractionPost.objects.get(pk=pk)
    user = request.user
    if attraction.user != request.user:
            return redirect('index')
    else:
        form = AttractionPostForm(request.POST, instance=attraction)
        if form.is_valid():
            attraction = form.save(commit=True)
            attraction.save()
            return redirect('index')
    return render(request, "travel/edit_attraction.html", {"form":form, "attraction":attraction})

def display_attraction_pic(request, pk):
    if request.method == 'GET':

        attraction_pic = AttractionPost.objects.get(pk=pk)
        return render(request, 'attraction_details.html', {'attraction_pic': attraction_pic})

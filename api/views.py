from .serializers import AttractionPostSerializer, CommentSerializer
from travel.models import AttractionPost, Comment, Following
from rest_framework.viewsets import ModelViewSet
from django.db.models import Q
from django.db.models import Count
from rest_framework.generics import ListCreateAPIView, get_object_or_404, ListAPIView
from rest_framework import generics, status
from rest_framework.decorators import api_view



class AttractionPostViewSet(ModelViewSet):
    #This is question models view set.
    queryset          = AttractionPost.objects.all()
    serializer_class  = AttractionPostSerializer

    def get_queryset(self):
        #This is how you create a search code pulled form drf docs.
        search_term = self.request.query_params.get("search")
        if search_term is not None:
            #Filtering attraction post objects for anything that has search term in description.
            results = AttractionPost.objects.filter(Q(description__icontains=self.request.query_params.get("search"))| Q(title__icontains=self.request.query_params.get("search")))

        else:
            results = AttractionPost.objects.annotate(
                #This allows total number of comments for each attraction post
                total_comments=Count('comments')
            )
        return results

    def perform_create(self, serializer):
        #This means that post will be saved to users account.
        serializer.save(user=self.request.user)      

    def perform_destroy(self, instance):
        #This means that only the user can delete their own post.
        if self.request.user  == instance.user:
            instance.delete()

    def perform_update(self,serializer):
        #This means that the update will only save if the user is the creator of the post.
        if self.request.user == serializer.instance.user:
            serializer.save()

class CommentListCreateView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        #This is how you create a search code pulled form drf docs.
        search_term = self.request.query_params.get("search")
        if search_term is not None:
            #Filtering comment objects for anything that has search term in title.
            results = Comment.objects.filter (Q(comment__icontains=self.request.query_params.get("search")))
            return results

        # this is where we are only getting the comments related to the attractionpost
        return Comment.objects.filter(attractionpost_id=self.kwargs["attractionpost_pk"])
    # This is where we are changing the perform / create function within this API view 
    def perform_create(self, serializer):
        # This is where we are defining what a comment is, also making sure the comment is saved to the right user and attraction
        # 
        attractionpost = get_object_or_404(AttractionPost, pk=self.kwargs["attractionpost_pk"])
        serializer.save(comment_owner=self.request.user, attractionpost=attractionpost)
        
class MyComments(ListAPIView):
    #This is the view for a user to show there own comments.
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)      

class FollowingListCreateView(generics.ListCreateAPIView):
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

class FolloweePostList(generics.ListAPIView):
    queryset = AttractionPost.objects.all()

    def get_queryset(self):
        return AttractionPost.objects.filter(owner=self.kwargs['pk'])



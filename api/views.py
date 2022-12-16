from .serializers import AttractionPostSerializer
from travel.models import AttractionPost
from rest_framework.viewsets import ModelViewSet
from django.db.models import Q
from django.db.models import Count


class AttractionPost(ModelViewSet):
    #This is the attraction post modelviewset
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
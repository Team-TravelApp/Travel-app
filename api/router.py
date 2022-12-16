from api import views as api_views
from rest_framework import routers

#This router gives me all the question endpoints 
# in command line in terminal i can see them when I type python manage.py show_urls.
router = routers.DefaultRouter()
router.register('attractionposts',api_views.AttractionPostViewSet)
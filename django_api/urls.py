from django.urls import include, path
from rest_framework import routers
from api_testing import views

router = routers.DefaultRouter()
router.register(r'profile', views.User_profilesViewSet)
router.register(r'projects', views.ProjectsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = router.urls

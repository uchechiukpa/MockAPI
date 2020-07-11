from django.urls import path, include
from rest_framework import routers
from .views import ExperinceView, UserView, ProfileLoginView

router = routers.DefaultRouter()

router.register('experience', ExperinceView)
router.register('user', UserView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/',ProfileLoginView.as_view()),


]

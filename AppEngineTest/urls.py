
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from polls.views import CandidatesViewSet

routes = routers.DefaultRouter()
routes.register('Candidates', CandidatesViewSet)


urlpatterns = [
    path('', include(routes.urls)),
    path('admin/', admin.site.urls),
]

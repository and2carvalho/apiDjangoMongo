from django.urls import path, include
from rest_framework import routers
from .views import NoticiaViewSet, visualizaNoticia, pesquisaNoticia

app_name = 'api'
router = routers.DefaultRouter()
router.register('noticia', NoticiaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>', include(router.urls)),
    path('noticia/detail', pesquisaNoticia, name='pesquisa-noticia'),
    path('noticia/detail/<int:pk>', visualizaNoticia, name='visualiza-noticia'),
]

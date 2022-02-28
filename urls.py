from django.urls import path
from .views import ShowsView, ShowsDetail,ShowsEdit
from . import views

# http://127.0.0.1:8000/shows/

app_name = 'shows'

urlpatterns = [
    path('', ShowsView.as_view(), name='index' ),
    path('allshows/', ShowsDetail.as_view(), name='listado' ),
    path('delete/<int:id>/ajax', views.delete_shows_api, name='eliminar_ajax' ),
    path('edit/shows/<int:id>', ShowsEdit.as_view() , name='editar_forms' ),
    path('<int:id>', views.vershow, name='detail_id' ),
  
    
    
]
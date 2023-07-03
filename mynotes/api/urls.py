from . import views
from django.urls import path
app_name='api'
urlpatterns = [
    path('',views.getRoute,name='getRoute'),
    path('notes/',views.getNotes,name='getNotes'),


    path('notes/create',views.createNote,name='createNote'),
    path('notes/<str:pk>/update',views.updateNote,name='updateNote'),
    path('notes/<str:pk>/delete',views.deleteNode,name='deleteNode'),
    
    
    
    path('notes/<str:pk>',views.getNote,name='getNote'),
]

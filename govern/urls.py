from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('state/', views.state, name='state'),
    path('state/<state_id>', views.role, name='role'),
    path('add_position', views.add_position, name='add_position'),
    path('add_role/<state_id>', views.add_role, name='add_role'),

]

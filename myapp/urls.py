from django.urls import path
from .views import entity_list, entity_profile, image_view, create_entity, delete_entity, main_page

urlpatterns = [
    path('', main_page, name='main_page'),
    path('entity/', entity_list, name='entity_list'),
    path('entity/<int:id>/', entity_profile, name='entity_profile'),
    path('entity/create/', create_entity, name='create_entity'),
    path('entity/<int:id>/delete/', delete_entity, name='delete_entity'),
    path('image/', image_view, name='image_view'),  
]

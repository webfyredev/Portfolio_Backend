from django.urls import path
from .import views
urlpatterns = [
    path('contact/', views.contact_message, name='contacts'),
    path('contact-list/', views.contactsList, name='Contact-List'),
    path('project-list/', views.projectList, name='Project-List'),
]

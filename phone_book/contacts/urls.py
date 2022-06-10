from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.ContactView.as_view()),
    # path('<int:pk>', views.ContactView.as_view())
    path('', views.get_all_contact, name="all_contact"),
    path('get/<int:pk>', views.get_one_contact, name="one_contact"),
    path('create', views.create_contact, name="create"),
    path('update/<int:pk>', views.update_contact, name="update"),
    path('delete/<int:pk>', views.delete_contact, name="delete"),
]
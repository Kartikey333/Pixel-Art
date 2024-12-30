from django.urls import path
from pixel import views

# urlspatterns = {
#     path('home/', )
# }

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("photo/<pk>/", views.viewPhoto, name="photo"),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("main_create/", views.main_create, name="main_create"),
    path("main_create/<pk>/", views.main_create, name="main_create_with_pk"),
    path('run_model/', views.run_model, name='run_model'),



]
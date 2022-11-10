from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ako',views.ako, name='ako'),
    path("intro", views.calc, name='intro'),
    path("<str:name>", views.introduce, name="introduce"),
    path("<str:date>", views.introduce, name="introduce")

]
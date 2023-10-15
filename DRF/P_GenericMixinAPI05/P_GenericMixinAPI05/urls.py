from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapilist/', views.StudentList.as_view()),
    path('studentapicreate/', views.StudentCreate.as_view()),
    path('studentapiretieve/<int:pk>', views.StudentRetrieve.as_view()),
    path('studentapiupdate/', views.StudentUpdate.as_view()),
    path('studentapidestroy/', views.StudentDestroy.as_view()),



]

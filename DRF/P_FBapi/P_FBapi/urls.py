
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fbapi/',views.hello_world ),
    path('studentapi/',views.student_api )
]

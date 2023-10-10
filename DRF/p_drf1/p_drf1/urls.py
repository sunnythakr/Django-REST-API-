from django.contrib import admin
from django.urls import path
from drf1_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/<int:pk>', views.student_List),
    path('stuinfo/', views.student_details),
]
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter


# Creating Router Object 
router = DefaultRouter()

# Register StudentViewSet with ROuter
# router.register('employeeapi', views.EmployeeModelViewSet, basename='employee')
router.register('employeeapi', views.EmployeeReadOnlyModelViewSet, basename='employee')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls',namespace='rest_framework')), #this would enabel the login in your api

]

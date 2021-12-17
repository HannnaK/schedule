from django.urls import path
from .views import technical_data, time_for_project, schedule, one_project

urlpatterns = [
    path('', technical_data),
    path('czas_projektu/', time_for_project),
    path('harmonogram_druku/', schedule),
    path('projekt/<int:id>', one_project, name='project')
]

from django.urls import path
from appOne import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('student/', views.student_list),
    path('student/<int:pk>/', views.student_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)
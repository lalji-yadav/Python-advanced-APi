from django.urls import path
from ajaxdemo import views
# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('abc/', views.getdata ),
    # path('tech/', views.TechList.as_view()),
    # path('tech/<int:pk>/', views.TechDetail.as_view()),
    # path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),
]
# urlpatterns = format_suffix_patterns(urlpatterns)

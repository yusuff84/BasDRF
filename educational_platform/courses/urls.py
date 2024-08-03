from django.urls import path
from .views import (
    CourseListCreate, CourseDetail, ModuleListCreate, ModuleDetail,
    UserProfileListCreate, UserProfileDetail, ProgressListCreate, ProgressDetail
)

urlpatterns = [
    path('courses/', CourseListCreate.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetail.as_view(), name='course-detail'),
    path('modules/', ModuleListCreate.as_view(), name='module-list-create'),
    path('modules/<int:pk>/', ModuleDetail.as_view(), name='module-detail'),
    path('user-profiles/', UserProfileListCreate.as_view(), name='user-profile-list-create'),
    path('user-profiles/<int:pk>/', UserProfileDetail.as_view(), name='user-profile-detail'),
    path('progress/', ProgressListCreate.as_view(), name='progress-list-create'),
    path('progress/<int:pk>/', ProgressDetail.as_view(), name='progress-detail'),
]

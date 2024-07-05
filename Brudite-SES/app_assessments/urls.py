from django.contrib import admin
from django.urls import path
from app_assessments import views as main_views  

urlpatterns = [
    
    path('create/', main_views.AssignmentCreate.as_view()),
    path('assign/', main_views.Assignmentassign.as_view()),
    path('detail/<int:pk>/', main_views.AssignmentDetail.as_view()),
    path('user_detail/<int:pk>/',main_views.usersAssignmentdetail.as_view()),
    path('complete/<int:pk>/',main_views.completedAssignmentdetail.as_view()),
    path('incomplete/<int:pk>/',main_views.InCompletedAssignmentdetail.as_view())
    
]
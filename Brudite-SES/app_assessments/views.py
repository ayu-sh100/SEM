from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from app_assessments.models import Assignment,AssignmentProgress
from app_assessments.serializers import AssignmentSerializer,AssignmentProgressSerializer,UserSerializer
from app_customuser.models import CustomUser
from app_customuser.serializers import UserSerializer

class AssignmentCreate(generics.CreateAPIView):
    data = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class Assignmentassign(generics.CreateAPIView):
    data = AssignmentProgress.objects.all()
    serializer_class = AssignmentProgressSerializer
    
    

class AssignmentDetail(APIView):
    def get(self, request, pk):
        try:
            assignment = Assignment.objects.get(pk=pk)
            assignment_progress = AssignmentProgress.objects.filter(assignment=assignment)          
            user_pks = assignment_progress.values_list('user', flat=True)        
            users = CustomUser.objects.filter(pk__in=user_pks)
            user = UserSerializer(users, many=True)
            ASSIGNMENT = AssignmentSerializer(assignment)

            data = {
                'assignment':ASSIGNMENT.data,
                'users':user.data
            }
            return Response(data)
        except Assignment.DoesNotExist:
            return Response({"error": "Assignment not found"}, status=status.HTTP_404_NOT_FOUND)
        
class usersAssignmentdetail(APIView):
    
    def get(self,request,pk):
        try:
            user=CustomUser.objects.get(pk=pk)
            Assignment_progress = AssignmentProgress.objects.filter(user=user)
            assignment_pks = Assignment_progress.values_list('assignment',flat=True)
            assignments = Assignment.objects.filter(pk__in=assignment_pks)
            assignment_serializer = AssignmentSerializer(assignments,many=True)
            user_serializer = UserSerializer(user)
            data={
                
                'user':user_serializer.data,
                "Assignments":assignment_serializer.data
            }
            return Response(data)
        except CustomUser.DoesNotExist:
            return Response({"error": "user not found"}, status=status.HTTP_404_NOT_FOUND)
        

class completedAssignmentdetail(APIView):
    
    def get(self,request,pk):
        try:
            user=CustomUser.objects.get(pk=pk)
            Assignment_progress = AssignmentProgress.objects.filter(user=user,is_complete=True)
            assignment_pks = Assignment_progress.values_list('assignment',flat=True)
            assignments = Assignment.objects.filter(pk__in=assignment_pks)
            assignment_serializer = AssignmentSerializer(assignments,many=True)
            user_serializer = UserSerializer(user)
            data={
                
                'user':user_serializer.data,
                "Completed_Assignments":assignment_serializer.data
            }
            return Response(data)
        except CustomUser.DoesNotExist:
            return Response({"error": "user not found"}, status=status.HTTP_404_NOT_FOUND)

class InCompletedAssignmentdetail(APIView):
    
    def get(self,request,pk):
        try:
            user=CustomUser.objects.get(pk=pk)
            Assignment_progress = AssignmentProgress.objects.filter(user=user,is_complete=False)
            assignment_pks = Assignment_progress.values_list('assignment',flat=True)
            assignments = Assignment.objects.filter(pk__in=assignment_pks)
            assignment_serializer = AssignmentSerializer(assignments,many=True)
            user_serializer = UserSerializer(user)
            data={
                
                'user':user_serializer.data,
                "Incomplete_Completed_Assignments":assignment_serializer.data
            }
            return Response(data)
        except CustomUser.DoesNotExist:
            return Response({"error": "user not found"}, status=status.HTTP_404_NOT_FOUND)        
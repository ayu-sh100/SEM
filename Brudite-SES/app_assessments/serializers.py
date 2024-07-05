from rest_framework import serializers
from app_assessments.models import Assignment,AssignmentProgress
from app_customuser.models import CustomUser
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'  



class AssignmentProgressSerializer(serializers.ModelSerializer):
    user_details = serializers.SerializerMethodField()
    # assignment_details = serializers.SerializerMethodField()
    
    class Meta:
        model = AssignmentProgress
        fields = ('id','assignment', 'user', 'is_complete', 'percent_progress', 'score', 'user_details')
   
    def get_user_details(self,obj):
        user = obj.user
        assignment = obj.assignment
        details = {
            'user': user.name,
            'assignment':assignment.Name,
            "summary":assignment.Summary,
            'email': user.email
        }
        print(details)
        # return details
                            # ready html page to send the email to user
        htmlfile = render_to_string("assignemail.html",details)

                # Set up the email message
        subject, from_email, to = f"""You Assined a Assignment {user.name}""", settings.EMAIL_HOST_USER, user.email
        text_content = "This is an important message."
        html_content = htmlfile
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        print("sending mail")
        msg.send()   
            
    # def get_assignment_details(self,obj):
    #     assignment = obj.assignment
    #     return{
    #         'name': assignment.Name,
    #         'summary': assignment.Summary,
    #     }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','first_name','email')
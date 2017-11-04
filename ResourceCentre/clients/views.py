from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from serializers import MemberSerializer
from models import Member
from core import response_messages as resp_msg

class MemberView(APIView):
    """
    Member CRUD operation
    """

    def get(self, request):
        """
        ---
        parameters:
            - name: username
              required: true
              paramType: query
        """
        try:
            member_obj = Member.objects.get(username=request.GET.get("username"))
            member_serializer = MemberSerializer(member_obj)
            return Response(member_serializer.data, status=status.HTTP_200_OK)
        except Member.DoesNotExist:
            return Response(resp_msg.MEMBER_DOES_NOT_EXIST, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(resp_msg.DATABASE_ERROR, status=status.HTTP_400_BAD_REQUEST)

    
    def put(self, request):
        """
        ---
        parameters:
            - name: username
              required: true
            - name: first_name
              required: true
            - name: last_name
              required: true
            - name: email
              required: true
        """
        try:
            member_data = request.data.copy()
            member_obj = Member.objects.get(username=request.data.get("username"))
            member_serializer = MemberSerializer(member_obj, data=member_data)
            if member_serializer.is_valid():
                member_serializer.save()
                return Response(member_serializer.data, status=status.HTTP_201_CREATED)
            return Response(member_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Member.DoesNotExist:
            return Response(resp_msg.MEMBER_DOES_NOT_EXIST, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(resp_msg.DATABASE_ERROR, status=status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        """
        ---
        parameters:
            - name: username
              required: true
            - name: first_name
              required: true
            - name: last_name
              required: true
            - name: email
              required: true
        """
        try:
            member_data = request.data.copy()
            member_serializer = MemberSerializer(data=member_data)
            if member_serializer.is_valid():
                member_serializer.save()
                return Response(member_serializer.data, status=status.HTTP_201_CREATED)
            return Response(member_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(resp_msg.DATABASE_ERROR, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request):
        """
        ---
        parameters:
            - name: username
              required: true
        """
        try:
            member_obj = Member.objects.get(username=request.data["username"])
            member_obj.delete()
            return Response(resp_msg.SUCCESSFULLY_REMOVED, status=status.HTTP_200_OK)
        except Member.DoesNotExist:
            return Response(resp_msg.MEMBER_DOES_NOT_EXIST, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(resp_msg.DATABASE_ERROR, status=status.HTTP_400_BAD_REQUEST)




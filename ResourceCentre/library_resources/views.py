from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from serializers import BookSerializer
from models import Book
from core import response_messages as resp_msg


class BookView(APIView):
    """
    Book CRUD operation
    """

    def get(self, request):
        """
        ---
        parameters:
            - name: id
              required: true
              paramType: query
        """
        try:
            book_obj = Book.objects.get(pk=request.GET.get("id"))
            book_serializer = BookSerializer(book_obj)
            return Response(book_serializer.data, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response(resp_msg.BOOK_DOES_NOT_EXIST, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(resp_msg.DATABASE_ERROR, status=status.HTTP_400_BAD_REQUEST)

    
    def put(self, request):
        """
        ---
        parameters:
            - name: id
              required: true
            - name: name
              required: true
            - name: count
              required: true
        """
        try:
            book_data = request.data.copy()
            book_obj = Book.objects.get(pk=request.data.get("id"))
            book_serializer = BookSerializer(book_obj, data=book_data)
            if book_serializer.is_valid():
                book_serializer.save()
                return Response(book_serializer.data, status=status.HTTP_201_CREATED)
            return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Book.DoesNotExist:
            return Response(resp_msg.BOOK_DOES_NOT_EXIST, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(resp_msg.DATABASE_ERROR, status=status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        """
        ---
        parameters:
            - name: name
              required: true
            - name: count
              required: true
        """
        try:
            book_data = request.data.copy()
            book_serializer = BookSerializer(data=book_data)
            if book_serializer.is_valid():
                book_serializer.save()
                return Response(book_serializer.data, status=status.HTTP_201_CREATED)
            return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request):
        """
        ---
        parameters:
            - name: id
              required: true
        """
        try:
            book_obj = Book.objects.get(pk=request.data["id"])
            book_obj.delete()
            return Response(resp_msg.SUCCESSFULLY_REMOVED, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response(resp_msg.BOOK_DOES_NOT_EXIST, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(resp_msg.DATABASE_ERROR, status=status.HTTP_400_BAD_REQUEST)
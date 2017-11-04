from django.db import transaction

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from models import BookIssueTracker, MemberBooksTaken
from clients.models import Member
from library_resources.models import Book
from core import response_messages as resp_msg
from helper import get_member_obj, get_book_obj, get_member_books_obj, get_book_issue_obj
from django.db import transaction

class ResoureBorrowView(APIView):
    """
     Borrow Post View
    """
    @transaction.atomic
    def post(self, request):
        """
        ---
        parameters:
            - name: username
              required: true
            - name: book_id
              required: true
        """
        current_save = transaction.savepoint()
        try:
            success, member, error_message = get_member_obj(request.data.get("username"))
            if not success:
                return Response(error_message, status=status.HTTP_200_OK)

            success, book, error_message = get_book_obj(request.data.get("book_id"))
            if not success:
                return Response(error_message, status=status.HTTP_200_OK)

            if book.count == 0:
                return Response(resp_msg.BOOK_DOES_NOT_EXIST, status=status.HTTP_200_OK)
            book.count = book.count - 1
            book.save()
            bookissue_obj, is_created = BookIssueTracker.objects.get_or_create(member_involved=member, book=book)
            if not is_created:
                bookissue_obj.quantity = bookissue_obj.quantity + 1
                bookissue_obj.save()
            else:
                member_books_obj, is_created = MemberBooksTaken.objects.get_or_create(member=member)
                member_books_obj.books.add(request.data.get("book_id"))
                member_books_obj.save()
            return Response(resp_msg.SUCCESSFULLY_CREATED, status=status.HTTP_201_CREATED)
        except Exception as e:
            transaction.savepoint_rollback(current_save)
            return Response(resp_msg.DATABASE_ERROR, status=status.HTTP_400_BAD_REQUEST)

class ResoureReturnView(APIView):
    """
    Return post view
    """
    @transaction.atomic
    def post(self, request):
        """
        ---
        parameters:
            - name: username
              required: true
            - name: book_id
              required: true
        """
        current_save = transaction.savepoint()
        try:
            success, book, error_message = get_book_obj(request.data.get("book_id"))
            if not success:
                return Response(error_message, status=status.HTTP_200_OK)
            
            success, member_books_obj, error_message = get_member_books_obj(request.data.get("username"))
            if not success:
                return Response(error_message, status=status.HTTP_200_OK)

            success, bookissue_obj, error_message = get_book_issue_obj(request.data.get("username"), book)
            if not success:
                return Response(error_message, status=status.HTTP_200_OK)
            
            book_issued_previously = book.books_issued.filter(pk=member_books_obj.id).exists() 
            if not book_issued_previously:
                return Response(resp_msg.BOOK_IS_NOT_BORROWED, status=status.HTTP_200_OK)

            book.count = book.count + 1
            book.save()

            if bookissue_obj.quantity > 0:
                bookissue_obj.quantity = bookissue_obj.quantity - 1
                bookissue_obj.save()

            if bookissue_obj.quantity == 0:
                bookissue_obj.delete()
                member_books_obj.books.remove(request.data.get("book_id"))
                member_books_obj.save()
            return Response(resp_msg.SUCCESSFULLY_CREATED, status=status.HTTP_201_CREATED)
        except Exception as e:
            transaction.savepoint_rollback(current_save)
            return Response(resp_msg.DATABASE_ERROR, status=status.HTTP_400_BAD_REQUEST)
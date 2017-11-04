from clients.models import Member
from library_resources.models import Book
from models import BookIssueTracker, MemberBooksTaken
from core import response_messages as resp_msg

def get_member_obj(username):
    if not username:
        return False, None, resp_msg.USERNAME_MISSING
    try:
        return True, Member.objects.get(username=username), None
    except Member.DoesNotExist:
        return False, None, resp_msg.MEMBER_DOES_NOT_EXIST
    except (ValueError,):
        return False, None, resp_msg.VALUE_ERROR
    except Exception as e:
        return False, None, e.message


def get_book_obj(id):
    if not id:
        return False, None, resp_msg.ID_MISSING
    try:
        return True, Book.objects.get(id=id), None
    except Book.DoesNotExist:
        return False, None, resp_msg.BOOK_DOES_NOT_EXIST
    except (ValueError,):
        return False, None, resp_msg.VALUE_ERROR
    except Exception as e:
        return False, None, e.message


def get_member_books_obj(username):
    if not username:
        return False, None, resp_msg.USERNAME_MISSING
    try:
        return True, MemberBooksTaken.objects.get(member__username=username), None
    except Book.DoesNotExist:
        return False, None, resp_msg.MEMBER_DOES_NOT_EXIST
    except (ValueError,):
        return False, None, resp_msg.VALUE_ERROR
    except Exception as e:
        return False, None, e.message


def get_book_issue_obj(username, book):
    if not username:
        return False, None, resp_msg.USERNAME_MISSING
    try:
        return True, BookIssueTracker.objects.get(member_involved__username=username, book=book), None
    except Book.DoesNotExist:
        return False, None, resp_msg.MEMBER_DOES_NOT_EXIST
    except (ValueError,):
        return False, None, resp_msg.VALUE_ERROR
    except Exception as e:
        return False, None, e.message
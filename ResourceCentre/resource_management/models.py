from __future__ import unicode_literals

from django.db import models
from clients.models import Member
from library_resources.models import Book


class BookIssueTracker(models.Model):
    member_involved = models.ForeignKey(Member, related_name='member_book')
    book = models.ForeignKey(Book, related_name="book_issued")
    quantity = models.IntegerField(default=1)

    unique_together = (member_involved, book)


class MemberBooksTaken(models.Model):
    member = models.ForeignKey(Member, related_name='current_member')
    books = models.ManyToManyField(Book, related_name="books_issued")

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import UserManager

from django.utils.translation import ugettext_lazy as _
from django.core import validators
from django.utils import timezone


class ResourceBaseModel(models.Model):
    """
    UserBaseModel is abstract base model that is used by other
    models to have general information to other models.
    
    :Note: This model is not created in the database.
    
    """
    # first name of the user.
    name = models.CharField(_('book_name'), max_length=30, blank=True)
    # when the entry was created.
    created = models.DateTimeField(auto_now_add=True)
    # when the entry was modified.
    modified = models.DateTimeField(auto_now=True)
    count = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Book(ResourceBaseModel):

    def __str__(self):
        return self.name

    
    
    
    
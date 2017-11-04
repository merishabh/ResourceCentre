from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import UserManager
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from django.utils import timezone

from library_resources.models import Book


class UserBaseModel(models.Model):
    """
    UserBaseModel is abstract base model that is used by other
    models to have general information to other models.
    
    :Note: This model is not created in the database.
    
    """
    username = models.CharField(
        _('username'),
        max_length=255,
        unique=True,
        help_text=_('Required. 255 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(
                r'^[\w.@+-]+$',
                _('Enter a valid username. This value may contain only '
                  'letters, numbers ' 'and @/./+/-/_ characters.')
            ),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    # first name of the user.
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    # last name of the user.
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    # email of the user.
    email = models.EmailField(_('email address'), unique=True, blank=True)
    # when the entry was created.
    created = models.DateTimeField(auto_now_add=True)
    # when the entry was modified.
    modified = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    class Meta:
        abstract = True


class Member(UserBaseModel):

    objects = UserManager()
    
    def __str__(self):
        return self.email
    


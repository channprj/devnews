# django
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _

UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    display_name = models.CharField(_('표시명'), max_length=30, blank=True)
    bio = models.TextField(_('소개'), max_length=1000, blank=True)
    karma = models.FloatField(_('카르마'), default=0.0)  # editable=False if necessary
    created_at = models.DateTimeField(_('추가일'), auto_now_add=True)
    updated_at = models.DateTimeField(_('수정일'), auto_now=True)

    class Meta:
        # verbose_name = _('Profile')
        # verbose_name_plural = _('Profiles')
        ordering = ['-created_at', '-updated_at', ]

    def __str__(self):
        return "%s (%s)" % (self.user, self.karma)

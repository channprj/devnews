# django
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

# third-party
from taggit.managers import TaggableManager


UserModel = get_user_model()


class Link(models.Model):
    user = models.ForeignKey(UserModel, null=True, on_delete=models.SET_NULL)
    url = models.URLField(null=False, max_length=1000)
    root_url = models.URLField(null=True, max_length=1000)
    title = models.CharField(max_length=200, null=False)
    content = models.TextField(null=True)
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # verbose_name = _('링크')
        # verbose_name_plural = _('링크 모음')
        ordering = ['-updated_at', '-created_at',]

    def __str__(self):
        return "%s - %s" % (self.user, self.title)


class Comment(models.Model):
    link = models.ForeignKey(Link, null=True, on_delete=models.SET_NULL)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(UserModel, null=True, on_delete=models.SET_NULL)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # verbose_name = _('댓글')
        # verbose_name_plural = _('댓글 모음')
        ordering = ['-updated_at', '-created_at',]

    def __str__(self):
        return "%s - %s" % (self.user, self.link.title)


class Vote(models.Model):
    VOTE_CHOICES = (
        (None, None),
        (True, 'Upvote'),
        (False, 'Downvote'),
    )

    link = models.ForeignKey(Link, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(UserModel, null=True, on_delete=models.SET_NULL)
    action = models.NullBooleanField(choices=VOTE_CHOICES, max_length=3, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # verbose_name = _('투표')
        # verbose_name_plural = _('투표 모음')
        ordering = ['-created_at',]

    def __str__(self):
        return "%s - %s" % (self.user, self.link.title)

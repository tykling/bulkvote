import uuid
from django.db import models
from django.core.urlresolvers import reverse


class Vote(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
    author = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.description)

    def get_absolute_url(self):
        return reverse('showvote', kwargs={'uuid': self.uuid})


class Item(models.Model):
    item = models.CharField(max_length=50)
    vote = models.ForeignKey('bulkvote.Vote', related_name='items')

    def __unicode__(self):
        return unicode(self.item)


class Choice(models.Model):
    choice = models.CharField(max_length=50)
    vote = models.ForeignKey('bulkvote.Vote', related_name='choices')

    def __unicode__(self):
        return unicode(self.choice)


class UserChoice(models.Model):
    choice = models.ForeignKey('bulkvote.Choice', related_name='userchoices')
    item = models.ForeignKey('bulkvote.Item', related_name='userchoices')

    def __unicode__(self):
        return unicode(self.item.item + ': ' + self.choice.choice)

from __future__ import unicode_literals

from django.db import models


class ImdbRatingModel(models.Model):
    """This class contain fields which require
        to store popular data"""
    popularity_99 = models.FloatField(blank=False)
    director = models.CharField(max_length=100,blank=False)
    genre = models.TextField(blank=False)
    imdb_score = models.FloatField(blank=False)
    name = models.CharField(max_length=100,blank=False)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class UserKpiDetail(models.Model):
    from django.utils import timezone
    userid = models.CharField(max_length=10,blank=True,null=True)
    contactno = models.CharField(max_length=10,blank=True)
    kpicount = models.IntegerField(blank=True)
    kpidate = models.DateField(default=timezone.now)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{0} - {1} - {2}".format(self.contactno,kpicount,kpidate)

from django.db import models
from postgres_composite_types import CompositeType


class Point(CompositeType):
    class Meta:
        db_type = 'example_point'

    x = models.IntegerField()
    y = models.IntegerField()


class ExampleModel(models.Model):
    name = models.CharField(max_length=100)
    coordinates = Point.Field()

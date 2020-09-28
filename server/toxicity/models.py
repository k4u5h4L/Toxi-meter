from django.db import models
from rest_framework.views import APIView
from .scrape import Scrape

# Create your models here.


class Tox(models.Model, APIView):
    route = "api route POST"  # models.CharField(max_length=200)
    # description = models.TextField()
    predictions = []
    comments = []
    links = []
    status = ""

    def get(self, request):
        print(request)

    def __str__(self):
        """A string representation of the model."""
        return self.route

from rest_framework import serializers
from .models import Tox


# class ToxSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = (
#             'id',
#             'title',
#             'big_array',
#         )
#         model = Tox

class ToxSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'route',
            'predictions',
            'comments',
            'links',
            'status'
        )
        model = Tox

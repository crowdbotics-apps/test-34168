from rest_framework import serializers
from title.models import REview


class REviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = REview
        fields = "__all__"

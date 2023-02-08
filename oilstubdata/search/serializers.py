from rest_framework import serializers


class SearchSerializer(serializers.Serializer):
    search_term = serializers.CharField(max_length=200)

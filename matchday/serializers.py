from rest_framework import serializers
from .models import Quote, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["first_name", "last_name"]


class QuoteSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Quote
        fields = ["quote", "author"]

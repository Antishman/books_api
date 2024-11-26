from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'published_year']

    def validate(self, data):
        if data['published_year'] < 0:
            raise serializers.ValidationError("Published year cannot be negative.")
        return data
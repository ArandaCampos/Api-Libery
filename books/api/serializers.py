from dataclasses import field
from rest_framework import serializers
from books.models import booksModel

class bookSerialize(serializers.ModelSerializer):
    class Meta:
        model = booksModel
        fields = '__all__'

from rest_framework import viewsets
from books.api.serializers import bookSerialize
from books.models import booksModel

class bookViewSets(viewsets.ModelViewSet):
    queryset = booksModel.objects.all()
    serializer_class = bookSerialize
    
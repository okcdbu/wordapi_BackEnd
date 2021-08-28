from django.shortcuts import render
from .models import Word
from rest_framework import viewsets
from .serializers import WordSerializer

class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        random = self.request.query_params.get('get_by_level','')
        if random:
            qs = qs.filter(grade=random).order_by('?')[:1]
        return qs
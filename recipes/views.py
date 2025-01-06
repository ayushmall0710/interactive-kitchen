from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class RecipeSuggestionViewSet(ViewSet):
    def list(self, request):
        return Response({'message': 'Recipe suggestions will be implemented here.'})

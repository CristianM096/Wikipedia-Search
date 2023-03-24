from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Query
from .serializers import QuerySerializer

class ReportListView(APIView):
    def get(self, request, *args, **kwargs):
        reports = Query.objects.all()[0:10]
        serializer = QuerySerializer(reports,many=True)
        return Response(serializer.data)

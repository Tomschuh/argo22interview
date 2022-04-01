from .models import QRDocument
from .serializers import QRDocumentUpdateSerializer
from .serializers import QRDocumentDetailSerializer
from rest_framework import generics
from rest_framework.response import Response

class QRDocumentUploadView(generics.CreateAPIView):
    queryset = QRDocument.objects.all()
    serializer_class = QRDocumentUpdateSerializer
    

class QRDocumentDetailView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    
    queryset = QRDocument.objects.all()
    serializer_class = QRDocumentDetailSerializer
    
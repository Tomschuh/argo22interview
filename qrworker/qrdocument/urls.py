from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.QRDocumentUploadView.as_view()),
    path('<int:pk>/', views.QRDocumentDetailView.as_view(), name='qrdocument-detail'),
]
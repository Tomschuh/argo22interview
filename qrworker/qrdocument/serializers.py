from rest_framework import serializers
from .models import QRDocument
import io
import base64 
from pyzbar import pyzbar
from PIL import Image
from datetime import datetime

class QRDocumentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model =  QRDocument
        url = serializers.SerializerMethodField('get_url')        
        fields = [
            'imageBase64',
            'url'
        ]
        
    def create(self, validated_data):
        validated_data['process_state'] = QRDocument.ProcessState.PENDING
        try:
            imgdata = base64.b64decode(validated_data['imageBase64'])
            image = Image.open(io.BytesIO(imgdata))
            qr_code = pyzbar.decode(image)[0]
            format = "%Y-%m-%d"
            date_string = qr_code.data.decode("utf-8")
            date = datetime.strptime(date_string, format)
            if date < datetime.now():
                validated_data['process_state'] = QRDocument.ProcessState.EXPIRED
            else:
                validated_data['process_state'] = QRDocument.ProcessState.VALID
        except:
            validated_data['process_state'] = QRDocument.ProcessState.FRAUD
        
        return QRDocument.objects.create(**validated_data)
        
    def get_url(self, obj):
        return f"/api/qrdocument/{obj.id}/"

class QRDocumentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRDocument
        fields = [
            'process_state',
        ]
    
        
        


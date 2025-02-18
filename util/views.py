from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from util.models import QrCheckEvent
from rest_framework import status
class Checkin(APIView):
    def post(self, request):
        data = request.data
        user_id = data.get('user_id', None)
        event_id = data.get('event_id', None)

        if not user_id or not event_id:
            return Response({"error": "Lỗi khi post lên"}, status=status.HTTP_400_BAD_REQUEST)

        qr_code = QrCheckEvent.objects.filter(event_id=event_id, user_id=user_id).first()

        if qr_code:
            qr_code.da_tham_gia = True
            qr_code.save()
            return Response({"message": "Check in thành công"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Không check in được vé sai"}, status=status.HTTP_404_NOT_FOUND)
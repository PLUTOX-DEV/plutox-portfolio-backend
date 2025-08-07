from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

# 🔹 POST Contact message
@api_view(['POST'])
def contact_view(request):
    name = request.data.get('name')
    email = request.data.get('email')
    message = request.data.get('message')

    if not name or not email or not message:
        return Response({'error': 'All fields are required.'}, status=status.HTTP_400_BAD_REQUEST)

    subject = f"New Contact Message from Portfolio {name}"
    body = f"From: {name} <{email}>\n\nMessage:\n{message}"

    try:
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_RECEIVER_EMAIL],  # Make sure this is set in settings.py
            fail_silently=False,
        )
        return Response({'success': 'Message sent successfully!'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
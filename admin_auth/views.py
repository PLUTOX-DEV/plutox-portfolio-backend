from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def admin_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        if username == 'admin' and password == 'plutox':
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'error': 'Invalid credentials'}, status=401)

    return JsonResponse({'error': 'Only POST allowed'}, status=405)

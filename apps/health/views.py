from django.db import connection
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def health(request):
    return Response({'status': 'ok', 'service': 'docmind'})


@api_view(['GET'])
def ready(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT 1')
            cursor.fetchone()
    except Exception as exc:
        return Response({'status': 'degraded', 'database': exc.__class__.__name__}, status=503)
    return Response({'status': 'ok', 'database': 'up'})
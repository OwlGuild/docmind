from django.urls import path, include
urlpatterns=[path('health/', include('apps.health.urls'))]

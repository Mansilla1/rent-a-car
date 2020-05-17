from django.urls import path

from apps.clients import views


app_name = 'clients'

urlpatterns = [
    path(
        'clients/',
        views.ClientList.as_view(),
        name='clients',
    ),
]

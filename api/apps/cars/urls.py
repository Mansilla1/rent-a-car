from django.urls import path

from apps.cars import views


app_name = 'cars'

urlpatterns = [
    path(
        'cars/',
        views.CarList.as_view(),
        name='cars',
    ),
]

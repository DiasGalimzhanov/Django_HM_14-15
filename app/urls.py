from django.urls import path
from .views import VDList, VDCreate

urlpatterns = [
    path('', VDList.as_view(), name='home'),
    path('create/', VDCreate.as_view(), name='create'),
]
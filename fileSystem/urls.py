from django.urls import path
from fileSystem.views import *

urlpatterns = [
    path(r'upload', SaveFile.as_view(), name='uploadsss'),
]
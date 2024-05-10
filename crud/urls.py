from django.urls import path
from .views import CRUDView

urlpatterns = [
    path('', CRUDView.as_view({"post":"post",
                               "get":"get",
                               "patch":"update",
                               "delete":"delete"}))
]

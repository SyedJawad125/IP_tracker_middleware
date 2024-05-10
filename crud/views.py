from rest_framework.viewsets import ModelViewSet
from .controllers import CRUDController

crud_controller = CRUDController()

class CRUDView(ModelViewSet):
    def post(self, request):
        return crud_controller.post(request)

    def get(self, request):
        return crud_controller.get(request)

    def update(self, request):
        return crud_controller.update(request)

    def delete(self, request):
        return crud_controller.delete(request)
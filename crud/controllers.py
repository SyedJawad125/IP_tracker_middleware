from utils.reusable import *
from .serializers import DataSerializer

class CRUDController:
    serializer_class = DataSerializer
    def post(self, request):
        try:
            serialized_data = self.serializer_class(data=request.data)
            if serialized_data.is_valid():
                response_data = serialized_data.save()
                return create_response(self.serializer_class(response_data).data, SUCCESSFUL, 200)
            else:
                return create_response({},get_first_error_message_from_serializer_errors(serialized_data.errors, UNSUCCESSFUL),400)
        except Exception as e:
            return create_response({'error':str(e)}, SOMETHING_WENT_WRONG, 500)

    def get(self, request):
        try:
            if "id" in request.query_params:
                data = self.serializer_class.Meta.model.objects.filter(id=request.query_params.get("id"))
                if not data:
                    return create_response({}, NOT_FOUND, 400)
            else:
                data = self.serializer_class.Meta.model.objects.all()
            serialized_data = self.serializer_class(data, many=True).data
            return create_response(serialized_data, SUCCESSFUL, 200)

        except Exception as e:
            return create_response({'error': str(e)}, SOMETHING_WENT_WRONG, 500)

    def update(self, request):
        try:
            if "id" in request.data:
                instance = self.serializer_class.Meta.model.objects.filter(id=request.data['id']).first()
                if instance:
                    serialized_data = self.serializer_class(instance, data=request.data, partial=True)
                    if serialized_data.is_valid():
                        response_data = serialized_data.save()
                        return create_response(self.serializer_class(response_data).data, SUCCESSFUL, 200)
                    else:
                        return create_response({}, get_first_error_message_from_serializer_errors(serialized_data.errors, UNSUCCESSFUL),400)
                else:
                    return create_response({}, NOT_FOUND, 404)
            else:
                return create_response({}, ID_NOT_PROVIDED, 400)

        except Exception as e:
            return create_response({'error': str(e)}, SOMETHING_WENT_WRONG, 500)

    def delete(self, request):
        try:
            if "id" in request.data:
                instance = self.serializer_class.Meta.model.objects.filter(id=request.data['id']).first()
                if instance:
                    instance.delete()
                    return create_response({}, SUCCESSFUL, 200)
                else:
                    return create_response({}, NOT_FOUND, 404)
            else:
                return create_response({}, ID_NOT_PROVIDED, 400)

        except Exception as e:
            return create_response({'error':str(e)}, UNSUCCESSFUL, 500)
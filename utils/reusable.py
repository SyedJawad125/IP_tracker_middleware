from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnList


def create_response(data, message, status_code):
    result = {
        "status_code": status_code,
        "message": message,
        "data": data
        }
    return Response(result, status=status_code)



def get_first_error_message_from_serializer_errors(serialized_errors, default_message=""):
    if not serialized_errors:
        return default_message
    try:

        serialized_error_dict = serialized_errors

        # ReturnList of serialized_errors when many=True on serializer
        if isinstance(serialized_errors, ReturnList):
            serialized_error_dict = serialized_errors[0]

        serialized_errors_keys = list(serialized_error_dict.keys())
        # getting first error message from serializer errors
        try:
            message = serialized_error_dict[serialized_errors_keys[0]][0].replace("This", serialized_errors_keys[0])
            return message
        except:
            return serialized_error_dict[serialized_errors_keys[0]][0]

    except Exception as e:
        # logger.error(f"Error parsing serializer errors:{e}")
        return default_message



# Response Messages

SOMETHING_WENT_WRONG = "Something went wrong"
SUCCESSFUL = "Successful"
UNSUCCESSFUL = "Unsuccessful"
ID_NOT_PROVIDED = "ID not provided"
NOT_FOUND = "Record not found"
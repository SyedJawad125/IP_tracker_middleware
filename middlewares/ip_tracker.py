
class LogUserDetails:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        user_agent = request.META.get('HTTP_USER_AGENT')
        user_api_address = request.META.get('REMOTE_ADDR')
        user_locale_address = request.META.get('LC_ADDRESS')

        print("User's IP address:", user_api_address)
        print("User's browser:", user_agent)
        print("User's Locale:",user_locale_address)
        print('Hellllow world')

        return response


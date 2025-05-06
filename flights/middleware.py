import random
import string

from rest_framework.response import Response

class PromoCodeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        is_new_user = request.COOKIES.get('new_user', 'true') == 'true'
        promo_code = self.generate_promo_code() if is_new_user else None

        response = self.get_response(request)

        if (
            promo_code
            and isinstance(response, Response)
            and isinstance(response.data, dict)
        ):
            response.data['promo_code'] = promo_code
            response._is_rendered = False
            response.render()
            response.set_cookie('new_user', 'false', max_age=30 * 24 * 60 * 60)

        return response

    def generate_promo_code(self, length=6):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

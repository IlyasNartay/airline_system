from rest_framework.response import Response
from rest_framework.decorators import api_view
import random
import string

def generate_promo_code(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

@api_view(['GET'])
def test_api(request):
    is_new_user = request.COOKIES.get('new_user', 'true') == 'true'
    promo_code = generate_promo_code() if is_new_user else None

    response_data = {"message": "API is working"}
    if promo_code:
        response_data["promo_code"] = promo_code

    response = Response(response_data)
    if promo_code:
        response.set_cookie('new_user', 'false', max_age=30 * 24 * 60 * 60)

    return response

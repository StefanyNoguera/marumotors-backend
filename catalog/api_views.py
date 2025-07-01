from rest_framework import generics
from .models import Car, Autopart
from .serializers import CarSerializer, AutopartSerializer
import stripe
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json


# Cars
class CarListView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDetailView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'id'

# Autoparts
class AutopartListView(generics.ListAPIView):
    queryset = Autopart.objects.all()
    serializer_class = AutopartSerializer

class AutopartDetailView(generics.RetrieveAPIView):
    queryset = Autopart.objects.all()
    serializer_class = AutopartSerializer
    lookup_field = 'id'

stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        items = data.get('items', [])

        line_items = []
        for item in items:
            line_items.append({
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item['name'],
                    },
                    'unit_amount': int(float(item['price']) * 100),
                },
                'quantity': item['quantity'],
            })

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=f"{settings.DOMAIN}/checkout-success",
            cancel_url=f"{settings.DOMAIN}/cart",
        )
        return JsonResponse({'url': session.url})

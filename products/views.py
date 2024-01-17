from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from django.http import JsonResponse
import json

class GetAllProduct(APIView):

    def get(self, request):
        person = Product.objects.all()
        print(person)
        serializer = ProductSerializer(person, many=True)
        print(serializer)
        # response
        return JsonResponse(serializer.data, safe=False)

class CreateProduct(APIView):
    def post(self, request):
        body = json.loads(request.body.decode('utf-8'))
        data = {
            'name': body.get('name','default'),
            'price': body.get('price','default'),
        }
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
class DeleteProduct(APIView):
    def delete(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)

        product.delete()
        return JsonResponse({'message': 'Product deleted successfully'}, status=204)
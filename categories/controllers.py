from rest_framework.views import APIView
from .models import Category
from .serializers import CategorySerializer
from django.http import JsonResponse

class GetAllCategory(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        # response
        return JsonResponse(serializer.data, safe=False)

class CreateCategory(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
class DeleteCategory(APIView):
    def delete(self, request, category_id):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return JsonResponse({'error': 'Category not found'}, status=404)

        category.delete()
        return JsonResponse({'message': 'Category deleted successfully'}, status=204)
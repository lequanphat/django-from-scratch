from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from django.http import JsonResponse

class GetAllUsers(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        # response
        return JsonResponse(serializer.data, safe=False)

class CreateUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
class DeleteUser(APIView):
    def delete(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

        user.delete()
        return JsonResponse({'message': 'User deleted successfully'}, status=204)
    

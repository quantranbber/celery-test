from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from store.celery_app import app
from store.serializers import StoreSerializer, UserSerializer
from store.models import Store, User


class ListCreateStoreView(ListCreateAPIView):
    model = Store
    serializer_class = StoreSerializer

    def get_queryset(self):
        return Store.objects.order_by('id')

    def create(self, request, *args, **kwargs):
        serializer = StoreSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new Car successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Car unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)


class ListCreateUserView(ListCreateAPIView):
    model = User
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            app.send_task('register', args=(request.data.get('store_id'), user.id))

            return JsonResponse({
                'message': 'register successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'register unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

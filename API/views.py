from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import User, Favourites
from .serializers import UserSerializer, UserRegistrationSerializer, FavouritesSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'users': '/user-list/',
        'users-create': '/user-create/',
        'users-update': '/user-update/<str:pk>/',
        'users-delete': '/user-delete/<str:pk>/',
        'user-favourites': '/user-favourites/',
        'user-favourites-add': '/user-favourites-add/',
        'user-favourites-delete': '/user-favourites-delete/',
    }
    return Response(api_urls)

@api_view(['GET'])
def userList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def userRegistration(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def userUpdate(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance = user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def userDelete(request,pk):
    user = User.objects.get(id=pk)
    user.delete()
    return Response('User deleted successfully')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userFavourites(request):
    user = request.user
    favourites = Favourites.objects.filter(user=user)
    serializer = FavouritesSerializer(favourites, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userFavouritesAdd(request):
    user = request.user
    serializer = FavouritesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userFavouritesDelete(request, pk):
    user = request.user
    favourite = Favourites.objects.get(id=pk)
    favourite.delete()
    return Response('Favourite deleted successfully')


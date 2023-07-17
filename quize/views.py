from rest_framework import generics
from .models import Quize
from .serializers import QuizeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(['POST'])
def quize_create(request):
    email = request.data.get('email', None)
    if email is not None and Quize.objects.filter(email=email).exists():
        return Response(
            {'error': 'Email already exists.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = QuizeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class QuizeListCreateView(generics.ListCreateAPIView):
    queryset = Quize.objects.all()
    serializer_class = QuizeSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        if email is not None and Quize.objects.filter(email=email).exists():
            return Response(
                {'error': 'Email already exists.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().create(request, *args, **kwargs)

class QuizeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quize.objects.all()
    serializer_class = QuizeSerializer

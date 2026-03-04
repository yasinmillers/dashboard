from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .models import Complaint
from .serializers import UserSerializer, ComplaintSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = get_user_model().objects.filter(email=email).first()
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({"access": str(refresh.access_token)})
        return Response({"detail": "Invalid credentials"}, status=401)

class ComplaintCreateView(generics.CreateAPIView):
    serializer_class = ComplaintSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ComplaintListView(generics.ListAPIView):
    serializer_class = ComplaintSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return Complaint.objects.all()
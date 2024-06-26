from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import *

from .serializers import *
from .permissions import IsStudent


class StudentCreateAPIView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentRegisterSerializer


class StudentRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsStudent, ]

    queryset = Student.objects.all()
    serializer_class = StudentDetailsSerializer

    def get_object(self):
        return self.request.user


class StudentUpdateAPIView(UpdateAPIView):
    permission_classes = [IsStudent, ]

    queryset = Student.objects.all()
    serializer_class = StudentUpdateSerializer

    def get_object(self):
        return self.request.user


class StudentDeleteAPIView(DestroyAPIView):
    permission_classes = [IsStudent, ]

    queryset = Student.objects.all()
    serializer_class = StudentDetailsSerializer

    def get_object(self):
        return self.request.user

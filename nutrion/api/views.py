from django.shortcuts import render


from nutriologist.models import Patients
from nutriologist.models import PatientStats

from .serializers import PatientSerializer
from .serializers import PatientStatsSerializers


from rest_framework import viewsets
from rest_framework import status


from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

class PatientCreateView(viewsets.ModelViewSet):

    serializer_class = PatientSerializer

    def get_queryset(self):

        return Patients.objects.filter(nutrioligist_id = self.request.user.id)

    def create(self, request):

        serializers = PatientSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save(nutrioligist=self.request.user)
            return Response(serializers.data, status=status.HTTP_201_CREATED)


class PatientStatsView(viewsets.ModelViewSet):
    serializer_class = PatientStatsSerializers

    def get_queryset(self):
        return PatientStats.objects.select_related('patient_name').filter(patient_name__nutrioligist_id = self.request.user.id)


    def create(self, request):
        serializers = PatientStatsSerializers(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status = status.HTTP_201_CREATED)

class PatientListStatsView(viewsets.ReadOnlyModelViewSet):

    serializer_class = PatientStatsSerializers

    def get_queryset(self, *args, **kwargs):
        queryset = PatientStats.objects.select_related('patient_name').filter(patient_name__nutrioligist_id = self.request.user.id)
        query_param = self.request.query_params.get("patient_name",)
        if query_param:
            queryset = PatientStats.objects.select_related('patient_name').filter(patient_name = query_param)

        return queryset

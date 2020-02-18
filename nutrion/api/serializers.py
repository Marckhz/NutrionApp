from nutriologist.models import Patients
from nutriologist.models import PatientStats

from rest_framework import serializers



class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'
        read_only_fields = ['nutrioligist']

        def create(self, validated_data):

            patient = Patients(
                firstname=validated_data['firstname'],
                lastname=validated_data['lastname'],
                cellphone=validated_data['cellphone'],
                email=validated_data['email'],
                sex=validated_data['sex'],
                age = validated_data['age'],
                nutrioligist =  self.request.user.id
            )
            patient.save()
            return patient


class PatientStatsSerializers(serializers.ModelSerializer):
    patient_name = serializers.StringRelatedField()
    class Meta:
        model = PatientStats
        fields =   ('patient_name', 'weight', 'foreams', 'hip', 'date')

        def create(self, validated_data):
            return PatientStats.objects.create(**validated_data)

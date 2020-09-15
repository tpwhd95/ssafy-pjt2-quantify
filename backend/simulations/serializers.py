from rest_framework import serializers
from simulations.models import SimulationBreakdown,Simulation
from . import models
class SimulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Simulation
        fields = '__all__'
        # read_only_fields = 'id'
    # def create(self, validated_data):
    #     """
    #     검증한 데이터로 새 `Snippet` 인스턴스를 생성하여 리턴합니다.
    #     """
    #     return Simulation.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     검증한 데이터로 기존 `Snippet` 인스턴스를 업데이트한 후 리턴합니다.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance
        
class SimulationBreakdownSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SimulationBreakdown
        fields = '__all__'
        # read_only_fields = 'id'
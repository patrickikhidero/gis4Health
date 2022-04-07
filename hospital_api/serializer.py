from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers

from .models import  SubCounties,HealthFacilities

class SubCountiesSerializer(GeoFeatureModelSerializer):

	class Meta:
		model = SubCounties
		fields = '__all__'
		geo_field = 'geom'

    
class HealthFacilitiesSerializer(GeoFeatureModelSerializer):
    	
	# distance = serializers.CharField()

	class Meta:
		model = HealthFacilities
		fields = '__all__'
		geo_field = 'geom'
		read_only_fields = ['distance']
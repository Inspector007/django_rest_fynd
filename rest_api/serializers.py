from rest_framework import serializers
from .models import ImdbRatingModel, UserKpiDetail

class ImdbRatingModelSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""
    class Meta:
        """Map this serializer to a model and their fields."""
        model = ImdbRatingModel
        fields = ('popularity_99','director','genre','imdb_score','name')

class UserKpiDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserKpiDetail
		fields = ('userid','contactno','kpicount','kpidate')

from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
	location = serializers.SlugRelatedField(
		read_only=True,
		slug_field='name'
	)

	class Meta:
		model = User
		fields = '__all__'

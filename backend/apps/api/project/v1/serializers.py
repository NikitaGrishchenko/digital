from rest_framework import serializers

from ..models import Project


class ProjectSerializer(serializers.ModelSerializer):
    """ Сериализатор проектов """

    class Meta:
        model = Project
        fields = "__all__"

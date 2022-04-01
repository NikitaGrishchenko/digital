from apps.api.project.models import Project
from apps.api.project.v1.serializers import ProjectSerializer
from rest_framework.generics import ListAPIView


class ProjectAPIList(ListAPIView):
    """
    Список проектов
    """

    serializer_class = ProjectSerializer
    queryset = Project.objects.filter(dont_show_the_project=False)

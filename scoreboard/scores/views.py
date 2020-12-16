from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Score, Game
from .permissions import ReadOnly
from .serializers import ScoreSerializer, GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (ReadOnly,)


class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action in ['update', 'partial_update', 'destroy']:
            permission_classes.append(IsAdminUser)
        return [permission() for permission in permission_classes]

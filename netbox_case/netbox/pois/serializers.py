from rest_framework import serializers
from .models import POI

class POISerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo POI (Point of Interest).

    Este serializer converte instâncias do modelo POI em representações JSON na listagem e 
    JSON em instâncias na criação.

    Decisões:
    - Usei o ModelSerializer pois ele facilita a criação de serializers baseados em tabelas,
      reduzindo a quantidade de código boilerplate necessário.
    - Usei uma tupla na declaração dos campos por questões de performance.
    - Declarei as variáveis manualmente seguindo o princípio de "exposição mínima controlada".
    """
    class Meta:
        model = POI
        fields = (
            'name',
            'description',
            'x',
            'y'
        )


class POIProximitySerializer(serializers.Serializer):
    """
    Serializer para calcular a proximidade de um ponto de interesse.

    Este serializer recebe coordenadas (x, y) e uma distância máxima para calcular a proximidade
    de pontos de interesse.

    Campos:
    - x: Coordenada X do ponto de interesse.
    - y: Coordenada Y do ponto de interesse.
    - max_distance: Distância máxima para considerar a proximidade.

    Decisões:
    - Usei aqui um serializer simples já que são dados que serão usados para o cálculo e nao para
     serializar o modelo.
    - Todos os campos são obrigatórios para garantir que a proximidade seja calculada corretamente.
    """
    x = serializers.IntegerField(required=True)
    y = serializers.IntegerField(required=True)
    max_distance = serializers.IntegerField(required=True)

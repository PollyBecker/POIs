from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import POI
from .serializers import POIProximitySerializer, POISerializer
from django.db.models import Q

class POIList(ModelViewSet):
    serializer_class = POISerializer

    def get_queryset(self):
        return POI.objects.all()
    
    def create(self, request, *args, **kwargs):
        """
        Cria um novo POI se a localização não estiver já cadastrada.
        
        Decisões:
        - Validação dos dados de entrada para garantir que todos os campos obrigatórios estão presentes e corretos.
        - Verificação se a localização já existe com exists que é super eficiente para evitar duplicidade.
        - Mensagem personalizada de erro para uma melhor experiência do usuário.
        """
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        x = serializer.validated_data["x"]
        y = serializer.validated_data["y"]
        name = serializer.validated_data["name"]
        description = serializer.validated_data["description"]
        if POI.objects.filter(x=x, y=y).exists():
            return Response({"message":"Ops! Localização já foi cadastrada na terra média!"}, status=400)
        poi = POI.objects.create(
            x=x,
            y=y,
            name=name,
            description=description
        )
        response_serializer = self.get_serializer(poi)
        return Response({"poi": response_serializer.data})
        

class POIProximity(ModelViewSet):
    serializer_class = POIProximitySerializer
    
    def get_queryset(self):
        return POI.objects.all()
     
    def post(self, request, *args, **kwargs):
        """
        Calcula a proximidade de POIs com base nas coordenadas fornecidas e na distância máxima.
        
        Decisões:
        - Validação dos dados de entrada para garantir que todos os campos obrigatórios estão presentes e corretos.
        - Uso de filtros de intervalo para encontrar POIs dentro do range de distância escolhido.
        - Como o model é um Inteiro Positivo não preciso me preocupar com valores negativos no range ;)
        """
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        x_ref = serializer.validated_data['x']
        y_ref = serializer.validated_data['y']
        d_max = serializer.validated_data['max_distance']
        pois = POI.objects.filter(
            x__range=(x_ref - d_max, x_ref + d_max),
            y__range=(y_ref - d_max, y_ref + d_max)
        )
        return Response(POISerializer(pois, many=True).data)

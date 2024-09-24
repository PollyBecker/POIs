from django.urls import path
from .views import POIList, POIProximity

urlpatterns = [
    path('', POIList.as_view({'get':'list','post':'create'}), name='poi-list'),
    path('proximidade/', POIProximity.as_view({'get':'retrieve', 'post':'post'}), name='poi-proximity'),
]

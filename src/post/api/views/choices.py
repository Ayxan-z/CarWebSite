from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from post.api.serializers.choices import *
from rest_framework import status


class ChoicesAutoModelsView(ListAPIView):
    serializer_class = ChoicesModelSerializer

    def get_queryset(self):
        if q_brand := self.request.GET.get('brand'):
            try:
                return BrandModel.objects.get(id=q_brand).auto_models.all()
            except:
                return Response('Not Found', status=status.HTTP_404_NOT_FOUND)


class ChoicesListView(ListAPIView):
    def list(self, request, *args, **kwargs):
        return Response({
            'brand': ChoicesBrandSerializer(BrandModel.objects.all(), many=True).data,
            'category': ChoicesCategorySerializer(CategoryModel.objects.all(), many=True).data,
            'mileage_type': ChoicesMileageTypeSerializer(MileageTypeModel.objects.all(), many=True).data,
            'color': ChoicesColorSerializer(ColorModel.objects.all(), many=True).data,
            'price_type': ChoicesPriceTypeSerializer(PriceTypeModel.objects.all(), many=True).data,
            'prior_owners_count': ChoicesPriorOwnersCountSerializer(PriorOwnersCountModel.objects.all(), many=True).data,
            'seats_count': ChoicesSeatsCountSerializer(SeatsCountModel.objects.all(), many=True).data,
            'fuel_type': ChoicesFuelTypeSerializer(FuelTypeModel.objects.all(), many=True).data,
            'gear': ChoicesGearSerializer(GearModel.objects.all(), many=True).data,
            'transmission': ChoicesTransmissionSerializer(TransmissionModel.objects.all(), many=True).data,
            'year': ChoicesYearSerializer(YearsModel.objects.all(), many=True).data,
            'engine_volume': ChoicesEngineVolumeSerializer(EngineVolumeModel.objects.all(), many=True).data,
            'market': ChoicesMarketSerializer(MarketModel.objects.all(), many=True).data,
            'city': ChoicesCitySerializer(CityModel.objects.all(), many=True).data,
            'extra_boolean_fields': ChoicesExtraBooleanFieldsSerializer(ExtraBooleanFieldsModel.objects.all(), many=True).data,
        })
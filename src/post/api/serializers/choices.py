from rest_framework.serializers import ModelSerializer
from choices.models import *


class ChoicesBrandSerializer(ModelSerializer):
    class Meta:
        model = BrandModel
        fields = '__all__'

class ChoicesModelSerializer(ModelSerializer):
    class Meta:
        model = AutoModelsModel
        fields = '__all__'

class ChoicesCategorySerializer(ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'

class ChoicesMileageTypeSerializer(ModelSerializer):
    class Meta:
        model = MileageTypeModel
        fields = '__all__'

class ChoicesColorSerializer(ModelSerializer):
    class Meta:
        model = ColorModel
        fields = '__all__'

class ChoicesPriceTypeSerializer(ModelSerializer):
    class Meta:
        model = PriceTypeModel
        fields = '__all__'

class ChoicesPriorOwnersCountSerializer(ModelSerializer):
    class Meta:
        model = PriorOwnersCountModel
        fields = '__all__'

class ChoicesSeatsCountSerializer(ModelSerializer):
    class Meta:
        model = SeatsCountModel
        fields = '__all__'

class ChoicesFuelTypeSerializer(ModelSerializer):
    class Meta:
        model = FuelTypeModel
        fields = '__all__'

class ChoicesGearSerializer(ModelSerializer):
    class Meta:
        model = GearModel
        fields = '__all__'

class ChoicesTransmissionSerializer(ModelSerializer):
    class Meta:
        model = TransmissionModel
        fields = '__all__'

class ChoicesYearSerializer(ModelSerializer):
    class Meta:
        model = YearsModel
        fields = '__all__'

class ChoicesEngineVolumeSerializer(ModelSerializer):
    class Meta:
        model = EngineVolumeModel
        fields = '__all__'

class ChoicesMarketSerializer(ModelSerializer):
    class Meta:
        model = MarketModel
        fields = '__all__'

class ChoicesCitySerializer(ModelSerializer):
    class Meta:
        model = CityModel
        fields = '__all__'

class ChoicesExtraBooleanFieldsSerializer(ModelSerializer):
    class Meta:
        model = ExtraBooleanFieldsModel
        fields = '__all__'
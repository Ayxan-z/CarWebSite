from django.contrib import admin
from .models import *


admin.site.register((
    AutoModelsModel,
    BrandModel,
    CategoryModel,
    ColorModel,
    FuelTypeModel,
    GearModel,
    MileageTypeModel,
    PriceTypeModel,
    PriorOwnersCountModel,
    SeatsCountModel,
    TransmissionModel,
    YearsModel,
    EngineVolumeModel,
    MarketModel,
    CityModel,
    ExtraBooleanFieldsModel,
))
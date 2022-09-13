from django.db import models
from choices.models import *
from account.models import User
from django.core.validators import MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class PostModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='posts')
    brand = models.ForeignKey(BrandModel, on_delete=models.SET_NULL, null=True)
    auto_model = models.ForeignKey(AutoModelsModel, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True)
    mileage = models.PositiveIntegerField('Mileage', validators=(MaxValueValidator(10000000),))
    mileage_type = models.ForeignKey(MileageTypeModel, on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey(ColorModel, on_delete=models.SET_NULL, null=True)
    price = models.PositiveIntegerField('Price', validators=(MaxValueValidator(10000000),))
    price_type = models.ForeignKey(PriceTypeModel, on_delete=models.SET_NULL, null=True)
    prior_owners_count = models.ForeignKey(PriorOwnersCountModel, on_delete=models.SET_NULL, null=True, blank=True)
    crashed = models.BooleanField('Crashed', default=False)
    painted = models.BooleanField('Painted', default=False)
    seats_count = models.ForeignKey(SeatsCountModel, on_delete=models.SET_NULL, null=True)
    loan = models.BooleanField('Loan', default=False)
    barter = models.BooleanField('Barter', default=False)
    fuel_type = models.ForeignKey(FuelTypeModel, on_delete=models.SET_NULL, null=True)
    gear = models.ForeignKey(GearModel, on_delete=models.SET_NULL, null=True)
    transmission = models.ForeignKey(TransmissionModel, on_delete=models.SET_NULL, null=True)
    year = models.ForeignKey(YearsModel, on_delete=models.SET_NULL, null=True, blank=True)
    engine_volume = models.ForeignKey(EngineVolumeModel, on_delete=models.SET_NULL, null=True)
    engine_power = models.PositiveIntegerField('Engine Power', validators=(MaxValueValidator(10000),))
    market = models.ForeignKey(MarketModel, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField('Description', max_length=3169, null=True, blank=True)
    city = models.ForeignKey(CityModel, on_delete=models.SET_NULL, null=True)
    extra_boolean_fields = models.ManyToManyField(ExtraBooleanFieldsModel, blank=True)
    creation_date = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0, validators=(MaxValueValidator(10000000),))
    phone_number = PhoneNumberField()

    def __str__(self) -> str:
        return str(self.id)

class PostImageModel(models.Model):
    post = models.ForeignKey(PostModel, default=None, on_delete=models.CASCADE, related_name='post_images')
    image = models.ImageField(upload_to="post_images")

    def __str__(self):
        return str(self.id)
from rest_framework.generics import ListAPIView
from account.api.serializers import MyPostsSerializer
from post.api.paginations import AllPostListPagination
from rest_framework.filters import OrderingFilter
from post.models import PostModel
from rest_framework.exceptions import ValidationError
from django.db.models import Count


class PostListView(ListAPIView):
    serializer_class = MyPostsSerializer
    pagination_class = AllPostListPagination
    filter_backends = (OrderingFilter,)
    ordering_fields = ('mileage', 'year', 'price')

    def get_queryset(self):
        queryset = PostModel.objects.all()
        q_brand = self.request.GET.get('brand', None)
        q_model = self.request.GET.get('model', None)
        q_usage = self.request.GET.get('usage', None)
        if q_usage:
            if q_usage == 'new':
                q_max_mileage = 0
                q_min_mileage = None
            elif q_usage == 'used':
                q_min_mileage = 1
                q_max_mileage = None
            else: raise ValidationError({'Value Error': "'usage' can be 'new' or 'used'"})
        if q_usage is None:
            q_min_mileage = self.request.GET.get('min_mileage', None)
            q_max_mileage = self.request.GET.get('max_mileage', None)
        elif q_usage == 'used':
            q_max_mileage = self.request.GET.get('max_mileage', None)
        q_city = self.request.GET.get('city', None)
        q_min_price = self.request.GET.get('min_price', None)
        q_max_price = self.request.GET.get('max_price', None)
        q_price_type = self.request.GET.get('price_type', None)
        q_loan = self.request.GET.get('loan', None)
        q_barter = self.request.GET.get('barter', None)
        q_category = self.request.GET.get('category', None)
        q_min_year = self.request.GET.get('min_year', None)
        q_max_year = self.request.GET.get('max_year', None)
        q_color = self.request.GET.get('color', None)
        q_fuel_type = self.request.GET.get('fuel_type', None)
        q_gear = self.request.GET.get('gear', None)
        q_transmission = self.request.GET.get('transmission', None)
        q_min_engine_volume = self.request.GET.get('min_engine_volume', None)
        q_max_engine_volume = self.request.GET.get('max_engine_volume', None)
        q_min_engine_power = self.request.GET.get('min_engine_power', None)
        q_max_engine_power = self.request.GET.get('max_engine_power', None)
        q_prior_owners_count = self.request.GET.get('prior_owners_count', None)
        q_seats_count = self.request.GET.get('seats_count', None)
        q_crashed = self.request.GET.get('crashed', None)
        q_painted = self.request.GET.get('painted', None)
        q_market = self.request.GET.get('market', None)
        q_extra_fields = self.request.GET.get('extra_fields', None)

        try:
            if q_brand: queryset = queryset.filter(brand=q_brand)
            if q_model: queryset = queryset.filter(auto_model__in=q_model.split(','))
            if q_min_mileage is not None and q_max_mileage is not None:
                queryset = queryset.filter(mileage__range=(q_min_mileage, q_max_mileage))
            elif q_max_mileage is not None:
                queryset = queryset.filter(mileage__range=(0, q_max_mileage))
            elif q_min_mileage is not None:
                queryset = queryset.filter(mileage__gte=q_min_mileage)
            if q_city: queryset = queryset.filter(city__in=q_city.split(','))
            if q_min_price is not None and q_max_price is not None:
                queryset = queryset.filter(price__range=(q_min_price, q_max_price))
            elif q_max_price is not None:
                queryset = queryset.filter(price__range=(0, q_max_price))
            elif q_min_price is not None:
                queryset = queryset.filter(price__gte=q_min_price)
            if q_price_type: queryset = queryset.filter(price_type=q_price_type)
            if q_loan:
                if q_loan == 'true': queryset = queryset.filter(loan=True)
                else: raise ValidationError({'Value Error': "'loan' can be 'true'"})
            if q_barter:
                if q_barter == 'true': queryset = queryset.filter(barter=True)
                else: raise ValidationError({'Value Error': "'barter' can be 'true'"})
            if q_category: queryset = queryset.filter(category__in=q_category.split(','))
            if q_min_year is not None and q_max_year is not None:
                queryset = queryset.filter(year__year__range=(q_min_year, q_max_year))
            elif q_max_year is not None:
                queryset = queryset.filter(year__year__range=(0, q_max_year))
            elif q_min_year is not None:
                queryset = queryset.filter(year__year__gte=q_min_year)
            if q_color: queryset = queryset.filter(color__in=q_color.split(','))
            if q_fuel_type: queryset = queryset.filter(fuel_type__in=q_fuel_type.split(','))
            if q_gear: queryset = queryset.filter(gear__in=q_gear.split(','))
            if q_transmission: queryset = queryset.filter(transmission__in=q_transmission.split(','))
            if q_min_engine_volume is not None and q_max_engine_volume is not None:
                queryset = queryset.filter(engine_volume__volume__range=(q_min_engine_volume, q_max_engine_volume))
            elif q_max_engine_volume is not None:
                queryset = queryset.filter(engine_volume__volume__range=(0, q_max_engine_volume))
            elif q_min_engine_volume is not None:
                queryset = queryset.filter(engine_volume__volume__gte=q_min_engine_volume)
            if q_min_engine_power is not None and q_max_engine_power is not None:
                queryset = queryset.filter(engine_power__range=(q_min_engine_power, q_max_engine_power))
            elif q_max_engine_power is not None:
                queryset = queryset.filter(engine_power__range=(0, q_max_engine_power))
            elif q_min_engine_power is not None:
                queryset = queryset.filter(engine_power__gte=q_min_engine_power)
            if q_prior_owners_count: queryset = queryset.filter(prior_owners_count__in=q_prior_owners_count.split(','))
            if q_seats_count: queryset = queryset.filter(seats_count__in=q_seats_count.split(','))
            if q_crashed:
                if q_crashed == 'false': queryset = queryset.filter(crashed=False)
                else: raise ValidationError({'Value Error': "'crashed' can be 'false'"})
            if q_painted:
                if q_painted == 'false': queryset = queryset.filter(painted=False)
                else: raise ValidationError({'Value Error': "'painted' can be 'false'"})
            if q_market: queryset = queryset.filter(market__in=q_market.split(','))
            if q_extra_fields:
                q_extra_fields = q_extra_fields.split(',')
                queryset = PostModel.objects.filter(extra_boolean_fields__in=q_extra_fields)\
                    .annotate(num_extra_boolean_fields=Count('extra_boolean_fields'))\
                    .filter(num_extra_boolean_fields=len(q_extra_fields))

        except ValueError as e: raise ValidationError({'Value Error': e})

        return queryset.order_by('-id')
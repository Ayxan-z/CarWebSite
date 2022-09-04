from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from choices.models import *
from config.settings.base import BASE_DIR
from os.path import join
import json


def get_car_data() -> dict:
    options = Options()
    options.add_argument("--headless")
    driver = 'chromedriver_105'
    browser = Chrome(service=Service(executable_path=join(BASE_DIR, driver)), options=options)
    browser.get('https://turbo.az/autos/new')

    brand_options = browser.find_element(By.ID, 'auto_make_id')\
        .find_elements(By.TAG_NAME, 'option')[1:]

    brand_models = {}
    for o in brand_options:
        o.click()
        brand_models[o.text] = browser.find_element(By.ID, 'auto_model_id')\
            .text.split('\n')[1:]

    car_data = {
        'brand_models': brand_models,
        'category': browser.find_element(By.ID, 'auto_category_id').text.split('\n'),
        'mileage_type': [n.text for n in browser.find_elements(By.CSS_SELECTOR, '.auto_mileage_unit label')],
        'color': browser.find_element(By.ID, 'auto_color_id').text.split('\n'),
        'price_type': [n.text for n in browser.find_elements(By.CSS_SELECTOR, '.auto_currency label')],
        'prior_owners_count': browser.find_element(By.ID, 'auto_prior_owners_count').text.split('\n'),
        'seats_count': [s.text for s in\
            browser.find_elements(By.CLASS_NAME, 'new-product-i--inline')[1]\
            .find_elements(By.CLASS_NAME, 'collection_radio_buttons')],
        'fuel_type': browser.find_element(By.ID, 'auto_fuel_type_id').text.split('\n'),
        'gear': browser.find_element(By.ID, 'auto_gear_id').text.split('\n'),
        'transmission': browser.find_element(By.ID, 'auto_transmission_id').text.split('\n'),
        'year': browser.find_element(By.ID, 'auto_reg_year').text.split('\n'),
        'engine_volume': browser.find_element(By.ID, 'auto_engine_volume').text.split('\n'),
        'market': browser.find_element(By.ID, 'auto_market_id').text.split('\n'),
        'region': browser.find_element(By.ID, 'auto_region_id').text.split('\n'),
        'extra_fields': browser.find_element(By.CLASS_NAME, 'auto_extras').text.split('\n')[1:]
    }
    browser.quit()
    with open('car_data.json', 'w') as fp:
        json.dump(car_data, fp)

def create_objects():
    print('getting car data', end='\r')
    with open(join(BASE_DIR, 'car_data.json'), 'r') as fp:
        data = json.load(fp)
    print('creating brands and models', end='\r')
    for brand, models in data['brand_models'].items():
        brand_obj = BrandModel.objects.create(name=brand)
        for model in  models:
            AutoModelsModel.objects.create(name=model, brand=brand_obj)

    print('creating categories', end='\r')
    for c in data['category']: CategoryModel.objects.create(name=c)

    print('creating mileage_types', end='\r')
    for m in data['mileage_type']: MileageTypeModel.objects.create(name=m)

    print('creating colors', end='\r')
    for c in data['color']: ColorModel.objects.create(name=c)

    print('creating price_types', end='\r')
    for p in data['price_type']: PriceTypeModel.objects.create(name=p)

    print('creating prior_owners_counts', end='\r')
    for p in data['prior_owners_count']: PriorOwnersCountModel.objects.create(name=p)

    print('creating seats_conunts', end='\r')
    for s in data['seats_count']: SeatsCountModel.objects.create(count=s)

    print('creating fuel_types', end='\r')
    for f in data['fuel_type']: FuelTypeModel.objects.create(name=f)

    print('creating gears', end='\r')
    for g in data['gear']: GearModel.objects.create(name=g)

    print('creating transmissions', end='\r')
    for t in data['transmission']: TransmissionModel.objects.create(name=t)

    print('creating years', end='\r')
    for y in data['year']: YearsModel.objects.create(year=int(y))

    print('creating engine_volumes', end='\r')
    for e in data['engine_volume']: EngineVolumeModel.objects.create(volume=int(e))

    print('creating markets', end='\r')
    for m in data['market']: MarketModel.objects.create(name=m)

    print('creating cities', end='\r')
    for r in data['region']: CityModel.objects.create(name=r)

    print('creating extra_boolean_fields', end='\r')
    for e in data['extra_fields']: ExtraBooleanFieldsModel.objects.create(name=e)

    print('Object creation completed successfully')

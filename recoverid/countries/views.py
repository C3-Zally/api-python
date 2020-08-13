""" Countries views """

# Django REST Framework
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

# Models
from recoverid.countries.models import Country


@api_view()
@renderer_classes([JSONRenderer])
def list_countries(self):
    """ List countries """
    countries = Country.objects.all()[:196]
    data = []
    for country in countries:
        print(country.population)
        print(country.country_id)
        data.append({
            'id': country.country_id,
            'name': country.country_name,
            'alpha2Code': country.alpha2code,
            'alpha3Code': country.alpha3code,
            'capital': country.capital,
            'region': country.region,
            'subregion': country.subregion,
            'flag': country.flag,
            # 'population': country.population // problem here!,
        })
    return Response(data, status=200)

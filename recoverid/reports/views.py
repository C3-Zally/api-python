""" Reports views """

# Django REST Framework
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import generics

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


#import requests
from django.http import HttpResponse
import requests
import json
import datetime

# Django
from django.db.models import Sum, Max

# Models
from recoverid.reports.models import Report
from recoverid.countries.models import Country


class ReportsView(generics.ListAPIView):

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'code']

    @api_view(['GET'])
    @renderer_classes([JSONRenderer])
    def list_reports(self):
        """ List reports """
        data = []
        confirm = Report.objects.all().aggregate(Sum('infections'))
        confirmed = confirm['infections__sum']
        dead = Report.objects.all().aggregate(Sum('deaths'))
        deaths = dead['deaths__sum']
        recover = Report.objects.all().aggregate(Sum('recovered'))
        recovered = recover['recovered__sum']
        rep = Report.objects.last()
        data.append({
            'Last_updated': rep.date,
            'confirmed': confirmed,
            'active_cases': rep.active_cases,
            'deaths': deaths,
            'recovered': recovered,
        })
        return Response(data, status=200)

    @api_view(['GET'])
    @renderer_classes([JSONRenderer])
    def daily_report(self, year, month, day):
        """ Daily report """
        y = (
            str(year),
            str(month),
            str(day)
        )
        date_s = "-".join(y)
        date_object = datetime.datetime.strptime(date_s, '%Y-%m-%d').date()
        data = []
        filter_dataset = Report.objects.filter(date=date_object)
        confirm = filter_dataset.aggregate(Sum('infections'))
        confirmed = confirm['infections__sum']
        dead = filter_dataset.aggregate(Sum('deaths'))
        deaths = dead['deaths__sum']
        recover = filter_dataset.aggregate(Sum('recovered'))
        recovered = recover['recovered__sum']
        active_c = filter_dataset.aggregate(Sum('active_cases'))
        active_cases = active_c['active_cases__sum']
        data.append({
            'query_date': date_object,
            'confirmed': confirmed,
            'active_cases': active_cases,
            'deaths': deaths,
            'recovered': recovered,
        })
        return Response(data, status=200)

    @api_view(['GET'])
    @renderer_classes([JSONRenderer])
    def reports_countries(self):
        """ List reports all countries """
        all_countries = Country.objects.all()[:197]
        data = []
        for countries in all_countries:
            reports = Report.objects.filter(
                country_id_id=countries.country_id).order_by('-updated_at')[:1]
            data.append({
                "code": countries.alpha2code,
                "country": countries.country_name,
                "country_data": reports.values('updated_at','created_at','infections','deaths','recovered'),
                }
            )
        return Response(data, status=200)

    @api_view(['GET'])
    @renderer_classes([JSONRenderer])
    def report_country(self, code):
        """ List report with country code """
        country = Country.objects.filter(alpha2code=code)
        data = []
        for country_data in country:
            reports = Report.objects.filter(
                country_id_id=country_data.country_id).order_by('-updated_at')[:1]
            data.append({
                "code": country_data.alpha2code,
                "country": country_data.country_name,
                "country_data": reports.values('updated_at','created_at','infections','deaths','recovered'),
                }
            )
        return Response(data, status=200)


def uploadDataHistory():

    req = requests.get('')
    data = json.loads(resp.content)


def uploadDataDialy():

    idUrl = ''
    try:
        respId = requests.get('https://app.scrapinghub.com/api/jobs/list.json?project=466670&spider=spider_google&state=finished',
                              auth=('dd7c837f14c947c7a39ce7baae339bcd', ''))
        jsonDataId = json.loads(respId.content)
        
        for dictData in jsonDataId['jobs']:
            if dictData['state'] == 'finished':
                idUrl = dictData['id']
                break
    except:
        return '404'

    strUrl = f'https://storage.scrapinghub.com/items/{idUrl}?apikey=dd7c837f14c947c7a39ce7baae339bcd&format=json&saveas=data_11.json'
    try:
        resp = requests.get(strUrl)
        jsonData = json.loads(resp.content)
        datajson = jsonData[0]
        dateReport = datajson['header']['date']
        date_time = datetime.datetime.strptime(
            dateReport, "%Y-%m-%dT%H:%M:%SZ")
  
        countReportDate = Report.objects.filter(date=date_time).count()
  
    except:
        return '404'

    try:
        if countReportDate == 0:        
            for dataReport in datajson['content']:
                reportData = Report()
                pais_id = Country.objects.get(
                    alpha2code=dataReport['code'])  # .values('country_id')
                reportData.country_id = pais_id
                reportData.active_cases = dataReport['confirmed']
                reportData.date = date_time.date()
                reportData.deaths = dataReport['deaths']
                reportData.new_cases = dataReport['newCases']
                reportData.recovered = dataReport['recovered']
                reportData.save()

            return '200'
    except:
        return '500'


def uploadData(requests):
    # countReport = Report.objects.count()
    # if countReport == 0:
    #     uploadDataHistory
    respInsert = uploadDataDialy()
    return HttpResponse(status=respInsert)

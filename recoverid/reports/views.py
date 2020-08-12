""" Reports views """

# Django REST Framework
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from recoverid.reports.models import Report
#import requests
from recoverid.countries.models import Country
from django.http import HttpResponse
import requests
import json
import datetime

# Django
from django.db.models import Sum

# Models
from recoverid.reports.models import Report

@api_view()
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



def uploadDataHistory():

    req = requests.get('')
    data = json.loads(resp.content)



def uploadDataDialy():

    idUrl = ''
    try:
        respId = requests.get('https://app.scrapinghub.com/api/jobs/list.json?project=466670&spider=spider_google&state=finished',auth=('dd7c837f14c947c7a39ce7baae339bcd',''))
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
        date_time = datetime.datetime.strptime(dateReport,"%Y-%m-%dT%H:%M:%SZ")
        countReportDate = Report.objects.filter(date=date_time).count()
    except:
        return '404'
    
    try:
        if countReportDate == 0 :
            for dataReport in datajson['content']:
                reportData = Report()
                pais_id = Country.objects.get(alpha2code=dataReport['code']) #.values('country_id')
                reportData.country_id = pais_id
                reportData.active_cases = dataReport['confirmed']
                reportData.date = date_time.date()
                reportData.deaths = dataReport['deaths']
                reportData.new_cases = dataReport['newCases']
                reportData.recovered = dataReport['recovered']
                reportData.save()
                return '200'
    except :
        return '500'

    
def uploadData(requests):
    # countReport = Report.objects.count()
    # if countReport == 0:
    #     uploadDataHistory
    respInsert = uploadDataDialy()
    return HttpResponse(status=respInsert)



from django.shortcuts import render
from ..config import initilizationData
from tethys_sdk.permissions import login_required
from django.contrib.auth.models import User

def getContextData():
    context = {
        'CountryName':initilizationData['country'],
        'navLogoImage':initilizationData['navLogoImage'],
        'defaultView':initilizationData['defaultView'],
        'TethysAppName':initilizationData['TethysAppName'],
        'AdminLevel':initilizationData['AdminLevel'],
        'regionOrCountryId':initilizationData['regionOrCountryId'],
        'TethysAPIAppName':initilizationData['TethysAPIAppName'],
        'DefaultPlotInfo':initilizationData['DefaultPlotInfo'],
        'MaskWMS':initilizationData['MaskWMS'],
        'ForceMaxZoomOut':initilizationData['ForceMaxZoomOut'],
    }
    return context

authorizedUsernames=['aqwatchbt']

@login_required()
def Recent(request):
    """
    Controller for the app home page.
    """
    userName=request.user.username
    if userName in authorizedUsernames:
        context = getContextData()
        return render(request, 'aqwatchbt/recent_AirQualityWatch.html', context)
    else:
        context= {
            'requestPath':request.path
        }
        return render(request, 'aqwatchapi/logoutPage.html', context)


@login_required()
def Archive(request):
    """
    Controller for the app home page.
    """

    userName=request.user.username
    if userName in authorizedUsernames:
        context = getContextData()
        return render(request, 'aqwatchbt/archive_AirQualityWatch.html', context)
    else:
        context= {
            'requestPath':request.path
        }
        return render(request, 'aqwatchapi/logoutPage.html', context)


@login_required()
def Forecast(request):
    """
    Controller for the app home page.
    """

    userName=request.user.username
    if userName in authorizedUsernames:
        context = getContextData()
        return render(request, 'aqwatchbt/forecast_AirQualityWatch.html', context)
    else:
        context= {
            'requestPath':request.path
        }
        return render(request, 'aqwatchapi/logoutPage.html', context)





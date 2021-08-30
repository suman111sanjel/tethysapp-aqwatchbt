# from t
from tethysapp.aqwatchbt.app import Aqwatchbt

TethysAppName = Aqwatchbt.package

AllRegion={0:'HKH',
           1:'AFGHANISTAN',
           4:'BANGLADESH',
           7:'BHUTAN',
           8:'CHINA',
           3:'INDIA',
           6:'MYANMAR',
           5:'NEPAL',
           2:'PAKISTAN'}

initilizationData = {
    'country': 'Bhutan',
    'navLogoImage': '/static/' + TethysAppName + '/images/nologo.png',
    'defaultView': '''
    {
        center: ol.proj.transform([90.47482193197189, 27.493171939609666], 'EPSG:4326', 'EPSG:3857'),
        zoom: 8,
        extent: [6702855.884774126, 1769255.1930753174, 12194542.852403797, 4812621.833531793]
    }
    ''',
    'DefaultPlotInfo':'''
    {
        colorScheme: 'jet',
        BBOX: [88.5, 26.5, 92.5, 28.5],
        tickSpan: 1,
        Resolution: 600,
        width: 12,
        height: 9
    }
    ''',
    'TethysAppName': TethysAppName,
    'AdminLevel': 'l2Jumla',
    'regionOrCountryId': 7,
    'TethysAPIAppName':'aqwatchapi',
    'MaskWMS':'false',
    'ForceMaxZoomOut': 'false'
}

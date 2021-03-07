from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import PersistentStoreDatabaseSetting,PersistentStoreConnectionSetting

class Aqwatchbt(TethysAppBase):
    """
    Tethys app class for Aqwatchbt.
    """

    name = 'Air Quality Watch - Bhutan'
    index = 'aqwatchbt:recent'
    icon = 'aqwatchbt/images/icon.gif'
    package = 'aqwatchbt'
    root_url = 'aqwatchbt'
    color = '#f39c12'
    description = ''
    tags = 'Air Quality Watch'
    enable_feedback = False
    feedback_emails = []


    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='recent',
                url='aqwatchbt/recent',
                controller='aqwatchbt.controllers.home.Recent'
            ), UrlMap(
                name='archive',
                url='aqwatchbt/archive',
                controller='aqwatchbt.controllers.home.Archive'
            ), UrlMap(
                name='forecast',
                url='aqwatchbt/forecast',
                controller='aqwatchbt.controllers.home.Forecast'
            ),
            UrlMap(
                name='aeronetData',
                url='aqwatchbt/aeronetaodpm',
                controller='aqwatchbt.controllers.viewer.AeronetAODData',
            ), UrlMap(
                name='aeronetData',
                url='aqwatchbt/getGeoJSONofStations',
                controller='aqwatchbt.controllers.viewer.getGeoJSONofStations',
            ),
            UrlMap(
                name='getAllSatationID',
                url='aqwatchbt/getAllStationsID',
                controller='aqwatchbt.controllers.viewer.getIDofStations',
            ),
            UrlMap(
                name='getGeoJsonForOneSatation',
                url='aqwatchbt/getGeoJsonForOneSatation',
                controller='aqwatchbt.controllers.viewer.getGeoJsonForOneSatation',
            ),
            UrlMap(
                name='USembassyData',
                url='aqwatchbt/usembassypm',
                controller='aqwatchbt.controllers.viewer.USEmbassyPM',
            ),
            UrlMap(
                name='getData',
                url='aqwatchbt/getData',
                controller='aqwatchbt.controllers.viewer.GetData',
            ),
            UrlMap(
                name='GeojsonRegion',
                url='aqwatchbt/geojsonregion',
                controller='aqwatchbt.controllers.viewer.GeojsonRegion',
            ),
            UrlMap(
                name='AOIPolygon',
                url='aqwatchbt/aoipolygon',
                controller='aqwatchbt.controllers.viewer.AOIPolygon',
            ),
            UrlMap(
                name='GetMapPNG',
                url='aqwatchbt/getmapimage',
                controller='aqwatchbt.controllers.viewer.GetMapIMAGE',
            ), UrlMap(
                name='getImage',
                url='aqwatchbt/getimage',
                controller='aqwatchbt.controllers.viewer.getImage',
            ), UrlMap(
                name='create_GIF_Map_IMAGE',
                url='aqwatchbt/creategifmapimage',
                controller='aqwatchbt.controllers.viewer.Create_GIF_Map_IMAGE',
            ), UrlMap(
                name='timeseriesmodeldata',
                url='aqwatchbt/timeseriesmodeldata',
                controller='aqwatchbt.controllers.viewer.TimeSeriesModelSata',
            ), UrlMap(
                name='downloadImage',
                url='aqwatchbt/downloadImage',
                controller='aqwatchbt.controllers.viewer.downloadImage',
            ), UrlMap(
                name='downloadImage',
                url='aqwatchbt/slicedfromcatalog',
                controller='aqwatchbt.controllers.viewer.SlicedFromCatalog',
            ),
        )
        return url_maps


    # def persistent_store_settings(self):
    #     """
    #     Define Persistent Store Settings.
    #     """
    #     ps_settings = (
    #         PersistentStoreDatabaseSetting(
    #             name='airqualitywatch',
    #             description='Air Quality Watch',
    #             initializer='aqwatchbt.model.init_primary_db',
    #             required=True,
    #             spatial=True
    #         ),
    #         PersistentStoreConnectionSetting(
    #             name='airqualitywatch',
    #             description='Air Quality Watch',
    #             required=True
    #         ),
    #     )
    #     return ps_settings

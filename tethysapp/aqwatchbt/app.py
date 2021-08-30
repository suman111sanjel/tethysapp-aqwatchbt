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
        )
        return url_maps

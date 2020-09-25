
import logging
from youtubeSearch import YoutubeSearch
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction


logger = logging.getLogger(__name__)

icon_file='images/icon.png'


class YoutubeSeachExtension(Extension):
    def __init__(self):
        super(YoutubeSeachExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        query = event.get_argument() or str()

        if len(query.strip()) == 0:
            return RenderResultListAction([
                ExtensionResultItem(
                    icon=icon_file,
                    name='No input',
                    on_enter=HideWindowAction()
                )
            ])

        result_dict = YoutubeSearch.perform_search(query)
        logger.debug('Obtained result' + str(result_dict))

        
        if not result_dict:
             return RenderResultListAction([
                ExtensionResultItem(
                    icon=icon_file,
                    name='No results',
                    on_enter=HideWindowAction()
                )
            ])


        return RenderResultListAction([ ExtensionResultItem(
                icon=icon_file,
                name=title,
                description='',
                on_enter= OpenUrlAction("https://youtube.com" + url))
                for title, url in result_dict.items() ])

if __name__ == "__main__":
    YoutubeSeachExtension().run()
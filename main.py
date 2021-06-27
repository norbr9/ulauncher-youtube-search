import logging
import gi
gi.require_version('Gdk', '3.0')

from youtube_search import YoutubeSearch
from items import generate_search_items, no_input_item, no_results_item

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction


logger = logging.getLogger(__name__)


class YoutubeSearchExtension(Extension):
    def __init__(self):
        super(YoutubeSearchExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        query = event.get_argument() or str()

        if len(query.strip()) == 0:
            return RenderResultListAction(no_input_item())

        result_dict = YoutubeSearch.execute(query)
        logger.debug('Obtained result' + str(result_dict))

        if not result_dict:
            return RenderResultListAction(no_results_item())

        return RenderResultListAction(generate_search_items(result_dict, extension.preferences['description_template']))

if __name__ == "__main__":
    YoutubeSearchExtension().run()

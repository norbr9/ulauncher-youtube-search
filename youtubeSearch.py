import urllib.parse
import requests
import logging
import re

logger = logging.getLogger(__name__)

class YoutubeSearch():
    MAX_RESULTS = 10

    # If result execeds this value it will be treated as junk and removed
    RESULT_CHAR_LIMIT = 300

    BASE_URL = "https://youtube.com/results?search_query="

    REX = r"(\"title\":{\"runs\":\[{\"text\":\")(.*?)(\"}\],\"accessibility\":{\"accessibilityData\":{\"label\":\"(.*?))(\"}}},\"(descriptionSnippet|longBylineText))((?!\"webCommandMetadata).)*(.*?)(\"webCommandMetadata\":{\"url\":(\"\/watch\?v=([^\"](?!radio))*\"))"

    @staticmethod
    def perform_search(query):
        encoded_url = YoutubeSearch.BASE_URL + urllib.parse.quote(query)

        logger.debug('Performing request to ' + encoded_url)
        response = requests.get(encoded_url)

        result = re.findall(YoutubeSearch.REX, response.text)
        logger.debug('obtained regex response : ' + str(result))

        result_dict = {group[1].replace("\\",""):group[9].replace("\"","") for group in result if len(group[1]) < YoutubeSearch.RESULT_CHAR_LIMIT}

        return dict(list(result_dict.items())[:YoutubeSearch.MAX_RESULTS])
        
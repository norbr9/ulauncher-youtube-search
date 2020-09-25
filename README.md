# ulauncher-youtube-search
Extension for ulancher to perform youtube searchs. By default, it returns the first 10 results.

## Requirements

* [Ulauncher](https://github.com/Ulauncher/Ulauncher) 5.0+


## How it works
Youtube website needs to render html using some js scripts that would add delay to the query. To achive near real-time results, this extension performs regex matches on the js code itself.

The regex employed is:

```
(\"title\":{\"runs\":\[{\"text\":\")(.*?)(\"}\],\"accessibility\":{\"accessibilityData\":{\"label\":\"(.*?))(\"}}},\"(descriptionSnippet|longBylineText))((?!\"webCommandMetadata).)*(.*?)(\"webCommandMetadata\":{\"url\":(\"\/watch\?v=([^\"](?!radio))*\"))
```

This regex extracts multiple groups in which title and url are found. To find out how it really works I would recommend any tool such [regex101](https://regex101.com) and run the following example:

```
"title":{"runs":[{"text":"Dalex - Hola [Audio Oficial]"}],"accessibility":{"accessibilityData":{"label":"Dalex - Hola [Audio Oficial] de Dalex hace 1 año 3 minutos y 46 segundos 9.875.686 visualizaciones"}}},"descriptionSnippet":{"runs":[{"text":"Dalex - "},{"text":"Hola","bold":true},{"text":" [Audio Oficial] Sencillo producido por Dimelo Flow y Magnifico Escúchalo Climaxxx en Spotify: ..."}]},"longBylineText":{"runs":[{"text":"Dalex","navigationEndpoint":{"clickTrackingParams":"CKEBENwwGAgiEwjRn-_d-oPsAhVUu1EKHeLRDh8=","commandMetadata":{"webCommandMetadata":{"url":"/channel/UCeSCejKJS0W4LTptFuBYU0g","webPageType":"WEB_PAGE_TYPE_CHANNEL","rootVe":3611}},"browseEndpoint":{"browseId":"UCeSCejKJS0W4LTptFuBYU0g","canonicalBaseUrl":"/channel/UCeSCejKJS0W4LTptFuBYU0g"}}}]},"publishedTimeText":{"simpleText":"hace 1 año"},"lengthText":{"accessibility":{"accessibilityData":{"label":"3 minutos y 46 segundos"}},"simpleText":"3:46"},"viewCountText":{"simpleText":"9.875.686 visualizaciones"},"navigationEndpoint":{"clickTrackingParams":"CKEBENwwGAgiEwjRn-_d-oPsAhVUu1EKHeLRDh8yBnNlYXJjaFIEaG9sYZoBAxD0JA==","commandMetadata":{"webCommandMetadata":{"url":"/watch?v=kXYsaXKyQxo","webPageType":"WEB_PAGE_TYPE_WATCH","rootVe":3832}},"watchEndpoint":{"videoId":"kXYsaXKyQxo","params":"6gILbmxYcXAz
```

You will find out how the groups extract the desired information.


## Installation
Make sure you have installed pip3. 

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```
https://github.com/norbr9/ulauncher-youtube-search
```

## Usage
**yt** *searchword*: search searchword on youtube


## Links
* [Ulauncher Extensions](https://ext.ulauncher.io/)
* [Ulauncher 5.0 (Extension API v2.0.0) — Ulauncher 5.0.0 documentation](http://docs.ulauncher.io/en/latest/)


## TODO
It would be interesting to stop any music player that has already been opened. Moreover, to close any previous youtube browser tab and then open the new search. 
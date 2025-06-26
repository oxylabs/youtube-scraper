
<h2 align="center">
   YouTube Scraper
</h2>

[![Oxylabs promo code](https://raw.githubusercontent.com/oxylabs/product-integrations/refs/heads/master/Affiliate-Universal-1090x275.png)](https://oxylabs.io/pages/gitoxy?utm_source=877&utm_medium=affiliate&groupid=877&utm_content=youtube-scraper-github&transaction_id=102f49063ab94276ae8f116d224b67)


[![](https://dcbadge.vercel.app/api/server/eWsVUJrnG5)](https://discord.com/invite/Pds3gBmKMH)

With [<u>YouTube
Scraper</u>](https://oxylabs.io/products/scraper-api/web/youtube), you
can easily collect public YouTube data without blocks. Follow this guide
to see how to scrape YouTube using Oxylabs’ [<u>Scraper
API</u>](https://oxylabs.io/products/scraper-api).

## How it works

Simply, send a web request to our API and you’ll retrieve the HTML of
any public YouTube page you wish to scrape.

### Python code example

The below code requests and delivers the HTML content of [<u>this
Oxylabs video</u>](https://www.youtube.com/watch?v=SLSGtgKWzxg) on
YouTube:

```python
import requests
from pprint import pprint

# Structure payload.
payload = {
    'source': 'universal',
    'url': 'https://www.youtube.com/watch?v=SLSGtgKWzxg',
    'render': 'html'
}

# Get a response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('USERNAME', 'PASSWORD'),  # Your credentials go here
    json=payload
)

# Instead of response with job status and results URL, this will return the
# JSON response with results.
pprint(response.json())
```

See Oxylabs
[<u>documentation</u>](https://developers.oxylabs.io/scraper-apis/web-scraper-api)
for more details.

### Output sample

```json
{
    "results": [
        {
            "content":"<!doctype html>\n<html lang=\"en\">\n<head>
            ...
            </script></body>\n</html>\n",
            "created_at": "2023-05-18 12:33:40",
            "updated_at": "2023-05-18 12:33:55",
            "page": 1,
            "url": "https://www.youtube.com/watch?v=SLSGtgKWzxg",
            "job_id": "7064941110115745793",
            "status_code": 200
        }
    ]
}
```

Oxylabs’ YouTube Scraper API will ease your data gathering efforts and
you’ll be sure to gather YouTube data like channel information, video
details, titles, descriptions, playlists, and more. Reach out to us via
[<u>live chat</u>](https://oxylabs.io/) or
[<u>email</u>](mailto:support@oxylabs.io) in case you have any
questions.


Also, check this tutorial on [pypi](https://pypi.org/project/youtube-video-scraper-api/)

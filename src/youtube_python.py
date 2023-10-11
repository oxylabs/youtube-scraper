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

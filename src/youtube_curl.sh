curl --user USERNAME:PASSWORD \
'https://realtime.oxylabs.io/v1/queries' \
-H "Content-Type: application/json" \
-d '{"source": "universal", "url": "https://www.youtube.com/watch?v=SLSGtgKWzxg", "render": "html"}'

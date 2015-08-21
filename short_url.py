# Install the Python Requests library:
# `pip install requests`

import json,sys,requests

def send_request(urlToShort):
    # My API (POST https://www.googleapis.com/urlshortener/v1/url)

    try:
        r = requests.post(
            url="https://www.googleapis.com/urlshortener/v1/url",
            params = {
                "key":"AIzaSyBsTsPGbvWkniBir3KJFk3WXt5ODdCBlFg",
            },
            headers = {
                "Content-Type":"application/json",
            },
            data = json.dumps({
                "longUrl": urlToShort
            })
        )
        response = json.loads(r.content)
        return response['id']
    except requests.exceptions.RequestException as e:
        print('HTTP Request failed')

if len(sys.argv) != 2:
    print 'Some arguments are missing:'
    print ' 1. URL to short'
    sys.exit(-1)

urlToShort = sys.argv[1]
short = send_request(urlToShort)
print(short)
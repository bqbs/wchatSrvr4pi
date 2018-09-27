import urllib
import urllib.request
import json

# tuling robot
def tuling_robot(content):
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    req = urllib.request.Request(url % content.encode("utf-8"))
    req.add_header("apikey", "")
    resp = urllib.request.urlopen(req)
    content = resp.read()
    if content:
        print(content)
        content_json = json.loads(content)
        if content_json["text"]:
            content = content_json["text"]
    return content

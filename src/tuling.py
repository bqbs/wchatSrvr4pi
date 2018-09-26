# tuling robot
def tuling_robot(content):
    return content
    url = 'http://apis.baidu.com/turing/turing/turing?key=879a6cb3afb84dbf4fc84a1df2ab7319&info=%s&userid=eb2edb736'
    req = urllib.request.Request(url % content.encode("utf-8"))
    req.add_header("apikey", "d0c1245201bc618440af7c0bf4fa187c")
    resp = urllib.request.urlopen(req)
    content = resp.read()
    if content:
        print(content)
        content_json = json.loads(content)
        if content_json["text"]:
            content = content_json["text"]
    return content

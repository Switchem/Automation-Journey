import ssl
import re
from urllib.request import Request, urlopen




ssl_context = ssl._create_unverified_context() # <- disables SSL cert checks

url = "https://criticalfault.com/services/penetration-testing-services/"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"

}

req = Request(url, headers=headers)
page = urlopen(req, context=ssl_context)

html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)

title_index = html.find("<title>")
title_index

start_index = title_index + len("<title>")
start_index

end_index = title_index + len("</title>")
end_index

title = html[start_index:end_index]

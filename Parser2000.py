import re
import ssl
from urllib.request import Request, urlopen

ssl_context = ssl._create_unverified_context()

url = "https://criticalfault.com/services/penetration-testing-services/"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"

}
req = Request(url, headers=headers)
page = urlopen(req, context=ssl_context)


html = page.read().decode("utf-8")

pattern = "<tile.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags
print(title)
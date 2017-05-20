"""Kata5: Extract domain name from a URL, given a string of URL, 
return domain name in string.

#1 Best Practice
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

"""


def domain_name(url):
    """Extract domain name"""
  head = ["http://", "https://", "www."]
  if any(x in url for x in head):
    url = url.replace("http://","")
    url = url.replace("https://","")
    url = url.replace("www.","")
  return url.split(".")[0]
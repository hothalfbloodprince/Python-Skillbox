import requests
import re


def get_subheadings(url):
    response = requests.get(url)
    response.raise_for_status()
    html_text = response.text

    subheadings = re.findall(r'<h3.*?>(.*?)<\/h3>', html_text, re.DOTALL)
    subheadings = [re.sub(r'<.*?>', '', heading).strip() for heading in subheadings]

    return subheadings


url = "http://www.columbia.edu/~fdc/sample.html"
subheadings = get_subheadings(url)

print(subheadings)

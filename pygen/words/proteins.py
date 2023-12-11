
import requests

try:
    url = "https://python.sdv.univ-paris-diderot.fr/data-files/human-proteome.fasta"
    r = requests.get(url)
    print("HTML:\n", r.text)
except:
    print(
        "Invalid URL or some error occured while making the GET request to the specified URL"
    )
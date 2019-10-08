import requests

def scrape(args):
    base_url = 'https://sig.ifc.edu.br/sigaa/'
    sub_url = args['sub_url']

    # Request URL and Beautiful Parser
    r = requests.get(base_url + sub_url)
    return  r.text

if __name__ == "__main__":
    print(scrape())
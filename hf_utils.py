from bs4 import BeautifulSoup
import requests


def model_url_list():
    return [
        f"https://huggingface.co/models?p={i}&sort=downloads&search=dreambooth"
        for i in range(0, 5)
    ]


def data_scraping(url_list):
    model_list = []
    div_class = 'grid grid-cols-1 gap-5 2xl:grid-cols-2'
    for url in url_list:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        div = soup.find('div', {'class': div_class})
        model_list.extend(a['href'] for a in div.find_all('a', href=True))
    return model_list


def get_model_list():
    model_list = data_scraping(model_url_list())
    for i in range(len(model_list)):
        model_list[i] = model_list[i][1:]

    best_model_list = [
        "dreamlike-art/dreamlike-photoreal-2.0",
        "dreamlike-art/dreamlike-diffusion-1.0",
        "runwayml/stable-diffusion-v1-5",
        "CompVis/stable-diffusion-v1-4",
        "prompthero/openjourney",
    ]

    model_list = best_model_list + model_list
    return model_list

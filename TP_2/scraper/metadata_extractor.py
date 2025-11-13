from bs4 import BeautifulSoup

def extract_meta_tags(soup: BeautifulSoup) -> dict:
    #Extrae los meta tags relevantes de la página
    meta_tags = {}

    # Description
    description = soup.find("meta", attrs={"name": "description"})
    meta_tags["description"] = description["content"] if description else ""

    # Keywords
    keywords = soup.find("meta", attrs={"name": "keywords"})
    meta_tags["keywords"] = keywords["content"] if keywords else ""

    # Open Graph
    og_title = soup.find("meta", property="og:title")
    meta_tags["og:title"] = og_title["content"] if og_title else ""

    return meta_tags

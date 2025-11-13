from bs4 import BeautifulSoup

def extract_title(soup: BeautifulSoup) -> str:
    #Extrae el título de la página
    title_tag = soup.find("title")
    return title_tag.get_text() if title_tag else ""

def extract_links(soup: BeautifulSoup, base_url: str) -> list:
    #Extrae todos los enlaces de la página
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("http"):
            links.append(href)
        else:
            links.append(f"{base_url.rstrip('/')}/{href.lstrip('/')}")
    return links

def count_images(soup: BeautifulSoup) -> int:
    #Cuenta el número de imágenes en la página
    return len(soup.find_all("img"))

def count_headers(soup: BeautifulSoup) -> dict:
    #Cuenta los headers H1-H6 en la página
    return {f"h{i}": len(soup.find_all(f"h{i}")) for i in range(1, 7)}

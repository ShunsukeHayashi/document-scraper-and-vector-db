import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def extract_document_urls(root_url):
    print(f"Extracting document URLs from: {root_url}")
    try:
        response = requests.get(root_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {root_url}: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    document_urls = []

    for link in soup.find_all('a', href=True):
        full_url = urljoin(root_url, link['href'])
        document_urls.append(full_url)

    print(f"Found {len(document_urls)} URLs.")
    return document_urls

def scrape_documents(urls):
    documents = []
    for url in urls:
        print(f"Scraping document from: {url}")
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')
        body_text = soup.get_text(separator='\n', strip=True)
        documents.append(body_text)
        print(f"Successfully scraped document from: {url}")

    return documents

def save_to_text_file(documents, filename='doc_scraping/documents.txt'):
    os.makedirs(os.path.dirname(filename), exist_ok=True)  # ディレクトリが存在しない場合は作成
    print(f"Saving documents to {filename}")
    with open(filename, 'w', encoding='utf-8') as file:
        for document in documents:
            file.write(document + '\n\n')
    print(f"Documents saved to {filename}")

def save_url_tree(urls, filename='doc_scraping/url_tree.txt'):
    os.makedirs(os.path.dirname(filename), exist_ok=True)  # ディレクトリが存在しない場合は作成
    print(f"Saving URL tree to {filename}")
    with open(filename, 'w', encoding='utf-8') as file:
        for url in urls:
            parsed_url = urlparse(url)
            path_parts = parsed_url.path.strip('/').split('/')
            indent = '  ' * len(path_parts)
            file.write(f"{indent}{url}\n")
    print(f"URL tree saved to {filename}")

# 使用例
if __name__ == "__main__":
    root_url = input("スクレイピングするルートURLを入力してください: ")
    document_urls = extract_document_urls(root_url)
    documents = scrape_documents(document_urls)
    save_to_text_file(documents)
    save_url_tree(document_urls)
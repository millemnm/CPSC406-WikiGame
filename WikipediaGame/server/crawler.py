import time
import requests
from bs4 import BeautifulSoup
import re

from openai import OpenAI

client = OpenAI(api_key=)
import os
from scipy.spatial.distance import cosine

TIMEOUT = 10  # time limit in seconds for the search

def get_links(page_url):
    print(f"Fetching page: {page_url}")
    response = requests.get(page_url)
    print(f"Finished fetching page: {page_url}")
    soup = BeautifulSoup(response.text, 'html.parser')
    from urllib.parse import urljoin
    all_links = [urljoin(page_url, a['href']) for a in soup.find_all('a', href=True) if '#' not in a['href']]
    # print(f"All links found: {all_links}")
    links = [link for link in all_links if re.match(r'^https://en\.wikipedia\.org/wiki/[^:]*$', link) and '#' not in link]
    print(f"Found {len(links)} links on page: {page_url}")
    return links

def find_path(start_page, finish_page):
    queue = [(start_page, [start_page], 0)]
    discovered = set([start_page])
    logs = []
    first_links_texts = []

    # breadth first search
    start_time = time.time()
    while queue and (time.time() - start_time) < TIMEOUT:  
        (vertex, path, depth) = queue.pop(0)
        current_links = set(get_links(vertex)) - discovered

        # Fetch content for ranking if path is found
        if vertex == finish_page:
            finish_text = get_page_text(finish_page)
            for link in current_links:
                link_text = get_page_text(link)
                first_links_texts.append((link, link_text))
            
            # Compute similarities and sort
            topics = [text for _, text in first_links_texts]
            target_text = get_page_text(finish_page)
            sorted_links = rank_topics(target_text, topics, client)

            return path, sorted_links, time.time() - start_time, len(discovered)
        
        for next in current_links:
            discovered.add(next)
            queue.append((next, path + [next], depth + 1))

    raise TimeoutErrorWithLogs("Search exceeded time limit.", logs, time.time() - start_time, len(discovered))


def get_embedding(text, model="text-embedding-3-small"):
    try:
        response = client.embeddings.create(input=text,
        model=model)
        return response.data[0].embedding
    except Exception as e:
        print(f"An error occurred while getting embedding: {e}")
        return None

def rank_topics(base_text, topics):
    base_embedding = get_embedding(base_text)
    if base_embedding is None:
        return []

    topic_embeddings = [(topic, get_embedding(topic)) for topic in topics]
    topic_embeddings = [te for te in topic_embeddings if te[1] is not None]  # Filter out failed embeddings

    # Calculate similarity scores (lower cosine distance means higher similarity)
    similarities = [(topic, 1 - cosine(base_embedding, emb)) for topic, emb in topic_embeddings]

    # Sort topics based on similarity scores
    sorted_topics = sorted(similarities, key=lambda x: x[1], reverse=True)
    return [topic for topic, _ in sorted_topics]

def get_page_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find('div', {'id': 'mw-content-text'})
    if content:
        return content.text
    return ""  # Return an empty string if no content is found

class TimeoutErrorWithLogs(Exception):
    def __init__(self, message, logs, time, discovered):
        super().__init__(message)
        self.logs = logs
        self.time = time
        self.discovered = discovered
        


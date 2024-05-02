import time
import requests
from bs4 import BeautifulSoup
import re
from scipy.spatial.distance import cosine

from openai import OpenAI

client = OpenAI(api_key=)  # Fill in your API key
import os

TIMEOUT = 60  # time limit in seconds for the search

def get_embedding(text, model="text-embedding-3-small"):
    try:
        response = client.embeddings.create(input=text, model=model)
        return response.data[0].embedding
    except Exception as e:
        print(f"An error occurred while getting embedding: {e}")
        return None

def rank_topics(base_text, topics):
    base_embedding = get_embedding(base_text)
    if base_embedding is None:
        return []
    ranked_topics = []
    for topic in topics:
        topic_embedding = get_embedding(topic)
        if topic_embedding is not None:
            distance = cosine(base_embedding, topic_embedding)
            ranked_topics.append((topic, distance))
    ranked_topics.sort(key=lambda x: x[1])  # Sort topics by distance
    return [topic[0] for topic in ranked_topics]  # Return only topic names in ranked order

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
    discovered = set()
    logs = []

    # breadth first search
    start_time = time.time()
    elapsed_time = time.time() - start_time
    while queue and elapsed_time < TIMEOUT:  
        (vertex, path, depth) = queue.pop(0)
        for next in set(get_links(vertex)) - discovered:
            if next == finish_page:
                log = f"Found finish page: {next}"
                print(log)
                logs.append(log)
                logs.append(f"Search took {elapsed_time} seconds.")
                print(f"Search took {elapsed_time} seconds.")  # Add a print statement to log the elapsed time
                logs.append(f"Discovered pages: {len(discovered)}")
                return path + [next], logs, elapsed_time, len(discovered) # return with success
            else:
                log = f"Adding link to queue: {next} (depth {depth})"
                print(log)
                logs.append(log)
                discovered.add(next)
                queue.append((next, path + [next], depth + 1))
        elapsed_time = time.time() - start_time
    logs.append(f"Search took {elapsed_time} seconds.")
    print(f"Search took {elapsed_time} seconds.")  # Add a print statement to log the elapsed time
    logs.append(f"Discovered pages: {len(discovered)}")
    raise TimeoutErrorWithLogs("Search exceeded time limit.", logs, elapsed_time, len(discovered))

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

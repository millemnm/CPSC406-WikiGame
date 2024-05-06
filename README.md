# WikipediaGame

## Project Description
This project is an extension of a project started by [Alexander Kurz](https://github.com/alexhkurz) of the Wikipedia link searching game with the source code being https://github.com/alexhkurz/WikipediaGame.git.

The original project uses a breadth-first search (BFS) algorithm to retrieve links from the current Wikipedia page, storing them in a queue and subsequently navigating through these links to locate the target page. Although this algorithm is designed for finding the shortest path, it can still be improved.

Our improved implementation uses  **A\* OpenAI's embedding models** to find similar articles more efficiently by summarizing Wikipedia titles and article contents through AI. We also employed the **A\*Wikipedia API** instead of web scraping to speed up the retrieval of Wikipedia data.

## Presentation Link

https://docs.google.com/presentation/d/1tsm4XntdmyxGCJEWxKKwOspHBl3wSrhLYwKZ5r-2z8U/edit?usp=sharing

## Installation

(these instructions should work under GNU/Linux and macOS and WSL)

Prerequisites: Python

```
git clone https://github.com/millemnm/CPSC406-WikiGame.git
cd CPSC406-WikiGame/WikipediaGame/server
source setup.sh
```

PLEASE INSERT AN OPENAI SECRET KEY INTO crawler.py

Starting the server:

```
python server.py
```

Play the game on [`localhost:5001`](http://127.0.0.1:5001/) (this link will only work after you start the server on your machine (watch the console in case the port number changes to, e.g., `5002`)).

## Testing
1. Start the server for the original Wikipedia game and this one, ensuring that their ports are different
2. Visit each link
3. Leave both the URLs as default (the starting page should be Martin Wirsing, and the ending page should be David Hilbert)
4. Press "Find Path"
5. Wait until both processes are complete and compare

This version of the Wikipedia game should vastly reduce the number of pages visited to find the end page, at the cost of taking longer to complete the search. Note that the
search in both game versions includes random factors, such as how it finds similar links and how embeddings summarize Wikipedia articles. Results may vary but should follow the described trend.

### Example output

Original Wikipedia Game:

<img width="1024" alt="Screen_Shot_2024-05-02_at_7 07 42_PM" src="https://github.com/millemnm/CPSC406-WikiGame/assets/69368034/de3b2e06-99f8-4d35-85ae-df848ea1e5f7">

Our AI-Enhanced Wikipedia Game:

<img width="1025" alt="Screen Shot 2024-05-02 at 7 07 26 PM" src="https://github.com/millemnm/CPSC406-WikiGame/assets/69368034/c458c567-408a-4ffc-8b97-9606a169cb72">

## Limitations

- The UI works as expected only for Chrome-based browsers (Chrome, Brave, ...).
- Only works for Wikipedia pages.
- Implemented via HTTP requests (no web socket connection between client and server).
- Users are identified by IP address (no cookies or sessions).

## Parameters

- `RATELIMIT` in `server.py`.
- `TIMEOUT` in `crawler.py`.

## Further Ideas

- Improve the speed of the search via backtracking.
- Experiment with conversational models of OpenAI (ChatGPT 4.0).
- Implement other APIs to make fetching information and links faster.
 

## API Test

#### Test Python Script for Ranking Topics Based on Similarity Utilizing ChatGPT API

APITest.pi is a Python script that uses the OpenAI API to generate embeddings for a base text and a list of topics. It then ranks these topics based on their similarity to the base text.

#### Requirements

- Python 3.x
- openai library
- scipy library

#### Setup

1. **Install Python Packages**: Make sure you have Python installed on your system and then install the required packages using pip:

   ```bash
   pip install openai scipy
   ```

2. **API Key**: You need an API key from OpenAI. Please insert your OpenAI Secret Key into the program before running.


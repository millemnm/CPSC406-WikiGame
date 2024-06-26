# WikipediaGame

## Project Description
This project is an extension of a project started by [Alexander Kurz](https://github.com/alexhkurz) of the Wikipedia link searching game with the source code being https://github.com/alexhkurz/WikipediaGame.git.

The original project uses a breadth-first search (BFS) algorithm to retrieve links from the current Wikipedia page, storing them in a queue and subsequently navigating through these links to locate the target page. Although this algorithm is designed for finding the shortest path, it can still be improved.

Our improved implementation uses  **OpenAI's embedding models** to find similar articles more efficiently by summarizing Wikipedia titles and article contents through AI. We also employed the **Wikipedia API** instead of web scraping to speed up the retrieval of Wikipedia data.

## Presentation Link

[The presentation about our approach can be found here.](https://github.com/millemnm/CPSC406-WikiGame/blob/main/CPSC406%20-%20WikiGame%20AI.pdf) Please note the program was not fully implemented into the Wikipedia Game when the presentation was given, but APITest.py was complete.

## Installation

(these instructions should work under GNU/Linux and macOS and WSL)

Prerequisites: Python

```
git clone https://github.com/millemnm/CPSC406-WikiGame.git
cd CPSC406-WikiGame/WikipediaGame/server
source setup.sh
```

PLEASE INSERT AN OPENAI SECRET KEY INTO WikipediaGame/server/crawler.py, ON LINE 9

Starting the server:

```
python server.py
```

Play the game on [`localhost:5001`](http://127.0.0.1:5001/) (this link will only work after you start the server on your machine (watch the console in case the port number changes to, e.g., `5002`)).

## Testing
1. Start the server for the original Wikipedia game and this one, ensuring that their ports are different
2. Visit each game link
3. Insert your favorite two Wikipedia articles into Start Page URL and Finish Page URL
- We tested this with both the default inputs and Leonardo da Vinci and the Laurentian Library. Test results are shown below. 
5. Press "Find Path"
6. Wait until both processes are complete and compare

This version of the Wikipedia game should vastly reduce the number of pages visited to find the end page, at the cost of taking longer to complete the search. Note that the
search in both game versions includes random factors, such as how it finds similar links and how embeddings summarize Wikipedia articles. Results may vary but should follow the described trend.

### Test Results
Test results were benchmarked by comparing the number of pages visited between versions of the Wikipedia Game, underlined in red in the following screenshots.
#### TEST #1

Original Wikipedia Game:

<img width="980" alt="Screen Shot 2024-05-17 at 1 48 10 PM" src="https://github.com/millemnm/CPSC406-WikiGame/assets/69368034/b59959e7-afae-4aa6-8a25-f0aec13456ee">

Our AI-Enhanced Wikipedia Game:

<img width="986" alt="Screen Shot 2024-05-17 at 1 47 58 PM" src="https://github.com/millemnm/CPSC406-WikiGame/assets/69368034/3b8222ef-436e-40f0-bc18-9908990a76cb">

#### TEST #2
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

`APITest.py` is a Python script that uses the OpenAI API to generate embeddings for a base text and a list of topics. It then ranks these topics based on their similarity to the base text. This program was used to confirm the approach and create the functions we wanted to implement into The Wikipedia Game.

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


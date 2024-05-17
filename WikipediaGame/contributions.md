# Project Title
WikipediaGame
## Project Overview
This project is an extension of a project started by Alexander Kurz of the Wikipedia link searching game. It adds to the original project by implementing OpenAI's embedding models to find similar articles more efficiently by summarizing Wikipedia titles and article contents through AI. The Wikipedia API is also employed to avoid webscraping and speed up processing time.

## Team Members
- **Person 1:** Max Miller
- **Person 2:** Diego Lopez Ramos

## Contributions

### Person 1: Max
#### Role
Max came up with the idea of implementing AI to enhance the Wikipedia game. He experimented with OpenAI's generative AI APIs to determine how to best implement AI tools in the project, but ended up pivoting to OpenAI's Embedding model instead. His contributions include figuring out and creating test modules for the API, designing the architecture of the functions and their implementation, detailing his work in the readme, and formatting the slides.

#### Individual Contributions
- **Task 1:** Max started the project by paying for the basic embedding plan on OpenAI's website, giving him access to the API key that was used to deploy API calls in crawler.py. Then, he developed test modules in Python that demonstrated the implementation of the Embeddings model, encouraging modularity and demonstrability as design concepts. Once successful in implementing functionality in the API tests and proving their effectiveness, he demonstrated how it worked to Diego, giving him the insight necessary to use these functions in crawler.  
- **Task 2:** Once successful in implementing functionality in the API tests and proving their effectiveness, he demonstrated how it worked to Diego, giving him the insight necessary to use these functions in crawler. Thanks to the modular design, the functions he created were simple to implement into the project. It also simplified debugging, as the API tests were an isolated method that could be used with any inputs that were causing issues. 
- **Task 3:** Max also added his testing methods in the readme, making it easy to understand for users interested in the project and adding another layer of documentation. Additionally, he formatted the project presentation and created slides 1-5 and 9, allowing his ideas to be easily communicated and shared.

### Person 2: Diego
#### Role
Diego took up the project after the API was figured out. By adding the functions designed by Max into crawler.py, he figured out what the issues in implementations were and how to best address these issues. His contribution included implementing the API's functionality into the Wikipedia game, adding the Wikipedia API to speed up the processing time, creating the README, testing the project, and explaining the code and its roadblocks in the presentation.
#### Individual Contributions
- **Task 1:** Diego figured out that OpenAI's embeddings API struggled with such short inputs, such as the title of the Wikipedia articles. This was especially true when just given names of people and things without context as to what they were. It required longer texts to make meaningful connections, so he implemented the Wikipedia API in order to access summaries that could be used by the API in order to enhance the Wikipedia Game's effectiveness. He successfully implemented both APIs to complete the project.
- **Task 2:** Diego created and formatted the readme, including installation instructions and testing. Testing was crucial to demonstrating the benefit of using AI in the project. By providing screenshots of the test results and describing how testing was conducted, Diego showed that he completed his part of the project and succeeded in cutting down the number of pages visited to find the end page.
- **Task 3:** Diego designed slides 6-8 and discussed how the code works in the project presentation, giving an in-depth view of the backend mechanics. He explained how AI was implemented through API calls, and why it was necessary to add the Wikipedia API as well. He also discussed the roadblocks, and how he planned to continue forwards. Finally, he described what was next for the project and potential improvements that could be implemented in the future.
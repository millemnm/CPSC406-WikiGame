# Wikipedia Game Improvement Proposal

### Authors

Max Miller - maxmiller@chapman.edu
Diego Lopez Ramos - lopezramos@chapman.edu

### Proposal

To enhance the Wikipedia Game, we propose leveraging ChatGPT to create semantic understanding by reading the start and target articles. By analyzing the starting page links and the entirety of the final page, ChatGPT can identify the most similar links in the first node and create a prioritized list of which links to check first, guiding the program toward the target article more efficiently.

### Milestones:

1. (4/4) Get OpenAI API working
2. (4/11) ChatGPT should now be creating prioritized lists from the list of links.
3. (4/18) Modifiy Search Algorithm to utilize prioritization.
4. (4/25) Finishing touches/Test code

### Pseudo-code:

```python
function enhanced_BFS(start_article, target_article):
    initialize queue with start_article
    initialize visited set with start_article
    start_article_content = read_article_with_gpt(start_article)
    target_article_content = read_article_with_gpt(target_article)
    common_links = find_common_links(start_article_content, target_article_content)
  
    while queue is not empty:
        current_article = queue.pop()
        if current_article == target_article:
            return path to current_article
        for linked_article in get_linked_articles(current_article):
            if linked_article not in visited and linked_article in common_links:
                add linked_article to visited
                add (linked_article, path_to_current_article + linked_article) to queue
    return "No path found"

function read_article_with_gpt(article):
    // Use ChatGPT to read and understand the content of the article
    return ChatGPT.summarize_article(article)

function find_common_links(article1_content, article2_content):
    // Compare the links present in both articles and identify common topics
    links_article1 = extract_links(article1_content)
    links_article2 = extract_links(article2_content)
    return find_common_elements(links_article1, links_article2)
```

### Description:

Our Wikipedia Game Improvement Proposal aims to enhance the algorithm by leveraging ChatGPT's semantic understanding. ChatGPT identifies the most similar links by analyzing start and target articles, aiding in more efficient pathfinding. This approach guides the BFS search towards the target article by prioritizing relevant links, improving the algorithm's effectiveness. The proposed method enhances the search process by leveraging ChatGPT's ability to comprehend and compare article content. With this improvement, the algorithm becomes more robust, leading to faster and more accurate results in navigating Wikipedia's interconnected topics.

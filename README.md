# KoreanDiscordChatAnalyzer
## Project Overview

The KoreanDiscordChatAnalyzer is an NLP-based project aimed at analyzing chat data from public Korean Discord communities. The goal is to extract meaningful trends, sentiments, and key phrases from chat conversations to gain insights into community dynamics, interests, and feedback. It can serve as a resource for community managers, game developers, and researchers interested in understanding the social interactions and preferences within these digital spaces.

## Breakdown

### Data Collection

* **Prerequisite**: A Discord Bot is required for data collection. To create a Discord bot and obtain a bot token, follow this follow this [tutorial](https://hackernoon.com/creating-a-python-discord-bot-how-to-get-data-for-analysis).
* The `data_collection/discord_data_collector.py` script utilizes a Discord bot to gather chat data from a specified channel in a Korean Discord community. Configured with necessary permissions, the bot fetches and stores up to 100,000 messages (or change to any numbers you need) as a CSV file, focusing on text content, author, and timestamps. Timestamps are converted from UTC to Korea Standard Time.

### Data Cleaning

Performs the following operations:

* Retention of only specified characters such as Korean, English, specific special characters, and emojis.
* Removal of URLs and Discord-specific markup (like user mentions and custom emojis).
* Normalization of repeated sequences to a maximum of three repetitions.
* Trimming whitespace.
* Removal of lines that are empty, contain only whitespace, or consist solely of punctuation, Korean punctuation, numbers, or one to two English characters.

### Analysis

#### Chat Frequency over Time

Identify patterns in chat activity over time to understand peak activity periods and any noticeable trends.

* Use the timestamps in the collected data to aggregate message counts on a daily / weekly / monthly basis. 
* Plot these counts in a time series graph to visualize the chat activity over time.

#### (Monthly) Most Active Users 

Recognize the most active community members on a monthly basis to potentially reward engagement or identify key influencers. 

* Summarize the number of messages per user for each month. 
* Rank users by their message count to find the top contributors.

#### (Monthly) Term Frequency

Analyze the most frequently used terms or words in the community chats to gauge the prevalent topics or interests.

* Tokenize the chat messages into words, remove common stopwords, and count the frequency of each term on a monthly basis.
* Plot the terms in a bar chart or a word cloud.

#### Sentiment Analysis

Assess the general sentiment (positive, negative, neutral) of the community chats to understand the overall mood or response to certain topics or events.

* Apply sentiment analysis on the text content of messages using pre-trained models,  e.g. https://huggingface.co/WhitePeak/bert-base-cased-Korean-sentiment

#### Topic Modeling

Uncover underlying topics in the chat messages to identify key themes or subjects of interest within the community.

* Use topic modeling algorithms like Latent Dirichlet Allocation (LDA) to extract topics from the collection of text data.

## Roadmap

- [x] Collect data from Discord
- [x] Clean and process the collected text
- [ ] Perform core data analysis
- [ ] Build a web interface to visualize insights
- [ ] Add tests to ensure reliability

## Data Privacy and Ethics

- **Public Data Only**: The analysis is performed exclusively on publicly available chat data. No private conversations or personal data are used.
- **Anonymization**: All data used in the project is anonymized to ensure individual privacy is maintained.
- **Ethical Considerations**: The project adheres to ethical guidelines for data usage and analysis, ensuring no community or individual is targeted or negatively impacted.

## License

Distributed under the GNU General Public License v3.0 License. See `LICENSE` file for more information.

## Acknowledgments

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
* Removal of lines that are empty, contain only whitespace, or consist solely of punctuation, Korean punctuation, or numbers.



## Roadmap

- [x] Collect data from Discord
  
- [x] Clean and process the collected text
- [ ] Perform core data analysis
- [ ] Visualize the analysis results
- [ ] Build a web interface to display insights
- [ ] Add tests to ensure reliability

## Data Privacy and Ethics

- **Public Data Only**: The analysis is performed exclusively on publicly available chat data. No private conversations or personal data are used.
- **Anonymization**: All data used in the project is anonymized to ensure individual privacy is maintained.
- **Ethical Considerations**: The project adheres to ethical guidelines for data usage and analysis, ensuring no community or individual is targeted or negatively impacted.

## License

Distributed under the GNU General Public License v3.0 License. See `LICENSE` file for more information.

## Acknowledgments

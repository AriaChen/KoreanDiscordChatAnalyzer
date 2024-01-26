import re
import pandas as pd
from soynlp.normalizer import *


def clean_text(text):
    """
    Cleans the input text according to the rules provided:
    - Retains only specified characters (Korean, English, specific special characters, and emojis)
    - Removes URLs
    - Remove special markup used by Discord to represent user mentions, custom emojis, and channel links
    - Normalizes repeated sequences to a maximum of 3 repetitions
    - Trims leading and trailing whitespace.

    Parameters:
    - text: The input text to be cleaned.

    Returns:
    - Cleaned text.
    """

    # Define patterns
    pattern = re.compile(f'[^ .,?!/@$%~％·∼()\x00-\x7Fㄱ-ㅣ가-힣]+')
    url_pattern = r'https?://\S+|www\.\S+'
    punctuation_pattern = re.compile(r'([.,!?;:()\-\'\"/\\])\1{3,}')
    discord_pattern = r'<(@|#|a?:\w+:)\d+>'

    # Apply transformations
    text = pattern.sub(' ', text)
    text = re.sub(url_pattern, '',  text)
    text = punctuation_pattern.sub(r'\1\1\1', text)
    text = re.sub(discord_pattern, '', text)
    text = repeat_normalize(text, num_repeats=3)
    text = text.strip()

    return text


def is_valid_content(content):
    """
    Determines if the content is invalid according to the rules provided:
    - Is empty or contains only whitespace.
    - Contains only punctuation, Korean punctuation, or numbers.
    - Contains only one or two English characters.

    Parameters:
    - content: The text line to be evaluated for validity.

    Returns:
    - bool: Returns True if the content is valid
    """
    # Check if content is empty or contains only whitespace
    if pd.isna(content) or content.strip() == '':
        return False

    # Regular expression to match only punctuation, Korean punctuation, or numbers
    pattern = re.compile(r'^[.,!?;:()`~\-\'\"/\\ㄱ-ㅎㅏ-ㅣ0-9\s]+$')
    if pattern.match(str(content)):
        return False

    # Check for content with only one or two English letters
    if re.fullmatch(r'[A-Za-z]{1,2}', content.strip()):
        return False

    return True


# Read the data
df = pd.read_csv('../data/chat_data.csv')

# Apply the clean_text function to the 'Content' column
df['Content'] = df['Content'].apply(clean_text)

# Filter out rows based on the 'Content' column
df = df[df['Content'].apply(is_valid_content)]

# Save the result to a new file
df.to_csv('../data/cleaned_chat_data.csv', index=False, encoding='utf-8-sig')
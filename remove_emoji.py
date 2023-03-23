import pandas as pd
import re

# Read excel file into a dataframe
df = pd.read_excel("emoji.xlsx")

# Define a regular expression pattern that matches emoji characters
emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

# Apply the pattern to each column of the dataframe and replace emoji with empty string
df = df.apply(lambda x: x.str.replace(emoji_pattern, ""))

# Save the dataframe to a new excel file
df.to_excel("no_emoji.xlsx", index=False)

#also try

import emoji
df = pd.DataFrame(data={'str_data':['يااا واجعوط هذا راه باغي يبدع فالسانكيام😭🤦‍♀️']})
df['str_data'] = df['str_data'].apply(lambda s: emoji.replace_emoji(s, ''))
df

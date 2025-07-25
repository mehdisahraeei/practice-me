import pandas as pd
import random
import string

def generate_new_code():
    letter1 = random.choice(string.ascii_lowercase)
    number = random.randint(1, 999)
    letters2 = ''.join(random.choices(string.ascii_lowercase, k=2))
    ending = random.choice(['0', '1'])
    return f"MTR_{letter1}{number}{letters2}{ending}"

df = pd.read_csv("info.csv")

df['site code'] = [generate_new_code() for _ in range(len(df))]

df.to_csv("info_updated.csv", index=False)


df.head()

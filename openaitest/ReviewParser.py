"""
This was created by Levi Barksdale, of team Winner's POV, on 3/27/2021 for the HackAI hackathon.

This program implements the OpenAI API to parse through hospital reviews and give them scores to more easily analyze
what the hospitals can improve upon.
"""

import os
import openai

# Super secret API key, please do not steal from me or I will be sad
os.environ["OPENAI_API_KEY"] = "sk-FPYUOFS9qgYnrdEJOhWj5W9rkzZoryXVwgGlRw76"

openai.api_key = os.environ["OPENAI_API_KEY"]

allReviews = ""

# Parses whole input file and compiles into one string that can easily be fed to API
reviewInput = open("reviews.txt", 'r')
for line in reviewInput:
    allReviews = allReviews + line

response = openai.Completion.create(
    engine="davinci-instruct-beta",
    prompt=allReviews,
    temperature=0.1,
    max_tokens=20,
    top_p=0.2,
    frequency_penalty=0,
    presence_penalty=0,
)

print(response.choices[0].text)


# print(allReviews)

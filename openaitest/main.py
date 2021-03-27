# Takes in a text file full of processed reviews and extracts an array of sentiments

import os
import openai

os.environ["OPENAI_API_KEY"] = "sk-x7wPkzm7kRacZPOWZhbOT727pPAY65xRFiDSYCUQ"

openai.api_key = os.environ["OPENAI_API_KEY"]

with open('data.txt', 'r') as file:
    data = file.read().replace('\n', '')

# Parse sentiments from file
sentiments = []
file1 = open("output.txt")
for line in file1.readlines():
    currentLine = (line.strip().split("Sentiment: "))
    # print(sentiment)
    sentimentVal = 0
    for i in currentLine:
        try:
            # print(i)
            sentimentVal = float(i)
            if sentimentVal > 0:
                sentiments.append(sentimentVal)
        except ValueError:
            # print(ValueError)
            pass
    print(sentiments)

file1.close()

# response = openai.Completion.create(
#   engine="davinci",
#   prompt=data,
#   temperature=0.9,
#   max_tokens=150,
#   top_p=1,
#   frequency_penalty=0.0,
#   presence_penalty=0.6,
#   stop=["\n", " Human:", " AI:"]
# )
#
# print(response.choices[0].text.strip())

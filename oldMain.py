
from flask import Flask, jsonify
import feedparser
app = Flask(__name__)
NewsFeed = feedparser.parse("https://news.google.com/rss?hl=en-SG&gl=SG&ceid=SG:en")
entry = []



for i in range(len(NewsFeed)):
  if i > 5:
    break
  entry += [[NewsFeed.entries[i].title,NewsFeed.entries[i].link]]

@app.route('/')
def sg_news():
  return jsonify(entry)
if __name__ == '__main__':
    app.run(host="0.0.0.0")

#i think the most we can do is have the link as a hyperlink so its not so messy
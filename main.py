from flask import Flask, jsonify
import feedparser
import requests

app = Flask(__name__)



entry = []

@app.route("/")
def default_page():
  search_parse = feedparser.parse(f"https://news.google.com/rss?gl=sg")
  return jsonify(search_parsed(search_parse))


@app.route("/search/<search>")
def search_parsing(search):
  search_parse = feedparser.parse(f"https://news.google.com/rss/search?q={search}")
  return jsonify(search_parsed(search_parse))

@app.route('/tag/<country>')
def search_country(country):
  search_parse = feedparser.parse(f"https://news.google.com/rss?gl={country}")
  return jsonify(search_parsed(search_parse))

def search_parsed(search_parse):
  entry = []
  for i in range(len(search_parse)):
    if i > 5:
      break
    r = requests.get(search_parse.entries[i].link)
    entry += [[search_parse.entries[i].title,r.url]]
  return entry





app.run(host='0.0.0.0')


import requests

try:

    # GET - Fetch all posts
    posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()

    # Loop through posts
    for post in posts:
        print(post["body"])

except:
    print("Not able to get the data")

print("hello")

#another example
import json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#another example
response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()
print(data[0]["title"])

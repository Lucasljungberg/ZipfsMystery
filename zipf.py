import praw
import re
import json

r = praw.Reddit("zipf")
subname = "all"

with open("db.json", 'r') as file:
    data = json.loads(file.read())
print("Data loaded.")

linklist = []
def process_comment(comment):
    words = re.split("\\W+", comment)
    for word in words:
        if word == "":
            continue
        if not word in data:
            data[word] = 1
        else:
            data[word] += 1


comments = r.get_comments(subname, limit=10000)
print("Comments gathered")
for comment in comments:
    linklist.append(comment.link_id)
    comment.link_id
    if comment.link_id == data["last_link_ending"]:
        print("Break on iteration %d" %len(linklist))
        break
    process_comment(comment.body.lower())

print("Comments processed")

data["last_link_ending"] = linklist[0]
with open("db.json", 'w') as file:
    json.dump(data, file, indent=4)

print("Saving done.")

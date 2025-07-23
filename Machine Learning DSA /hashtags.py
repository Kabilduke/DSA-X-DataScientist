#NLP
posts = [
    "Loving the new features! #updates #features",
    "Check out our latest blog post! #Blog #update",
    "#Throwback to our first launch day! #throwback #launch",
    "Working on bug fixes. #update #BugFix", 
    "Another day, another deployment. #update #DevOps"
]


import re
from collections import Counter

tags = []

for post in posts:
    hastags = re.findall(r'#(\w+)',post)
    tags.append(hastags[0].lower())

hastag_counts = Counter(tags)
most_common = hastag_counts.most_common()
print("Most commonly used hastags:",most_common[0][0])

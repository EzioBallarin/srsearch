import os
import urllib.request
import praw

r = praw.Reddit(user_agent='example')
search = input("Enter a subreddit name to search for ")
sr = r.get_subreddit(search)
if sr:
    submissions = sr.get_top_from_all(limit=25)
    dir = 'r' + sr.display_name
    if not os.path.exists(dir):
        os.makedirs(dir)
    save_path = os.path.dirname(os.path.realpath(__file__)) + '/' + dir + '/'
    for submission in submissions:
        if submission.is_self is not True and submission.url:
            img_url = submission.url
            if '.jpg' in img_url:
                last = img_url.rfind('/')
                file_path = save_path + img_url[last + 1:]
                if not os.path.isfile(file_path):
                    urllib.request.urlretrieve(img_url, file_path)
                    print("Image " + img_url + " downloaded to " + file_path)
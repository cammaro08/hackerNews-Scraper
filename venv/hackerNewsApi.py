import requests
from urllib.parse import urlparse


def getTopPosts(minPosts):
    posts = []
    topPostsID = getTopPostsIDs(minPosts)
    for i in range(len(topPostsID)):
        newPost = getPostFromID(topPostsID[i])
        cleanPost(i, newPost)
        if checkPostValues(newPost):
            posts.append(newPost)
    return posts


def checkIfStringIsValid(val):
    nonEmptyBool = val != ""
    charactersBool = len(val) < 256
    return nonEmptyBool and charactersBool


# works only if post key names are updated
def checkPostValues(post):
    titleAndAuthorBool = checkIfStringIsValid(post['title']) & checkIfStringIsValid(post['author'])
    pointsCommentsRankBool = (post['points'] & post['comments'] & post['rank']) >= 0
    urlBool = isURL(post['url'])
    if titleAndAuthorBool and pointsCommentsRankBool and urlBool:
        return True
    return False


def cleanPost(postRank, post):
    keysNeedToKeep = ['title', 'url', 'by', 'score', 'descendants']
    for key in list(post.keys()):
        if key in keysNeedToKeep:
            pass
        else:
            del post[key]
    updatePostKeyNames(post)
    post.update({'rank': postRank + 1})


# updates/creates new keys with proper names according to specification
def updatePostKeyNames(post):
    post['author'] = post.pop('by')
    post['points'] = post.pop('score')
    post['comments'] = post.pop('descendants')


def getPostFromID(ID):
    URL = "https://hacker-news.firebaseio.com/v0/item/{}.json".format(ID)
    r = requests.get(url=URL)
    return r.json()


def getTopPostsIDs(minimumPosts):
    URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
    r = requests.get(url=URL)
    return r.json()[0:minimumPosts]


def isURL(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

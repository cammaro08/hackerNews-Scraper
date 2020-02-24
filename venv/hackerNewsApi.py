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


def cleanPost(postRank, post):
    keysNeedToKeep = ['title', 'url', 'by', 'score', 'descendants']
    for key in list(post.keys()):
        if key in keysNeedToKeep:
            pass
        else:
            del post[key]
    makeAllKeysExist(post)
    updatePostKeyNames(post)
    post.update({'rank': postRank + 1})


# creating empty field if missing. Entire post will be checked in the checkPostValues function
def makeAllKeysExist(post):
    keysNeedToKeep = ['title', 'url', 'by', 'score', 'descendants']
    for key in keysNeedToKeep:
        if key not in list(post.keys()):
            post.update({key: ""})


# works only if post key names are updated
def checkPostValues(post):
    if checkNullValues(post):
        pointsCommentsRankBool = (post['points'] & post['comments'] & post['rank']) >= 0
    else:
        pointsCommentsRankBool = False
    urlBool = isURL(post['url'])
    if pointsCommentsRankBool and urlBool:
        return True
    return False


def checkIfStringIsValid(val):
    if type(val) == str:
        nonEmptyBool = val != ""
        charactersBool = len(val) < 256
        return nonEmptyBool and charactersBool
    else:
        return False


def checkIfNumberIsValid(val):
    if type(val) == int:
        return val != ""
    elif type(val) == list:
        temp = val[0]
        return temp != ""
    else:
        return False


def checkNullValues(post):
    titleAndAuthorBool = checkIfStringIsValid(post['title']) & checkIfStringIsValid(post['author'])
    numericsBool = checkIfNumberIsValid(post['points']) \
                   & checkIfNumberIsValid(post['comments']) & checkIfNumberIsValid([post['rank']])
    return titleAndAuthorBool and numericsBool


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


# checks if the input is a valid url
def isURL(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

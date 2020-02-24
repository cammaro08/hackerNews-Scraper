import pytest
import hackerNewsApi


def test_emptyStringsInPosts():
    dummypost = {'title': 'Padlet (YC W13) Is Hiring Designers in the Presidio of San Francisco',
                 'url': 'https://padlet.jobs',
                 'author': 'coffeebite', 'points': 1, 'comments': '', 'rank': 9}
    assert hackerNewsApi.checkNullValues(dummypost) == False


def test_listsInPosts():
    dummypost = {'title': 'Padlet (YC W13) Is Hiring Designers in the Presidio of San Francisco',
                 'url': 'https://padlet.jobs',
                 'author': 'coffeebite', 'points': [1], 'comments': '', 'rank': 9}
    assert hackerNewsApi.checkNullValues(dummypost) == False
    dummypost.update({'comments': 2})
    assert hackerNewsApi.checkNullValues(dummypost) == True


def test_correctPost():
    dummypost = {'title': 'Padlet (YC W13) Is Hiring Designers in the Presidio of San Francisco',
                 'url': 'https://padlet.jobs',
                 'author': 'coffeebite', 'points': 1, 'comments': 3, 'rank': 9}

    assert hackerNewsApi.checkPostValues(dummypost) == True
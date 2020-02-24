# make two get requests
# 1, to get the ids of top posts
# 2, to get the stories.

from hackerNewsApi import getTopPosts


def main():
    posts = getTopPosts(5)
    print(posts)


if __name__ == '__main__':
    main()

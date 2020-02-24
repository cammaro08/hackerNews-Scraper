from hackerNewsApi import getTopPosts


def main():
    posts = getTopPosts(23)
    print(posts)


if __name__ == '__main__':
    main()

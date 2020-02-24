import sys
from hackerNewsApi import getTopPosts


def main():
    try:
        userInput = input("Enter number of top posts you want from hacker news: ")
        val = int(userInput)
    except ValueError:
        sys.exit("Please enter a number")

    if (not val <= 100) & (val > 0):
        sys.exit("Invalid post request. Please request posts between 0 - 100")

    posts = getTopPosts(val)
    print(posts)


if __name__ == '__main__':
    main()

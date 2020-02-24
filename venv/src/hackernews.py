import sys
import argparse
from hackerNewsApi import getTopPosts



# code for passing post argument from command line
parser = argparse.ArgumentParser(description='Display top posts from hacker news')
parser.add_argument('-p','--posts', type=int, help='Please provide an integer number for number of posts')
args = parser.parse_args()


if __name__ == '__main__':
    if (not args.posts <= 100) & (args.posts > 0):
        sys.exit("Invalid post request. Please request posts between 0 - 100")
    posts = getTopPosts(args.posts)

    for s in posts:
        print(s)
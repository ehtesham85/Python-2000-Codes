import argparse

parser=argparse.ArgumentParser()

parser.add_argument("url", help="url of file to download")
parser.add_argument("output", help="by which name you want to save file")

args=args=parser.parse_args()

print(args.url)
print(args.output)


import os
import argparse

parser = argparse.ArgumentParser(description='desc')
parser.add_argument('path', help='Write path to files - myfiles/folder1/...')
parser.add_argument('name', help='Write name file')
parser.add_argument('exp', help='Write expansion file')
args = parser.parse_args()

def renameFiles(path, name, exp):
    for (i, filenames) in enumerate(os.listdir(path)):
        os.rename(path + filenames, path + '{}{}.{}'.format(name, i, exp))
    exit('Done')

if __name__ == '__main__':
    input(renameFiles(args.path, args.name, args.exp))
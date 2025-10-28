import argparse
from pathlib import Path
from .main import Classify
def master():
    parser = argparse.ArgumentParser(description='a cli script to classify your log file')
    
    #paths
    parser.add_argument('readingPath' , type = Path , help = 'the path to the log file you want to classify')
    parser.add_argument('writingPath' , type = Path , help = 'the path where you want to store your files after classification')

    #cli arguments
    parser.add_argument('--de',action = 'store_true' , help = 'classify based on debug')
    parser.add_argument('--inf',action = 'store_true' , help = 'classify based on info')
    parser.add_argument('--war',action = 'store_true' , help = 'classify based on warning')
    parser.add_argument('--err',action = 'store_true' , help = 'classify based on error')
    parser.add_argument('--cri',action = 'store_true' , help = 'classify based on critical')

    args = parser.parse_args()

    instance = Classify(args.readingPath,args.writingPath)

    #cli actions

    if args.de:
        instance.act('DEBUG')

    if args.inf:
        instance.act('INFO')

    if args.war:
        instance.act('WARNING')

    if args.err:
        instance.act('ERROR')

    if args.cri:
        instance.act('CRITICAL')

if __name__ == '__main__':
    master()

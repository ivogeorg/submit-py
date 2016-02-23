__author__ = 'ivogeorg'

import argparse
from sh import git
from sh import ls
from sh import cd

def main(output_file, pa_code):
    cd("./" + pa_code)
    list = ls("-l", _iter=True)
    next(list) # first line in ls output is not a file/dir
    for line in list:
        repo_path = line.split()[-1]
        print repo_path
        cd("./" + repo_path)
        for tag in git.tag(_iter=True):
            print tag,
        cd("..")
    cd("..")

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='This program takes a directory of Github roots and repos and checks them for tags.')

    parser.add_argument('-p', dest='pacode', default="pa1",
                       help='Specifies the programming assignment (pa) code. The default code is "pa1". Used to list the directory containing the cloned git repos.')

    parser.add_argument('-f', dest='outputfile', default="github-pa-repos-tags.txt",
                       help='Specifies the output file for the Github repos and tag list. The default output file is "github-pa-repos-tags.txt".')

    args = parser.parse_args()

    main(args.outputfile, args.pacode)

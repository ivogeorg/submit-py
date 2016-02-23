__author__ = 'ivogeorg'

import argparse
from sh import git
from sh import ErrorReturnCode

# Github URL: "https://github.com/" + github_root + "/" + repo_name + ".git"
# Local repo path: "pa1/ucd-csci2312-pa1-" + github_root

# github_root = "aaboarder"
# repo_name = "PA1"
# github_url = "https://github.com/" + github_root + "/" + repo_name + ".git"
# repo_path = "pa1/ucd-csci2312-pa1-" + github_root
# # git.clone("https://github.com/aaboarder/PA1.git", "pa1/ucd-csci2312-pa1-aaboarder")
# git.clone(github_url, repo_path)
# # TODO - error checking?

# clone the repos for all students
# identify the driver file and overwrite the 'main' function
# insert the grader files into each directory

# {
# insert the CMakeLists.txt file into each directory (filenames?)
# run cmake to generate a Makefile
# run make to build the project
# }

# OR

# {
# just run g++ with flags and files
# }

# run the executable (project name will be the same) with two arguments:
# - the github root name
# - a file name to append the score (create it in ../pa1)

def print_error(line):
    print line


def main(input_file, pa_code):
    with open (input_file, 'r') as f:
        for line in f.readlines():
            github_root, repo_name = line.partition(',')[::2]
            github_root = github_root.strip()
            repo_name = repo_name.strip()
            github_url = "https://github.com/" + github_root + "/" + repo_name + ".git"
            repo_path =  "./" + pa_code + "/ucd-csci2312-" + pa_code + "-" + github_root

            print "Cloning " + github_url + " to " + repo_path

            try:
                # output = git.clone(github_url, repo_path, _err=print_error, _out_bufsize=1)
                output = git.clone(github_url, repo_path, _iter=True)
                print "Output code: " + str(output.exit_code)
                # output.wait() # ???
            except ErrorReturnCode as e:
                aggr = ""
                print "RAN:"
                for c in e.full_cmd:
                    aggr += c
                print aggr
                print "STDOUT:"
                for c in e.stdout:
                    aggr += c
                print aggr
                print "STDERR:"
                for c in e.stderr:
                    aggr += c
                print aggr

            # TODO check if there are any tags (git tag): if not, notify student



if __name__=="__main__":
    parser = argparse.ArgumentParser(description='This program takes a list of Github account roots and repos and clones them.')

    parser.add_argument('-p', dest='pacode', default="pa1",
                       help='Specifies the programming assignment (pa) code. The default code is "pa1". Used for git cloning target directory.')

    parser.add_argument('-f', dest='inputfile', default="github-pa-repos.csv",
                       help='Specifies the input file for the Github accts and repos. The default output file is "github-pa-repos.csv".')

    # TODO add individual (-i) repo, mutually exclusive with (-f), and pass the Github root

    args = parser.parse_args()

    main(args.inputfile, args.pacode)

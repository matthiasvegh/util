#!/usr/bin/env python

import datetime

from git import Repo

def main():
    repo = Repo('.')
    commits = list(repo.iter_commits())

    differences = []

    for commit in commits:
        authordate = commit.authored_date
        commitdate = commit.committed_date
        differences.append(
                datetime.timedelta(seconds = commitdate - authordate))

    maxdelta = max(differences)
    maxcommit = commits[differences.index(maxdelta)]
    print "Max differences was:", maxdelta
    print "   ", maxcommit
    print "   ", maxcommit.message.replace("\n", "\n    ")

    total = sum(differences, datetime.timedelta())

    print "Total difference was:", total

    average = total / len(commits)

    print "Average was:", average


if __name__ == "__main__":
    main()

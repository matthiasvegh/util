#!/usr/bin/env python

import datetime
import matplotlib.pyplot as plt

from git import Repo

def main():
    repo = Repo('.')
    commits = list(repo.iter_commits())

    differences = []
    sizes = []

    for commit in commits:
        authordate = commit.authored_date
        commitdate = commit.committed_date
        sizes.append(commit.stats.total.get('lines')+1)
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

    pairList = [(sizes[i], differences[i]) for i in range(len(differences))]

    pairList = sorted(pairList, key=lambda pair: pair[0])

    sortedSizes = [pair[0] for pair in pairList]
    sortedDifferences = [pair[1].seconds for pair in pairList]

    sortedSizes.remove(sortedSizes[-1])
    sortedDifferences.remove(sortedDifferences[-1])

    plt.plot(sortedSizes, sortedDifferences)
    plt.xlabel("Size of commit in LOC")
    plt.ylabel("Review time in seconds")

    plt.show()

if __name__ == "__main__":
    main()

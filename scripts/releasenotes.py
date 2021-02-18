"""Script building release note draft using tagged PRs.

Collects Pull Requests since last release and categorizes them in the following
categories:
    - Features (tags including "enhancement")
    - Bugfixes (tags including "bug"
    - Tests (tags including "test")
    - Others (all PRs not matching any of the above patterns)

The script then prints these using basic Markdown to Stdout along with some
basic statistics.

To run
 export GITHUB_TOKEN="MY TOKEN"
 python3 GitHubAccont/Repo

Requires the pygithub package.
"""

import os
import sys
import github


repo_name = sys.argv[1] if len(sys.argv) > 1 else 'MycroftAI/mycroft-core'
gh_login = github.Github(os.environ['GITHUB_TOKEN'])
repo = gh_login.get_repo(repo_name)


labels = repo.get_labels()
bugfix_labels = [l for l in labels if 'bug' in l.name.lower()]
feature_labels = [l for l in labels if 'enhancement' in l.name.lower()]
test_labels = features = [l for l in labels if 'test' in l.name.lower()]


def print_pr_info(pr):
    print('- {} (#{}) by @{}'.format(pr.title, pr.number, pr.user.login))

def print_author_link(author):
    print('- [@{}](https://github.com/{})'.format(author, author))


class ReleaseNotes:
    def __init__(self):
        self.bugfixes = []
        self.features = []
        self.tests = []
        self.other = []
        self.authors = set()

    def add(self, pr):
        self.authors.add(pr.user.login)
        for ref in feature_labels:
            if ref in pr.labels:
                self.features.append(pr)
                return
        for ref in bugfix_labels:
            if ref in pr.labels:
                self.bugfixes.append(pr)
                return
        for ref in test_labels:
            if ref in pr.labels:
                self.tests.append(pr)
                return
        self.other.append(pr)

    def __len__(self):
        return (len(self.features) +
                len(self.bugfixes) +
                len(self.tests) +
                len(self.other))


release_notes = ReleaseNotes()
# Latest release as reference
latest_release = repo.get_releases()[0]

pull_requests = repo.get_pulls(state='closed', sort='updated',
                               direction='desc', base=repo.default_branch)

counter = 0  # This is a bad way to handle comments to long closed PR's
for pr in pull_requests:
    if pr.merged and pr.merged_at > latest_release.created_at:
        release_notes.add(pr)
        counter = 0
    elif pr.merged and pr.merged_at < latest_release.created_at:
        counter += 1
        if counter > 10:
            break

# Print all the different things
print('# {}'.format(repo_name))

if release_notes.features:
    print('\n\n## Features')
    for pr in release_notes.features:
        print_pr_info(pr)

if release_notes.bugfixes:
    print('\n\n## Bugfixes')
    for pr in release_notes.bugfixes:
        print_pr_info(pr)


if release_notes.tests:
    print('\n\n## Tests')
    for pr in release_notes.tests:
        print_pr_info(pr)

if release_notes.other:
    print('\n\n## Other changes')
    for pr in release_notes.other:
        print_pr_info(pr)

if release_notes.authors:
    print('\n\n## Contributors list')
    for author in release_notes.authors:
        print_author_link(author)

print('\n\n## Numbers:')
print('\tNumber of authors contributing to '
      'this release: {}'.format(len(release_notes.authors)))
print('\tFeatures: {}'.format(len(release_notes.features)))
print('\tBugfixes: {}'.format(len(release_notes.bugfixes)))
print('\tTests: {}'.format(len(release_notes.tests)))
print('\tOther: {}'.format(len(release_notes.other)))
print('Total: {}'.format(len(release_notes)))

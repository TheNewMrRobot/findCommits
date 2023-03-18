from pydriller import Repository

for commit in Repository('https://github.com/TheNewMrRobot/findCommits.git',only_in_branch="develop").traverse_commits():
    for file in commit.modified_files:
        files = file.diff_parsed
        for file in files["added"]:
            for changes in file:
                if type(changes) == str:
                    if changes.lstrip() == '"version": "1.0.2"':
                        print("-------",commit.hash,"--------")
                        print("found version")
                    else:
                         print("-------Other Commits",commit.hash,"--------")


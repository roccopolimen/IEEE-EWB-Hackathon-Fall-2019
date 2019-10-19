from git import Repo

repo = Repo("D:\Stevens Institute of Technology\IEEE\IEEE-EWB-Hackathon-Fall-2019")
print(repo.untracked_files)
repo.index.add(["D:\Stevens Institute of Technology\IEEE\IEEE-EWB-Hackathon-Fall-2019\plots"])
print(repo.untracked_files)
repo.git.commit('-m', 'test commit', author='stats3434@gmail.com')
repo.remote.origin.push()
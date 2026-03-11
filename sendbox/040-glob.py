import glob

# for filename in glob.glob("**/*.py"):
for filename in glob.glob("**/*.py", recursive=True):
    print(filename)

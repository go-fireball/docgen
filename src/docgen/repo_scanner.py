import os

def scan_repo(repo_path, extensions=(".ts", ".js")):
    files = []
    for root, _, filenames in os.walk(repo_path):
        for file in filenames:
            if file.endswith(extensions):
                files.append(os.path.join(root, file))
    return files

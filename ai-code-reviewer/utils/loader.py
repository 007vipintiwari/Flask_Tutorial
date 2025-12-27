import os

def load_code_files(repo_path, extensions=(".py", ".js", ".java")):
    files = []
    for root, _, filenames in os.walk(repo_path):
        for file in filenames:
            if file.endswith(extensions):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    files.append({
                        "content": f.read(),
                        "path": path
                    })
    return files

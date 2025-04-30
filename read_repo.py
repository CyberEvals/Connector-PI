import git
import os

#clone repo
def clone_repo(repo_url, clone_path='local-repo'):
    if not os.path.exists(clone_path):
        print(f"Cloning repository from {repo_url}...")
        git.Repo.clone_from(repo_url, clone_path)
        print("Repository cloned successfully.")
    else:
        print("Repository already cloned. Skipping clone.")

#read files
def read_text_files(repo_path='local-repo', extensions=('.txt', '.md', '.py', '.json')):
    file_contents = []

    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith(extensions):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        file_contents.append({
                            'file_path': file_path,
                            'content': content
                        })
                except Exception as e:
                    print(f"Failed to read {file_path}: {e}")
    return file_contents

# Example for testing
def main():
    repo_url = "https://github.com/CyberEvals/Connector-PI" 
    clone_repo(repo_url)
    files = read_text_files()

    print(f"\nRead {len(files)} files:\n")
    for file in files:
        print(f"--- {file['file_path']} ---\n{file['content'][:300]}...\n") #prints

if __name__ == "__main__":
    main()

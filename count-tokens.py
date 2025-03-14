import os
import tiktoken
from pathlib import Path
from tiktoken import Encoding


def count_tokens_in_file(file_path: Path, encoding: Encoding) -> int:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return len(encoding.encode(content))


def count_tokens_in_repository(
    repo_path: Path, encoding: Encoding, file_extensions: list[str]
) -> dict:
    """
    Returns a dictionary mapping each file (as a string path) to its token count.
    """
    file_token_map = {}
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith(tuple(file_extensions)):
                file_path = Path(os.path.join(root, file))
                tokens = count_tokens_in_file(file_path, encoding)
                file_token_map[str(file_path)] = tokens
    return file_token_map


def find_each_repo(root: Path) -> list[Path]:
    return [repo for repo in root.iterdir() if repo.is_dir()]


if __name__ == "__main__":
    EXTENSIONS = [".py"]
    encoding = tiktoken.get_encoding("o200k_base")

    # Dictionary mapping repo name to a dict of file token counts.
    repo_file_tokens = {}
    # Dictionary mapping repo name to total token count.
    repo_total_tokens = {}

    for repo in find_each_repo(Path("repos/")):
        file_token_map = count_tokens_in_repository(repo, encoding, EXTENSIONS)
        total_tokens = sum(file_token_map.values())
        repo_file_tokens[repo.name] = file_token_map
        repo_total_tokens[repo.name] = total_tokens

    for repo_name, file_map in repo_file_tokens.items():
        print(f"\nDetails for {repo_name}:")
        for file_path, tokens in file_map.items():
            print(f"  {file_path}: {tokens} tokens")

    for repo_name, tokens in sorted(repo_total_tokens.items(), key=lambda x: x[1]):
        print(f"Total tokens in {repo_name:<40} {tokens:>10}")

    # Write the total token per repo as a csv file
    with open("repo_token_counts.csv", "w") as f:
        f.write("repo_name,total_tokens\n")
        for repo_name, tokens in sorted(repo_total_tokens.items(), key=lambda x: x[1]):
            f.write(f"{repo_name},{tokens}\n")

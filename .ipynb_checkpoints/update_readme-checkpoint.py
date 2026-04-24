# Packages
import os
import re

def generate_readme():
    """
    Function that regenerates my README.md for my Project Euler GitHub Repo.
    Is fairly robust to name changes, but try to adhere to "Problem X [Name].ipynb" for solutions and folders "Problem X-Y"
    """
    REPO_NAME = "Project-Euler"
    
    # Detects folders like "Problems 0-50"
    folders = sorted([d for d in os.listdir('.') if os.path.isdir(d) and "Problems" in d])
    
    content = f"# {REPO_NAME}\n\n"
    content += "![Project Euler](https://img.shields.io/badge/Project-Euler-orange?style=for-the-badge)\n\n"
    content += "These are my solutions to the problems proposed at ![Project Euler](https://projecteuler.net/about) \n\n"

    # Table of Contents
    content += "## Progress\n"
    for folder in folders:
        content += f"- [{folder}](#{folder.lower().replace(' ', '-')})\n"
    content += "\n---\n"

    for folder in folders:
        content += f"### {folder}\n\n"
        content += "| # | Problem Title | Solution |\n"
        content += "| :--- | :--- | :---: |\n"
        
        # Get files and sort them naturally (1, 2, 10 instead of 1, 10, 2)
        files = [f for f in os.listdir(folder) if f.endswith('.ipynb')]
        files.sort(key=lambda f: int(re.search(r'\d+', f).group()) if re.search(r'\d+', f) else 0)

        for file in files:
            # Matches "Problem", then the number, then the title
            match = re.match(r"Problem\s+(\d+)\s+(.*)\.ipynb", file)
            
            if match:
                prob_num = match.group(1)
                prob_title = match.group(2)
                
                problem_url = f"https://projecteuler.net/problem={prob_num}"
                # URL encode spaces for GitHub links
                file_path = f"./{folder.replace(' ', '%20')}/{file.replace(' ', '%20')}"
                
                content += f"| {prob_num} | [{prob_title}]({problem_url}) | [View Notebook]({file_path}) |\n"
        content += "\n"

    with open("README.md", "w") as f:
        f.write(content)
    print("README.md updated successfully!")

if __name__ == "__main__":
    generate_readme()
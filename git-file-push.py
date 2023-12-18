import os
from GitPython.git import Repo

def initialize_github_project(repo_url, image_folder_path):
    # Clone the repository
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    Repo.clone_from(repo_url, repo_name)

    # Change directory to the cloned repository
    os.chdir(repo_name)

    # Check the image folder for files
    image_files = [f for f in os.listdir(image_folder_path) if os.path.isfile(os.path.join(image_folder_path, f))]

    if len(image_files) == 1:
        # Commit and push changes
        commit_and_push(image_folder_path, image_files[0])
        print("Image successfully committed and pushed.")
    else:
        print("Error: There should be exactly one image in the folder.")

def commit_and_push(image_folder_path, image_file):
    repo = Repo(".")
    # Add the image file to the staging area
    repo.index.add([os.path.join(image_folder_path, image_file)])

    # Commit changes
    repo.index.commit("Add image: {}".format(image_file))

    # Push changes to the remote repository
    repo.remote().push()

if __name__ == "__main__":
    # Provide the GitHub repository URL and image folder path
    github_repo_url = "https://github.com/ravirajjak/mock.git"
    image_folder_path = "/Users/nbt1638/Documents/python-workspace/git-img/"

    initialize_github_project(github_repo_url, image_folder_path)

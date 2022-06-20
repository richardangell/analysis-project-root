import sys
import os
from pathlib import Path


def reroot(project_root: str) -> None:
    """Search through parent folders to find the folder called `project_root`.
    If this is found then set the folder as the current working directory and
    insert into sys.path.

    Parameters
    ----------
    project_root : str
        Name of the root folder for the project.

    Raises
    ------
    FileNotFoundError
        If a parent folder called `project_root` is not found.

    """

    if type(project_root) is not str:

        raise TypeError(f"project_root should be str but got {type(project_root)}")

    if Path(".").resolve().stem != project_root:

        root_folder_found = False

        for parent_folder in Path(".").resolve().parents:

            if parent_folder.stem == project_root:

                project_root_path = str(parent_folder)

                root_folder_found = True

        if not root_folder_found:

            raise FileNotFoundError(f"project root folder {project_root} not found")

    else:

        project_root_path = str(Path(".").resolve())

    _insert_into_path(project_root_path)
    _change_working_directory(project_root_path)


def _insert_into_path(path: str) -> None:
    """Insert the given path into the start of sys.path."""

    if path not in sys.path:

        sys.path.insert(0, path)
        print(f"""inserted {path} into sys.path""")

    else:

        print(f"""{path} already in sys.path""")


def _change_working_directory(path: str) -> None:
    """Change the working directory to the specified path."""

    if not os.getcwd() == path:

        os.chdir(path)
        print(f"""changed working directory to {path}""")

    else:

        print(f"""{path} is already working directory""")

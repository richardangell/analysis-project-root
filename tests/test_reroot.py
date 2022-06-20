import sys
import os
import pytest

import analysis_project_root


@pytest.fixture()
def create_sub_directory_structure(tmp_path):
    d = tmp_path / "sub"
    d2 = d / "sub2"
    d.mkdir()
    d2.mkdir()
    return tmp_path, d2


@pytest.fixture()
def create_branched_sub_directory_structure(tmp_path):
    d = tmp_path / "sub"
    d2 = d / "sub2"
    d3 = tmp_path / "sub3"
    d.mkdir()
    d2.mkdir()
    d3.mkdir()
    return tmp_path, d3


@pytest.fixture()
def create_non_sub_directory_structure(tmp_path):
    d = tmp_path
    d.mkdir()
    return tmp_path


def test_exception_raised(create_sub_directory_structure):
    """Test an exception is raised if the root project folder cannot be found."""

    _, temp_sub2 = create_sub_directory_structure

    os.chdir(temp_sub2)

    with pytest.raises(
        FileNotFoundError, match="project root folder does_not_exist not found"
    ):

        analysis_project_root.reroot("does_not_exist")


@pytest.mark.parametrize(
    "dirs",
    ["create_sub_directory_structure", "create_branched_sub_directory_structure"],
)
def test_path_and_cwd_modified(request, dirs):
    """Test that working directory is changed project root and project root is
    inserted into to the path.
    """

    temp_root, temp_sub2 = request.getfixturevalue(dirs)

    os.chdir(temp_sub2)

    temp_root_project_folder = temp_root.stem

    assert os.getcwd() != str(
        temp_root
    ), "working directory already at the project root folder"

    assert str(temp_root) not in sys.path, "project root folder already on path"

    analysis_project_root.reroot(temp_root_project_folder)

    assert os.getcwd() == str(
        temp_root
    ), "working directory not moved to the project root folder"

    assert str(temp_root) == sys.path[0], "project root folder not inserted into path"


def test_path_modified(tmp_path):
    """Test path is modified if already starting with working directory at
    project root.
    """

    os.chdir(tmp_path)

    temp_root_project_folder = tmp_path.stem

    assert os.getcwd() == str(
        tmp_path
    ), "working directory not already at the project root folder"

    assert str(tmp_path) not in sys.path, "project root folder already on path"

    analysis_project_root.reroot(temp_root_project_folder)

    assert os.getcwd() == str(
        tmp_path
    ), "working directory not moved to the project root folder"

    assert str(tmp_path) == sys.path[0], "project root folder not inserted into path"

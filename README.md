# analysis-project-root

Reset project root for analysis projects.

For analysis projects sometimes it is useful to have a  scripts that can import from lots of relative locations in a project;

```
root/
  sub1/
    a.py
    sub2/
      b.py
  sub3/
    c.py
```

This is a very simple package that solves the problem for me and hides away unpleasant code to add to `sys.path` and change the working directory.

To install the package;

```
pip install analysis-project-root
```

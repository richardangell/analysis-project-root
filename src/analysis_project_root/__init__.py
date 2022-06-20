"""analysis_project_root - change the root in an analysis project."""

from ._version import __version__
from .pathmagic import reroot

__all__ = ["reroot", "__version__"]

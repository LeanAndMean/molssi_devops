"""
molssi_devops_uf
A sample repository for the MolSSI Workshop at UF.
"""

# Add imports here
from .molssi_math import canvas, mean
from .string_util import title_case

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions

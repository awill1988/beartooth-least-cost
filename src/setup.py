"""The setup script."""
# setuptools must be imported first
from setuptools import setup, Distribution
from setuptools.command.install import install
import sys

# Workaround for the system-installed setuptools on macOS. That version wants
# to write bytecode files to locations that violate the sandbox, with this
# message:
#
#   The package setup script has attempted to modify files on your system
#   that are not within the EasyInstall build area, and has been aborted.
#
#   This package cannot be safely installed by EasyInstall, and may not
#   support alternate installation locations even if you run its setup
#   script by hand.  Please inform the package's author and the EasyInstall
#   maintainers to find out if a fix or workaround is available.
#
sys.dont_write_bytecode = True

if sys.version_info < (3, 10):
    print("project requires at least Python 3.10", file=sys.stderr)
    sys.exit(1)

from pathlib import Path  # noqa

# Change this to what you want your library code to be called!
PACKAGE_NAME = "lib"

# Path to the directory containing this file
PYTHON_ROOT = Path(__file__).parent.absolute()

# Relative path to this directory from cwd.
FROM_TOP = PYTHON_ROOT.relative_to(Path.cwd())

# Path to the root of the git checkout
SRC_ROOT = PYTHON_ROOT.parents[1]

# Not automatically updated!
version = "0.0.0"

requirements = []

setup_requirements = []


class BinaryDistribution(Distribution):
    def is_pure(self):
        return False

    def has_ext_modules(self):
        return True


class InstallPlatlib(install):
    def finalize_options(self):
        install.finalize_options(self)
        if self.distribution.has_ext_modules():
            self.install_lib = self.install_platlib


setup(
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.10",
    ],
    description="Generic Library SDK",
    install_requires=requirements,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords=PACKAGE_NAME,
    name=PACKAGE_NAME,
    version=version,
    packages=[
        PACKAGE_NAME,
    ],
    package_dir={
        PACKAGE_NAME: FROM_TOP / PACKAGE_NAME,
    },
    setup_requires=[],
    zip_safe=False,
    distclass=BinaryDistribution,
    cmdclass={"install": InstallPlatlib},
)

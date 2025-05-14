from os.path import join, dirname, realpath
from setuptools import setup
import sys

assert sys.version_info.major == 3 and sys.version_info.minor >= 6, \
    "The Spinning Up repo is designed to work with Python 3.6 and greater." \
    + "Please install it before proceeding."

with open(join("spinup", "version.py")) as version_file:
    exec(version_file.read())

setup(
    name='spinup',
    py_modules=['spinup'],
    version=__version__,
    install_requires=[
        'cloudpickle==1.2.1',
        'gym[atari,box2d,classic_control]~=0.15.3',
        'ipython',
        'joblib',
        'matplotlib==3.1.1',
        'mpi4py',
        'numpy',
        'pandas',
        'pytest',
        'psutil',
        'scipy',
        'seaborn==0.8.1',
        'tqdm'
        # ⚠️ REMOVED: tensorflow<2.0
        # ⚠️ REMOVED: torch==1.3.1
        # 🔍 Tip: install TF2 manually via pip install tensorflow-macos
        # 🔍 Tip: install torch manually via pip install torch torchvision torchaudio
    ],
    description="Teaching tools for introducing people to deep RL.",
    author="Joshua Achiam",
)

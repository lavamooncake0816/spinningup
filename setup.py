from os.path import join
from setuptools import setup
import sys

assert sys.version_info.major == 3 and sys.version_info.minor >= 6, \
    "Spinning Up requires Python 3.6+"

with open(join("spinup", "version.py")) as version_file:
    exec(version_file.read())

setup(
    name='spinup',
    py_modules=['spinup'],
    version=__version__,
    install_requires=[
        'cloudpickle==1.2.1',
        'gym[box2d,classic_control]~=0.15.3',
        'ipython',
        'joblib',
        'matplotlib>=3.5.3',  # ✅ Replace 3.1.1 with M1-safe version
        'mpi4py',
        'numpy',
        'pandas',
        'pytest',
        'psutil',
        'scipy',
        'seaborn==0.8.1',
        'tqdm'
        # ❌ 'atari-py' removed
    ],
    description="Teaching tools for introducing people to deep RL.",
    author="Joshua Achiam",
)

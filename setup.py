import setuptools
from importlib import import_module

setuptools.setup(
    name="dcorchestrator",
    author="Massimiliano Galli",
    author_email="massimiliano.galli.95@gmail.com",
    package_dir={"": "src"},
    packages=setuptools.find_packages(),
    install_requires=[],
    python_requires=">=3.8",
)

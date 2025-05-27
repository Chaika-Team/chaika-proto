from setuptools import setup, find_packages

setup(
    name="chaika-proto",
    version="0.3.0",
    packages=find_packages(where="python"),
    package_dir={"": "python"},
    install_requires=[
        "grpcio>=1.30.0",
        "protobuf>=3.15.0",
    ],
)
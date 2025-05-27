from setuptools import setup, find_packages

setup(
    name="chaika-proto",
    version="0.5.0",
    packages=find_packages(),
    install_requires=[
        "grpcio>=1.30.0",
        "protobuf>=3.15.0",
    ],
)
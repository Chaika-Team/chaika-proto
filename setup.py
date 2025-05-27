from setuptools import setup, find_packages

setup(
    name="chaika_proto",
    version="0.5.0",
    description="Chaika Analytics & Reports gRPC stubs",
    # Look under gen/ for packages:
    packages=find_packages(where="gen"),
    package_dir={"": "gen"},
    install_requires=[
        "grpcio>=1.62.2",
        "protobuf>=4.25",
    ],
)
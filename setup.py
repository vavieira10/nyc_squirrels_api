from setuptools import setup, find_packages
setup(
    name = "nyc_squirrels_api",
    version = "latest",
    description = ("API for extracting information of the NYC squirrels census"),
    packages=find_packages(),
    include_package_data=True
)

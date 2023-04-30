from setuptools import setup

setup(
    name="common_io",
    author="tanakenology",
    author_email="tanakenology@gmail.com",
    packages=["common_io"],
    license="tanakenology",
    install_requires=[
        "smart_open[gcs]",
        "smart_open[s3]",
    ],
    extras_require={
        "dev": [
            "black",
            "flake8",
            "isort",
            "pylint",
            "autopep8",
            "pytest",
            "pytest-randomly",
            "mypy",
        ]
    },
)

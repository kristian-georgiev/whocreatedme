from setuptools import setup, find_packages

setup(
    name="whocreatedme",
    version="1.0.0",
    author="Kristian Georgiev",
    author_email="kris.georgiev@hey.com",
    description="Automate file origin tracking in your projects",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kristian-georgiev/whocreatedme",
    packages=find_packages(),
    install_requires=[
        "argparse",
    ],
    entry_points={
        "console_scripts": [
            "whocreatedme=whocreatedme.whocreatedme:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

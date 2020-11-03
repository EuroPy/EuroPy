import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-c0deking",
    author="John Doe",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EuroPy/EuroPyt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License, Version 2.0 (Apache-2.0)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="workbook-api",
    version="0.0.2",
    author="Tobias Balle-Petersen",
    author_email="tobiasbp@gmail.com",
    license="MIT",
    description="A wrapper for the API for workbook.net",
    keywords="Workbook api wrapper client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tobiasbp/workbook-api",
    packages=setuptools.find_packages(),
    install_requires=[
          'requests',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)

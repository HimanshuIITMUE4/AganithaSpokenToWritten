import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Spoken-2-Written",
    version="0.0.1",
    author="Himanshu Kumar",
    author_email="himanshu19kumar95@gmail.com",
    description="Converts a spoken paragraph to written English",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HimanshuIITMUE4/AganithaSpokenToWritten",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

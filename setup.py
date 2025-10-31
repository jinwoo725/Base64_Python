from setuptools import setup, find_packages

setup(
    name="base64_python",
    version="0.4",
    packages=find_packages(),
    install_requires=[],
    author="slave725",
    description="A beginner's base64 encoder/decoder in Python",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
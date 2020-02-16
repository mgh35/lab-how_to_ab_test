import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="how_to_ab_test",
    version="0.0.1",
    author="Mark Higgins",
    description="Lab investigating standard stats for AB testing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        "pandas",
        "numpy"
    ]
)

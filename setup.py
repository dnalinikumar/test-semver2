import setuptools

setuptools.setup(
    name="test",
    version="0.0.4",
    author="Nalini Kumar Danda",
    author_email="d.nalinikumar@gmail.com",
    description="Test package",
    packages=setuptools.find_packages(where="src"),
    package_dir={'':'src/'},
    classifiers=[
        "Programming Language :: Python :: 3.9"
    ],
    python_requires='~=3.9'
)

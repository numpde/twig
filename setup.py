import setuptools

setuptools.setup(
    name="twig",
    version="0.0.2",
    author="RA",
    author_email="numpde@null.net",
    keywords="logging",
    description="Lightweight logger",
    # long_description="",
    # long_description_content_type="text/markdown",
    # url="https://github.com/numpde/twig",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[''],

    # Required for includes in MANIFEST.in
    include_package_data=True,

    test_suite="nose.collector",
    tests_require=["nose"],
)

import setuptools

setuptools.setup(
    name="ssh-pocket",
    version="1.0.0",
    author="Dawn",
    author_email="congminh292k@gmail.com",
    description="Easy peasy ssh choosey",
    keywords="ssh management tool",
    license="MIT",
    url="https://github.com/mmmdawn/ssh-pocket",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux"
    ],
    packages=[],
    entry_points={"console_scripts": ["s="]},
    python_requires=">=3.6",
)

import setuptools
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="ssh-pocket",
    version="1.2.2",
    author="Dawn",
    author_email="congminh292k@gmail.com",
    description="Easy peasy ssh choosey",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords="ssh management tool",
    license="MIT",
    url="https://github.com/mmmdawn/ssh-pocket",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux"
    ],
    dependencies=[
        "inquirerpy ~= 0.3.4"
    ],
    install_requires=[
      "inquirerpy ~= 0.3.4"
    ],
    packages=["pocket"],
    entry_points={"console_scripts": ["s=pocket.__main__:main", "si=pocket.import_ssh:main"]},
    python_requires=">=3.6",
)

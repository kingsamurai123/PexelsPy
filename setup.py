import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pexelsPy",
    version="1.0.2",
    author="Sravan Kumar Shaganti",
    author_email="demonlyf98@protonmail.com",
    description="Use Pexels API v1 with Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kingsamurai123/pexels-api",
    keywords='pexels api images photos videos',
    install_requires=['requests'],
    packages=setuptools.find_packages(),
    
)
"""
Previous repo details

setuptools.setup(
    name="pexels-api",
    version="1.0.1",
    author="Arturo Aguilar Lagunas",
    author_email="aguilar.lagunas.arturo@gmail.com",
    description="Use Pexels API v1 with Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AguilarLagunasArturo/pexels-api",
    keywords='pexels api images photos',
    install_requires=['requests'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

"""

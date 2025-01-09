from setuptools import setup, find_packages

setup(
    name="DECaLSQuery",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'astroquery',
        'astropy',
        'requests'
    ],
    description="A package for querying the DECaLS catalog and downloading image cutouts.",
    author="Akhil Krishna R",
    author_email="akhil.r@res.christuniversity.in",
    url="https://github.com/akhilkrishnar0/DECaLSQuery",
)

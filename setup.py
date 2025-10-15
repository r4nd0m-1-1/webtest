from setuptools import setup, find_packages

setup(
    name="webtest",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "aiohttp", "requests", "beautifulsoup4", "lxml",
        "pyyaml", "click", "colorama", "cryptography", "python-nmap"
    ],
    entry_points={
        "console_scripts": ["webtest=webtest:main"]
    }
)

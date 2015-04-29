from setuptools import setup

requires = [
    "BeautifulSoup4",
    "six",
    "webhelpers2",
]

setup(name="bphtml",
      namespace_packages=["beproud"],
      packages=["beproud", "beproud.html"],
      test_suite="beproud.html",
      install_requires=requires,
)

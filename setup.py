"""Setup for flight_paths."""


from setuptools import setup


setup(
    name='code-katas',
    description="Python Practice: distance between points, \
     https://codefellows.github.io/sea-python-401d6/assignments/kata_flight_paths.html",
    version='0.1',
    author="",
    license='MIT',
    py_modules=['flight_paths', 'test_flight_paths'],
    install_requires=[''],
    package_dir={'': "src"},
    extras_require={'testing': ['pytest', 'pytest-cov', 'tox']},
)

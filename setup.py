from setuptools import setup


setup(
    name='code-katas',
    description="what it does",
    version='0.1',
    author="",
    license='MIT',
    py_modules=['vasya_clerk',''],
    install_requires=[''],
    package_dir={'': "src"},
    extras_require={'testing': ['pytest', 'pytest-cov', 'tox']},
)

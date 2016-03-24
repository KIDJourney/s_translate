from setuptools import setup, find_packages

setup(
    name="translateit",
    version='0.0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},

    zip_safe=False,

    install_requires=[
            'requests',
    ],


    classifiers=[
        'Programming Language :: Python :: 3',
    ],

    author="KIDJourney",
    author_email="kingdeadfish@qq.com",
    description="This is a simple console translator",
    license="MIT",
    keywords="hello world translate requests",

    entry_points={
        'console_scriptes': [
            'foo = translate.__main__:main',
        ],
    }
)

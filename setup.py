from setuptools import find_packages, setup

setup(
    name='foodkm',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'responder==1.3.0',
        'requests',
        'lxml',
        'unicodecsv',
        'pandas',
        'jupyter',
        'ipython',
        'bs4',
        'numpy',
        'pyopenssl',
        'ndg-httpsclient',
        'pyasn1',
        'selenium'
    ],
    extras_require={
        'example': [
            'ipdb',
            'jupyter',
            'jupyter-client',
            'jupyter-console',
            'ipython',
            'pylint',
            'flake8',]
    },
    scripts=[
        'scripts/debug'
    ]
)
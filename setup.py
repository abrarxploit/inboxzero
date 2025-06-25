from setuptools import setup, find_packages

setup(
    name='inboxzero',
    version='1.0.0',
    author='Abrar',
    description='Autonomous sentiment-based Gmail purging tool using BERT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'google-api-python-client',
        'google-auth-httplib2',
        'google-auth-oauthlib',
        'transformers',
        'torch',
    ],
    entry_points={
        'console_scripts': [
            'inboxzero=inboxzero.__main__:main',
        ],
    },
)

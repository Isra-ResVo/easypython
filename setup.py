from setuptools import find_packages, setup
setup(
    name='basicSIRA',
    packages=find_packages(include=['basicSIRA']),
    version='0.0.0',
    description='My first Python library',
    author='Israel Rescalvo',
    license='MIT',
    install_requires=['requests_htlm', 'requests']
)

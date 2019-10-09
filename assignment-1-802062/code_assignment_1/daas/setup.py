""" Sets up Trucaller API """
from setuptools import setup, find_packages

VERSION = '0.1.01'

setup(
    name='daas_api',
    version=VERSION,
    description='Daas Api',
    long_description='Providing web services to read and write CoreDms',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3'
    ],
    keywords='oak daas api',
    author='Omer Ahmed Khan',
    author_email='omerahmed122@gmail.com',
    url='',
    license='',
    packages=find_packages(),
    install_requires=['flask-restful', 'pymongo', 'pandas'],
    include_package_data=True,
    zip_safe=False
)
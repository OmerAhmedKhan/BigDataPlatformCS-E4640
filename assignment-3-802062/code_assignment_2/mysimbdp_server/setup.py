""" Sets up Trucaller API """
from setuptools import setup, find_packages

VERSION = '0.1.01'

setup(
    name='mysimbdpServer API',
    version=VERSION,
    description='mysimbdpServer Api',
    long_description='Providing web services to data ingest into CoreDms',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3'
    ],
    keywords='oak mysimbdpServer api',
    author='Omer Ahmed Khan',
    author_email='omer.khan@aalto.fi',
    url='',
    license='',
    packages=find_packages(),
    install_requires=['flask-restful', 'pymongo', 'pandas', 'pika', 'pyspark'],
    include_package_data=True,
    zip_safe=False
)
from setuptools import setup, find_packages
import byte_api


setup(
    name='byte-api',
    version=byte_api.__version__,

    author=byte_api.__author__,

    url='https://github.com/byte-api/byte-python',
    download_url='https://github.com/byte-api/byte-python/archive/v{}.zip'.format(
        byte_api.__version__
    ),

    description='Byte API Wrapper',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    license='MIT',

    packages=find_packages(),
    install_requires=['requests']
)

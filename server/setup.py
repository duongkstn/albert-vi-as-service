from os import path

from setuptools import setup, find_packages

# setup metainfo
libinfo_py = path.join('albert_vi_serving', 'server', '__init__.py')
libinfo_content = open(libinfo_py, 'r').readlines()
version_line = [l.strip() for l in libinfo_content if l.startswith('__version__')][0]
exec(version_line)  # produce __version__

setup(
    name='albert_vi_serving_server',
    version=__version__,
    description='Mapping a variable-length sentence to a fixed-length vector using BERT model (Server)',
    url='https://github.com/duongkstn/albert_vi_as_service',
    long_description=open('README.md', 'r', encoding="utf8").read(),
    long_description_content_type='text/markdown',
    author='duongkstn',
    author_email='nguyenduongyht@gmail.com',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'numpy',
        'six',
        'pyzmq>=17.1.0',
        'GPUtil>=1.3.0',
        'termcolor>=1.1'
    ],
    extras_require={
        'cpu': ['tensorflow>=1.10.0'],
        'gpu': ['tensorflow-gpu>=1.10.0'],
        'http': ['flask', 'flask-compress', 'flask-cors', 'flask-json', 'bert-serving-client']
    },
    classifiers=(
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ),
    entry_points={
        'console_scripts': ['albert-vi-serving-start=albert_vi_serving.server.cli:main',
                            'albert-vi-serving-benchmark=albert_vi_serving.server.cli:benchmark',
                            'albert-vi-serving-terminate=albert_vi_serving.server.cli:terminate'],
    },
    keywords='bert nlp tensorflow machine learning sentence encoding embedding serving',
)

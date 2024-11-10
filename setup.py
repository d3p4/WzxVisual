from setuptools import setup, find_packages

setup(
    name='WzxVisual',
    version='0.1.1',
    packages=find_packages(),
    author='ysoseri',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
    ],
)

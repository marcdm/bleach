from setuptools import setup, find_packages

setup(
    name='bleach',
    version='1.3.0',
    description='An easy whitelist-based HTML-sanitizing tool.',
    long_description=open('README.rst').read(),
    author='James Socol',
    author_email='me@jamessocol.com',
    url='http://github.com/jsocol/bleach',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['README.rst']},
    zip_safe=False,
    install_requires=['html5lib>=1.0b1'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: Mozilla',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

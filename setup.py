from setuptools import setup

import os.path

requirements_filename = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'requirements.txt')

with open(requirements_filename) as fd:
    install_requires = [i.strip() for i in fd.readlines()]

setup(
    name='dhcpwn',
    version='1.0.1',
    description='All your IPs are belong to us.',
    url='https://github.com/mschwager/dhcpwn',
    py_modules=['dhcpwn'],
    license='GPLv3',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Security',
    ],
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'dhcpwn = dhcpwn:main',
        ],
    },
)

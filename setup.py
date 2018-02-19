#!/usr/bin/env python

from setuptools import setup

from pycoin1.version import version

setup(
    name="pycoin1",
    version=version,
    packages=[
        "pycoin1",
        "pycoin1.blockchain",
        "pycoin1.cmds",
        "pycoin1.coins",
        "pycoin1.contrib",
        "pycoin1.convention",
        "pycoin1.ecdsa",
        "pycoin1.ecdsa.native",
        "pycoin1.key",
        "pycoin1.message",
        "pycoin1.networks",
        "pycoin1.serialize",
        "pycoin1.services",
        "pycoin1.tx",
        "pycoin1.tx.pay_to",
        "pycoin1.tx.script",
        "pycoin1.wallet"
    ],
    author="Vikram Singh",
    entry_points={
        'console_scripts':
            [
                'block = pycoin1.cmds.block:main',
                'ku = pycoin1.cmds.ku:main',
                'tx = pycoin1.cmds.tx:main',
                'msg = pycoin1.cmds.msg:main',
                # these scripts are obsolete
                'genwallet = pycoin1.cmds.genwallet:main',
                'spend = pycoin1.cmds.spend:main',
                'bu = pycoin1.cmds.bitcoin_utils:main',
            ]
        },
    author_email="viksingh98@gmail.com",
    url="https://github.com/gujjar95/pycoin",
    license="http://opensource.org/licenses/MIT",
    description="Utilities for Bitcoin and altcoin addresses and transaction manipulation.",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],)

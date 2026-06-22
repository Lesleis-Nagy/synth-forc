#!/usr/scripts/env python

# Copyright 2023 L. Nagy, Miguel A. Valdez-Grijalva, W. Williams, A. Muxworthy,  G. Paterson and L. Tauxe
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
# following conditions are met:
#
#   1. Redistributions of source code must retain the above copyright notice, this list of conditions and the
#      following disclaimer.
#
#   2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the
#      following disclaimer in the documentation and/or other materials provided with the distribution.
#
#   3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote
#      products derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#
# Project: synth-forc
# File: setup.py
# Authors: L. Nagy, Miguel A. Valdez-Grijalva, W. Williams, A. Muxworthy,  G. Paterson and L. Tauxe
# Date: Jan 25 2023
#

from setuptools import setup, find_packages

setup(
    name="synth-forc",
    version="0.2.4",
    description="A tool used to visualise synthetic FORC data generated using micromagnetic models.",
    url="https://github.com/Lesleis-Nagy/synth-forc",
    author="L. Nagy, Miguel A. Valdez-Grijalva, W. Williams, A. Muxworthy,  G. Paterson and L. Tauxe",
    author_email="lesleisnagy@gmail.com",
    packages=find_packages(
        where="lib",
        include="synth_forc/*",
    ),
    package_dir={"": "lib"},
    install_requires=[
        "typer>=0.15,<1.0",
        "rich>=13.7,<14",
        "numpy>=1.26,<3",  # numpy 2 is supported (np.NaN usage removed); <2 has no Python 3.13 wheels
        "matplotlib>=3.8,<4",
        "pandas>=2.2,<3",
        "scipy>=1.11,<2",  # interp2d was removed in scipy 1.14; migrated to RectBivariateSpline (plotting/forc.py)
        "pyyaml>=6.0.1,<7",
        "schematics==2.1.1",
        "falcon>=3.1,<4",
        "gunicorn>=21.2,<23",
        "msgpack>=1.0.8,<2"
    ],
    include_package_data=True,
    entry_points="""
    [console_scripts]
    synth-forc-cli=synth_forc.cli.forc:main
    """,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)

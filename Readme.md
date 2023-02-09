Synth FORC
==========

Synth-FORC is a simple yet powerful tool that can generate forward models of synthetic first order reversal curves 
(FORC) using micromagnetic models.


Installation
------------
You can install `synth-forc` using the `pip` command line tool in the following way

`$> pip install synth-forc`

The tool may then be run from the command line using

`$> synth-forc`

A [data set](https://zenodo.org/record/7625521) of FORC data is available on Zenodo (if you make use of
this data set in your projects/publications please cite the DOI: 10.5281/zenodo.7625521). The micromagnetic software
[MERRILL](https://www.rockmag.org) was used to generate this data.

Notes for developers
--------------------

When up-versioning the code you will need to change the version in the following files before tagging
* `lib/synth_forc/__init__.py`
* `setup.py`

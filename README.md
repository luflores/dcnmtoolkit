
# Description

The DCNM Toolkit is a set of python libraries that allow basic
configuration of Cisco Data Center Network Manage. It is intended to allow users to quickly begin using the
REST API and accelerate the learning curve necessary to begin using the APIC.


# Installation

## Environment

Required

* Python 2.7+
* [setuptools package](https://pypi.python.org/pypi/setuptools)

## Downloading

Option A:

If you have git installed, clone the repository

    git clone https://github.com/kecorbin/dcnmtoolkit.git



## Installing

After downloading, install using setuptools.

    cd dcnmtoolkit
    python setup.py install

If you plan on modifying the actual toolkit files, you should install the developer environment that will link the package installation to your development directory.

    cd dcnmtoolkit
    python setup.py develop

Alternatively you can install directly via pip

    pip install dcnmtoolkit


ack
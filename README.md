forked from [dashpay/sentinel](https://github.com/dashpay/sentinel)


# Ukkey Sentinel

[![Build Status](https://travis-ci.org/UkkeyCoin/sentinel.svg?branch=master)](https://travis-ci.org/UkkeyCoin/sentinel)

> An automated governance helper for Ukkey Masternodes.

Sentinel is an autonomous agent for persisting, processing and automating Ukkey governance objects and tasks. It is a Python application which runs alongside the UkkeyCore instance on each Ukkey Masternode.

## Table of Contents
- [Install](#install)
  - [Dependencies](#dependencies)
- [Usage](#usage)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Maintainer](#maintainer)
- [Contributing](#contributing)
- [License](#license)

## Install

These instructions cover installing Sentinel on Ubuntu 16.04 / 18.04.

### Dependencies

Make sure Python version 2.7.x or above is installed:

    python --version

Update system packages and ensure virtualenv is installed:

    $ sudo apt-get update
    $ sudo apt-get -y install python-virtualenv

Make sure the local UkkeyCore daemon running is at least version 12.1 (120100)

    $ ukkey-cli getinfo | grep version

### Install Sentinel

Clone the Sentinel repo and install Python dependencies.

    $ git clone https://github.com/ukkeyHG/sentinel.git && cd sentinel
    $ virtualenv ./venv
    $ ./venv/bin/pip install -r requirements.txt

## Usage

Sentinel is "used" as a script called from cron every minute.

### Set up Cron

Set up a crontab entry to call Sentinel every minute:

    $ crontab -e

In the crontab editor, add the lines below, replacing '/path/to/sentinel' to the path where you cloned sentinel to:

    * * * * * cd /path/to/sentinel && ./venv/bin/python bin/sentinel.py >/dev/null 2>&1

### Test Configuration

Test the config by running tests:

    $ ./venv/bin/py.test ./test

With all tests passing and crontab setup, Sentinel will stay in sync with ukkeyd and the installation is complete

## Configuration

An alternative (non-default) path to the `ukkey.conf` file can be specified in `sentinel.conf`:

    ukkey_conf=/path/to/ukkey.conf

## Troubleshooting

To view debug output, set the `SENTINEL_DEBUG` environment variable to anything non-zero, then run the script manually:

    $ SENTINEL_DEBUG=1 ./venv/bin/python bin/sentinel.py

## Maintainer

[@UkkeyHG](https://github.com/UkkeyHG)

## Contributing

Please follow the [UkkeyCore guidelines for contributing](https://github.com/ukkeyHG/UkkeyCoin/blob/master/CONTRIBUTING.md).

Specifically:

* [Contributor Workflow](https://github.com/ukkeyHG/UkkeyCoin/blob/master/CONTRIBUTING.md#contributor-workflow)

    To contribute a patch, the workflow is as follows:

    * Fork repository
    * Create topic branch
    * Commit patches

    In general commits should be atomic and diffs should be easy to read. For this reason do not mix any formatting fixes or code moves with actual code changes.

    Commit messages should be verbose by default, consisting of a short subject line (50 chars max), a blank line and detailed explanatory text as separate paragraph(s); unless the title alone is self-explanatory (like "Corrected typo in main.cpp") then a single title line is sufficient. Commit messages should be helpful to people reading your code in the future, so explain the reasoning for your decisions. Further explanation [here](http://chris.beams.io/posts/git-commit/).

## License

Released under the MIT license, under the same terms as UkkeyCore itself. See [LICENSE](LICENSE) for more info.

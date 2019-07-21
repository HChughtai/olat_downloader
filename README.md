# olat_downloader

A simple means of downloading all user uploaded files from the NSHCS's soon to be decommissioned OLAT platform.

## Prerequisites
* Python 3
* A downloaded OLAT report
* Your OLAT login details

## Installation

```
$ mkvirtualenv olat
$ workon olat
$ pip install -r requirements.txt
```

## Usage

The script acts on a generated and downloaded OLAT summary report by:

1. Logging into OLAT with the provided details
2. Extracting all file urls from a provided exported report pdf
3. Downloading all files into a `downloads` folder in the script's root directory

```
$ python download.py # running without options will make the script prompt for input

Usage: download.py [OPTIONS]

Options:
  --report PATH    the downloaded OLAT report
  --username TEXT  the email address used to login to OLAT
  --password TEXT  the OLAT password
  --help           Show this message and exit.
```

## Known bugs and limitations

* Files are all downloaded into a single folder - no hierarchical structure is maintained.
  
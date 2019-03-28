import click
import os
import pdfx
import re
import requests
from bs4 import BeautifulSoup

@click.command()
@click.argument('report', type=click.Path(exists=True))
def download(report):
    
    # extract links from pdf
    pdf = pdfx.PDFx(report)
    references_dict = pdf.get_references_as_dict()

    data = [value for (key, value) in (references_dict.items())]
    merged_data = [j for i in data for j in i]
    filtered_data = filter(check_file_url, merged_data)

    #import pdb; pdb.set_trace()

def create_olat_session(olat_username, olat_password):

def get_olat_file(olat_session, url_path):


def check_file_url(url_path):
    
    expr = p = re.compile('.*\.\w{3,4}$')
    
    is_file_url = expr.match(url_path)
    
    if is_file_url:
        return True
    else:
        return False

if __name__ == '__main__':
    download()
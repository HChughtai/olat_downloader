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

    import pdb; pdb.set_trace()

    return 1

def create_olat_session(olat_username, olat_password):

    form_data = {'name': olat_username, 'pass': olat_password,"form_build_id": "form-aJoz9y0op4X9SURCNSrc_wZaVYM4_2lkzhCPMyMy7r4", "form_id":"user_login", "op":"Log+in"} 
    login_url = "https://olat.nshcs.org.uk/user/login"
    session = requests.Session()
    session.post(login_url, data=form_data)
    
    return session


def get_olat_file(olat_session, url_path):
    pass


def check_file_url(url_path):
    
    expr = p = re.compile('.*\.\w{3,4}$')
    
    is_file_url = expr.match(url_path)
    
    if is_file_url:
        return True
    else:
        return False

if __name__ == '__main__':
    download()
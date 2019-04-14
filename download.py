import click
import os
import pdfx
import re
import requests
import tkinter as tk
from tkinter import filedialog

@click.command()
@click.option('--report', prompt=False,type=click.Path(exists=True),help='the downloaded OLAT report')
@click.option('--username', prompt=True,help='the email address used to login to OLAT')
@click.option('--password', prompt=True, hide_input=True,
              confirmation_prompt=True,help='the OLAT password')


def download(report,username,password):

    if report is None:
        root = tk.Tk()
        root.withdraw()

        report = filedialog.askopenfilename()

    click.echo("Reading report from %s" % report)

    # extract links from pdf
    pdf = pdfx.PDFx(report)
    references_dict = pdf.get_references_as_dict()

    data = [value for (key, value) in (references_dict.items())]
    merged_data = [j for i in data for j in i]
    filtered_data = filter(check_file_url, merged_data)

    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    
    session = create_olat_session(username, password)
    click.echo("Logged into OLAT as %s" % username)

    output_folder = filedialog.askdirectory()

    for url in filtered_data:
        file_name = url.rsplit('/', 1)[1]

        if os.path.isfile(output_folder+'/'+file_name) == True:
            click.echo("Skipping %s - file exists on disk" % url)
        else:
            get_olat_file(session,url,file_name)


def create_olat_session(olat_username, olat_password):

    form_data = {'name': olat_username, 'pass': olat_password,"form_build_id": "form-aJoz9y0op4X9SURCNSrc_wZaVYM4_2lkzhCPMyMy7r4", "form_id":"user_login", "op":"Log+in"} 
    login_url = "https://olat.nshcs.org.uk/user/login"
    session = requests.Session()
    session.post(login_url, data=form_data)
    
    return session


def get_olat_file(session, url,file_name):
    
    try:
        r = session.get(url, allow_redirects=True)
        click.echo("Downloading %s" % url)
        open('downloads/'+file_name, 'wb').write(r.content)

    except requests.exceptions.RequestException:
        click.echo("Skipping %s - not an accessible url" % url)

        


def check_file_url(url_path):
    
    expr = p = re.compile('.*\.\w{3,4}$')
    
    is_file_url = expr.match(url_path)
    
    if is_file_url:
        return True
    else:
        return False

if __name__ == '__main__':
    download()
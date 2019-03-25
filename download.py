import click
import os
from functools import reduce
import pdfx
import json

@click.command()
@click.argument("report")
def download(report):
    
    # check if the file pointed to exists
    if os.path.isfile(report) == False:
        click.echo("Invalid file %s" % report)    
        return
    
    # extract links from pdf
    pdf = pdfx.PDFx(report)
    references_dict = pdf.get_references_as_dict()
    
    with open('data/result.json', 'w') as fp:
        json.dump(references_dict, fp)


if __name__ == '__main__':
    download()
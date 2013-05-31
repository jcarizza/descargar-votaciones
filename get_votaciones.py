#!/usr/bin/python
# encoding: utf8

import urllib2
import urllib
import re
import os
import sys
import argparse
from bs4 import BeautifulSoup


def check_url(url):
    if not (url.startswith("http://") or url.startswith("https://")):
        log("\nURL need http:// or https:// prefix\n")
        sys.exit(1)


def create_folder(folder):
    """ Create folder if not exists """
    if os.path.exists(folder) is False:
        os.mkdir(folder)

    return folder


def save_links(links):
    """ Save links after download """
    with open("links.txt", "w") as f:
        for link in links:
            f.write("%s\n" % (link))
        f.close()
    log("\nLinks saved on %s file\n" % (f.name))


def log(data):
    """ print some info """
    sys.stdout.write(data)
    sys.stdout.flush()


def get_links(url):
    """ get pdf download links """
    log("Fetching links...")

    response = urllib2.urlopen(url)
    _html = BeautifulSoup(response.read())

    # Get links
    links = []
    for a in _html.find(class_="treeview").find_all("a", href=re.compile("\s*.pdf")):
        links.append(a.attrs["href"])

    log("\nPDF links found: %i\n" % (len(links)))
    return links


def download(links, output_folder):
    """ Download each one pdf file """

    total = len(links)
    downloaded = 0
    for pdf_url in links:
        file_name = os.path.basename(pdf_url)
        try:
            urllib.urlretrieve(pdf_url, "%s/%s" % (output_folder, file_name))
            # Update status
            downloaded += 1
            log("\rDownloaded: %d/%d" % (downloaded, total))
        except IOError:
            # File not found
            log("\rError downloading %s" % (pdf_url))

    log("\nFinalized...")


# Getting arguments
parser = argparse.ArgumentParser(description='Descargar PDF de votaciones nominales')
parser.add_argument("--folder",
                    help="Carpeta destino para PDF descargados",
                    type=create_folder, required=True)

parser.add_argument('--keep-links',
                    action='store_true',
                    help='Conservar links de PDF en un archivo links.txt')

parser.add_argument("--url",
                    help="URL del período de \
                    votaciones nominales Ej.: \
                    http://www.diputados.gov.ar/secadmin/ds_electronicos/periodo/2013/index.html",
                    required=True)


if __name__ == "__main__":

    # Get args
    args = parser.parse_args()
    output_folder = args.folder
    url = args.url
    keep_links = args.keep_links

    # Start process
    check_url(url)
    links = get_links(url)
    download(links, output_folder)

    # Keep links?
    if keep_links:
        save_links(links)

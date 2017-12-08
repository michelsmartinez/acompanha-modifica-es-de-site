#coding: utf-8

import requests
import os
from bs4 import BeautifulSoup
import re
import emailpy
import time


def get(url, de, senha, para):
    html = re.sub(r"<script.+?</script>", "", requests.get(url).text)
    html_soup = BeautifulSoup(html, 'html.parser')
    _msg = html_soup.find('body').get_text().strip()
    log = open('./status.log', 'r')
    status_anterior = ''.join(log.readlines())
    msg = ""
    for line in _msg.split('\n'):
        line_limpa = line.strip()
        if line_limpa != "":
            msg += line_limpa + '\n'

    if status_anterior != msg:
        log.close()
        emailpy.send(de, senha, para, 'Status modificado', msg)
        log = open('./status.log', 'w')
        log.write(msg)
    log.close()


if __name__ == '__main__':
    frequencia = int(os.sys.argv[5])
    while True:
        get(str(os.sys.argv[1]),
            str(os.sys.argv[2]),
            str(os.sys.argv[3]),
            str(os.sys.argv[4]))
        time.sleep(frequencia)

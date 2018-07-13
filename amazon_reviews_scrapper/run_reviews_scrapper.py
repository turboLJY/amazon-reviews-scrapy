# -*- coding: utf-8 -*-
"""
Created on: 07-Jul-2018

@author: Ai
"""


import os
import subprocess
from time import sleep
import pandas as pd
from pyfiglet import figlet_format


def main():
    print(figlet_format("Amazon Reviews Scrapper"))
    asin_data = pd.read_excel('./Data/ASIN_Data.xlsx').fillna('')
    cwd = os.getcwd()
    if not os.path.exists(cwd+'\\Output'):
        os.makedirs(cwd+'\\Output', exist_ok=True)
    if not os.path.exists(cwd+'\\Output\\Original'):
        os.makedirs(cwd+'\\Output\\Original', exist_ok=True)
    for i in range(asin_data.shape[0]):
        output_file = './Output/Original/{}_{}.json'.format(asin_data.iloc[i]['Country'], asin_data.iloc[i]['ASIN'])
        command = 'scrapy crawl amazon-reviews-spider -a store={0} -a product_id={1} -o {2}'.format(asin_data.iloc[i]['Store'], asin_data.iloc[i]['ASIN'], output_file)
        print("======\n{0}\n======\n\n".format(command))
        p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=False)
        (output, err) = p.communicate()
        p_status = p.wait()
        print(p_status)
        sleep(2)


if __name__ == '__main__':
    main()

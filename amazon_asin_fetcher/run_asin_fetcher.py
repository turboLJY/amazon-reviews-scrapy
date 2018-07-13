# -*- coding: utf-8 -*-
"""
Created on: 07-Jul-2018

@author: Ai
"""

from time import sleep
import subprocess
import plac
from AmazonSources.AmazonSources import AMS


@plac.annotations(
    country=("Amazon Website Country", "option", "c", str),
    key=("Search Key Phrase (use +)", "option", "k", str))
def main(country=None, key=None):
    ams = AMS()
    if key is None:
        raise Exception(("Key Phrase required!"))

    if country is None:
        raise Exception("Country required!")
    else:
        if country == "all":
            for c, s in ams.stores.items():
                output_file = './Output/asin_' + c + '.json'
                command = 'scrapy crawl asin -a country={0} -a key={1} -o {2}'.format(s, key, output_file)
                print("\n~~~~~~\n{0}\n~~~~~~\n".format(command))
                p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=False)
                (output, err) = p.communicate()
                p_status = p.wait()
                print(p_status)
                sleep(1)
        else:
            s = ams.stores[country]
            output_file = './Output/asin_' + country + '.json'
            command = 'scrapy crawl asin -a store={0} -a key={1} -o {2}'.format(s, key, output_file)
            print("\n~~~~~~\n{0}\n~~~~~~\n".format(command))
            p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=False)
            (output, err) = p.communicate()
            p_status = p.wait()
            print(p_status)
            sleep(1)


if __name__ == '__main__':
    plac.call(main)

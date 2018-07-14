# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 12:10:49 2018

@author: Ai
"""

import re
import os
import json
from os import path
from tqdm import tqdm


def fix(json_files):
    for file in tqdm(json_files):
        if os.stat('./Output/Original'+file).st_size:
            f = open('./Output/Original'+file, 'r').readlines()
            new_f = []
            for line in f:
                if line != '][\n':
                    new_f.append(line)
                else:
                    print("Fixed Error in:", file)
            for i in range(1, len(new_f)-2):
                if "}," not in new_f[i]:
                    new_f[i] = re.sub("}", "},", new_f[i])
            with open('./Output/New'+file, 'w') as openfile:
                for i in new_f:
                    openfile.write(i)


def check(json_files):
    err_f = []
    for file in tqdm(json_files):
        if os.stat('./Output/New'+file).st_size:
            try:
                f = json.load(open('./Output/New'+file, 'r'))
            except Exception as e:
                print("\nError:", file)
                err_f.append(file)
    return err_f


def main():
    """
    Fixes and checks repair of broken JSON files created by the Scrapy spider.
    """
    # Fetch All JSON Files
    print("Fetching JSON Files...")
    json_files = [f for f in os.listdir('./Output/Original') if path.isfile(path.join('./Output/Original', f))]
    # Fix JSON Files
    fix(json_files)
    json_files = [f for f in os.listdir('./Output/New') if path.isfile(path.join('./Output/New', f))]
    # Check Fix Operation
    check(json_files)


if __name__ == '__main__':
    main()

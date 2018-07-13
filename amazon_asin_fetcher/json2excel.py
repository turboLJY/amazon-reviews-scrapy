# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 00:14:20 2018

@author: Ai
"""

import os
from os.path import isfile, join
import json
import pandas as pd
from AmazonSources.AmazonSources import AMS
from tqdm import tqdm


def create_df(json_files):
    country = []
    asin = []
    product = []
    for file in tqdm(json_files):
        f = json.load(open('./Output/'+file, 'r'))
        country.extend([file.split('.')[0].split('_')[1] for i in range(len(f))])
        asin.extend([i['ASIN'] for i in f])
        product.extend([i['Product'] for i in f])
    asin_data = pd.DataFrame({'ASIN': asin, 'Product': product,
                              'Country': country}, columns=['ASIN', 'Product', 'Country'])
    return asin_data


def main():

    ams = AMS()
    # Fetch All JSON Files
    print("Fetching JSON Files...")
    json_files = [f for f in os.listdir('./Output') if isfile(join('./Output', f))]

    # Create ASIN Database
    print("Creating ASIN Database...")
    asin_data = create_df(json_files)

    region = [ams.region[i] for i in tqdm(asin_data['Country'].tolist())]
    s = [ams.stores[i] for i in tqdm(asin_data['Country'].tolist())]

    asin_data['Region'] = pd.Series(region)
    asin_data['Store'] = pd.Series(s)

    # Save ASIN Database
    print("Saving ASIN Database...")
    asin_data.to_excel('./Data/ASIN_Data.xlsx')


if __name__ == '__main__':
    main()

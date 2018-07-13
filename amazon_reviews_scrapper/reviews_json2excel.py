# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 11:08:39 2018

@author: Ai
"""


import os
from os import path
import json
import pandas as pd
from tqdm import tqdm


def create_df(json_files, df1):
    review_data = pd.DataFrame(columns=['Product_ID', 'Review_ID', 'Date',
                                        'Review_Title', 'Review', 'Stars',
                                        'Author', 'Helpful_Count', 'Store'])
    country = []
    product = []
    region = []
    for file in tqdm(json_files):
        if os.stat('./Output_v2/'+file).st_size:
            asin = file.split('.')[0].split('_')[1]
            f = pd.DataFrame(json.load(open('./Output/New'+file, 'r')))
            review_data = pd.concat([review_data, f], sort=False).fillna('')
            country.extend([df1[df1['ASIN'] == asin].iloc[0]['Country'] for i in range(f.shape[0])])
            product.extend([df1[df1['ASIN'] == asin].iloc[0]['Product'] for i in range(f.shape[0])])
            region.extend([df1[df1['ASIN'] == asin].iloc[0]['Region'] for i in range(f.shape[0])])
        review_data['Country'] = pd.Series(country)
        review_data['Region'] = pd.Series(region)
        review_data['Product Description'] = pd.Series(product)
    return review_data


def main():

    # Fetch All JSON Files
    print("Fetching JSON Files...")
    json_files = [f for f in os.listdir('./Output/New') if path.isfile(path.join('./Output/New', f))]

    # Open Original ASIN Data
    df1 = pd.read_excel('./Data/ASIN_Data.xlsx', index=False).fillna('')

    # Create Reviews df
    print("Creating Reviews Database...")
    reviews_data = create_df(json_files, df1)

    # Save Amazon Reviews Database
    print("Saving Reviews Database...")
    reviews_data.to_excel('./Data/AmazonReviews_All_EN.xlsx')


if __name__ == '__main__':
    main()

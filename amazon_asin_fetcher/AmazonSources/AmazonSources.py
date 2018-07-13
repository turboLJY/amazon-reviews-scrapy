# -*- coding: utf-8 -*-
"""
Created on: 4-Jul-2018

@author: Ajinkya Indulkar
"""


class AMS():
    def __init__(self):
        self.stores = {
                       'India': 'amazon.in',
                       'China': 'amazon.cn',
                       'Japan': 'amazon.co.jp',
                       'France': 'amazon.fr',
                       'Germany': 'amazon.de',
                       'Italy': 'amazon.it',
                       'Netherlands': 'amazon.nl',
                       'Spain': 'amazon.es',
                       'UK': 'amazon.co.uk',
                       'Canada': 'amazon.ca',
                       'Mexico': 'amazon.com.mx',
                       'US': 'amazon.com',
                       'Australia': 'amazon.com.au',
                       'Brazil': 'amazon.br',
                       }

        self.region = {
                       'India': 'Asia',
                       'China': 'Asia',
                       'Japan': 'Asia',
                       'France': 'Europe',
                       'Germany': 'Europe',
                       'Italy': 'Europe',
                       'Netherlands': 'Europe',
                       'Spain': 'Europe',
                       'UK': 'Europe',
                       'Canada': 'North America',
                       'Mexico': 'North America',
                       'US': 'North America',
                       'Australia': 'Oceania',
                       'Brazil': 'South America',
                       }

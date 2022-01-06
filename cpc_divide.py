# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 13:59:38 2021

@author: young
"""

import pandas as pd

path_dir = './electronic_manufacture_2021-main/patent_data/patent/'
file_list = os.listdir(path_dir)

for j in file_list:  
    data = pd.read_csv("./electronic_manufacture_2021-main/patent_data/patent/"+j) #데이터 import
    cpc_sets=[]
    sample = data['cpcs'].to_list()
    for i in sample:
        cpc_set = ''
        i = pd.DataFrame(eval(i))
        for c in i['cpc_subgroup_id']:
            try:
                cpc = c.split('/')[0]
                cpc_set = cpc_set +','+ cpc
            except:
                cpc_set = cpc_set + 'None'
        cpc_sets.append(cpc_set)
    data['cpc_set'] = cpc_sets
    data['cpc_set'] = data['cpc_set'].str.lstrip(",")
    data.to_csv('./electronic_manufacture_2021-main/patent_data/cpc_devide/cpc_'+j, encoding='utf8', index=False)
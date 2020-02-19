#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# library
import pandas as pd


def main():
    '''
    （このコメント欄にメソッドの説明を書く）
    （シンプルで他の人が見て分かりやすいことが大切）
    main
    
    argument:

    '''
    meshsize = "1000"

    # 1) Load
   
    input_data = "../data/src/input.csv"
    output_data = "../data/dev/step1.csv"
    
    df = pd.read_csv(input_data)
    
    # 2) processing
    
    df = cleansing(mcr_data1, mcr_data2)
    

    # 3) export
    df.to_csv(output_data, index=False, encoding="utf-8")


def cleansing(df):
    '''
    cleansing the data.
    
    argument:
    1. df
    '''


    return df
    

if __name__ == '__main__':
    main()
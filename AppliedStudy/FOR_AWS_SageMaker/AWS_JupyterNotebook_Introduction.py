
# coding: utf-8

# # AWS Sage maker Introduction
# * ファイルの読み書きはすべてS3上で実施
# * 参考：　https://recipe.kc-cloud.jp/archives/10921
# * https://github.com/awslabs/amazon-sagemaker-examples/blob/master/advanced_functionality/scikit_bring_your_own/scikit_bring_your_own.ipynb

# ## 共通実施事項
# * sagemakerライブラリのインポート
# * S3情報の登録
# * IAMアカウント情報の登録

# IAMのroleの宣言

# In[138]:


import boto3
import re
import sagemaker
from sagemaker import get_execution_role
import pandas as pd
import io
import os
role = get_execution_role()


# ## S3
# ### 登録
# 読み込みと書き込みで用いる変数の指定

# In[139]:


BUCKET = 'yourbucketname' #バケット名を入力
inpath = "file/to/path/" #入力データまでのパス
infile = "scotlip.csv" #入力データのファイル名
KEY = inpath + infile

outpath = "out/to/path/"
outfile = "scot_test.csv"
outKEY = outpath + outfile


# ### 読み込み

# In[140]:


# S3からCSVをダウンロード
s3 = boto3.client('s3')
response = s3.get_object(Bucket=BUCKET, Key=KEY)

data = pd.read_csv(io.StringIO(response['Body'].read().decode('utf-8'))) #decode以下で文字コードを指定する


# In[141]:


data.head(5)


# In[142]:


test = data["NAME"]
test.head(3)


# ### 書き込み
# 一旦SageMakerの/home上に書き込んだのち、botoを用いてS3に移動。
# 参考　https://qiita.com/is_ryo/items/e16527db5800854cd95f

# In[143]:


test.to_csv(outfile)


# In[144]:


s3 = boto3.resource('s3')
bucket = s3.Bucket(BUCKET)
bucket.upload_file(outfile, outKEY)


# ### home/上のファイルを削除
# 容量節約のため、必ず行うこと。

# In[148]:


os.remove(outfile)


# ### ライブラリのインストール
# * 試験的にpyprojライブラリをインストール
# * 参考：　[公式ガイド](https://docs.aws.amazon.com/ja_jp/sagemaker/latest/dg/nbi-add-external.html)
# 
# ⇒問題なくインストール・インポートに成功　Colab上と同様。

# In[124]:


get_ipython().system('pip install pyproj')


# In[125]:


import pyproj


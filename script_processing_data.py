#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 04:54:30 2022

@author: khalifardy
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

data = pd.read_excel('raw_data_survey.xlsx')
data_null = data.isnull().sum()#untuk menghitung jumlah data null
median = data.median()["waktu tunggu kerja"]
data["waktu tunggu kerja"] = data["waktu tunggu kerja"].fillna(median) #isi data null

data_rata_rata_jur = data.groupby('Asal Jurusan', as_index=False)['waktu tunggu kerja'].mean()
data_rata_rata_pengalaman = data.groupby('pengalaman kerja', as_index=False)['waktu tunggu kerja'].mean()
data_rata_rata_organisasi = data.groupby('aktif organisasi', as_index=False)['waktu tunggu kerja'].mean()
#data_rata_rata_organisasi = data.groupby('aktif organisasi', as_index=False)['waktu tunggu kerja'].mean()
data_rata_rata_pelatihan = data.groupby('menikuti pelatihan', as_index=False)['waktu tunggu kerja'].mean()
keys_peng = [i for i in data_rata_rata_pengalaman['pengalaman kerja']]
keys_org = [i for i in data_rata_rata_organisasi['aktif organisasi']]
keys_pel = [i for i in data_rata_rata_pelatihan['menikuti pelatihan']]
values =[i for i in data_rata_rata_pengalaman['waktu tunggu kerja']]
corelasi= data.corr()



#membuat plot rata-rata jurusan dibanding dengan waktu tunggu
fig,ax = plt.subplots(figsize=(8,6))
ax.hist(data_rata_rata_jur)
ax.set_xticks(range(len(data_rata_rata_jur['waktu tunggu kerja'])))
ax.set_xticklabels(data_rata_rata_jur['Asal Jurusan'])
ax.tick_params(axis='x', labelrotation=90)
ax.set_ylabel("rata-rata")
ax.set_title("Perbandingan jurusan dengan waktu tunggu")
fig.tight_layout()


fig1,ax1 = plt.subplots(figsize=(8,5))
ax1.bar(keys_peng,values)
ax1.set_xlabel("pengalaman")
ax1.set_ylabel("rata-rata waktu tunggu")
ax1.set_title("perbandingan pengalaman dengan waktu tunggu")
plt.show()


fig2,ax2 = plt.subplots(figsize=(8,5))
ax2.bar(keys_org,values)
ax2.set_xlabel("aktif organisasi")
ax2.set_ylabel("rata-rata waktu tunggu")
ax2.set_title("perbandingan aktif organisasi dengan waktu tunggu")
plt.show()

fig3,ax3 = plt.subplots(figsize=(8,5))
ax3.bar(keys_org,values)
ax3.set_xlabel("mengikuti pelatihan")
ax3.set_ylabel("rata-rata waktu tunggu")
ax3.set_title("perbandingan mengikuti pelatihan dengan waktu tunggu")
plt.show()


"""
plt.hist(data_rata_rata_jur, bins=len(data_rata_rata_jur))
plt.title("Rata-rata lama waktu tunggu per jurusan ")
plt.xlabel("jurusan")
plt.ylabel("rata-rata")
plt.xticks(rotation=90)

plt.show()
"""
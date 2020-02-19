# Exercise2

## Summary

* 緯度経度からメッシュコードを生成するサンプルコード。

## Usage


### 0. 共通

`緯度経度<=>メッシュコード変換` をまとめている`meshlonlat.py`をimport

```
from meshlonlat import lonlat2mesh, mesh2lonlat
```

### 1. メッシュコードから緯度経度を取得する例

* `addlonlat.py` を参照してください。

```

meshcode = []
for index, row in df.iterrows():
    meshcode.append(row.KEY_CODE)

lon = []
lat = []
for i in range(len(meshcode)):
    _lat, _lon = mesh2lonlat(str(int(meshcode[i])), 500)
    lon.append(_lon)
    lat.append(_lat)

df['longitude'] = lon
df['latitude'] = lat
```

### 2. 緯度経度からメッシュコードを取得する例

```
for i in range(len(df)):
    meshcode_WGS.append(lonlat2mesh(lon[i], lat[i], meshsize=500))
```


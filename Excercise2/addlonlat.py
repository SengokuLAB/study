from meshlonlat import lonlat2mesh, mesh2lonlat
import pandas as pd

def main():
    """""
    関数の説明を記載
    
    例）
    緯度経度にメッシュコードを付与
    
    引数がある場合には、引数の説明を書く。　
    返り値（return）がある場合には、返り値の説明を書く
    　整数型(int）かどうかなど。
    """""
    
    input_path = '~/data/product/FuturePopulation/ver1.6/src/estat500/mesh500.txt'
    output_path = '~/data/product/FuturePopulation/ver1.6/src/estat500/mesh500_meshcode.csv'
    
    df = pd.read_csv(input_path)
    df = df.reindex(columns=["KEY_CODE","lat","lon","T000847001","T000847025"])

    lon = []
    lat = []
    for i in range(len(df)):
        meshcode = df["KEY_CODE"][i]
        _lat, _lon = mesh2lonlat(str(meshcode), 500)
        lon.append(_lon)
        lat.append(_lat)

    df['lat'] = pd.DataFrame(lat)
    df['lon'] = pd.DataFrame(lon)
    df.to_csv(output_path, index=False)

if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-

"""
    全ノード間の最短経路を標準出力に出力する。
"""

import argparse
import csv
import datetime
import os
import sys
import time
import pandas as pd

from dijkstra import *

def main():
    """
    メイン実行処理
    サンプルエリア：　世田谷区
    
    """
    
    nodefilename = "./data/osm_roads_nodes_13112.csv"
    edgefilename = "./data/osm_roads_13112.csv"
    targetfilename = "./data/buildings_node.csv"
    outputfilename = "./data/shortest_path.csv"
    
    shortest_path(nodefilename, edgefilename, targetfilename, outputfilename)


def shortest_path(nodefilename, edgefilename, targetfilename, outputfilename):
    """
    main func:  
    1 Import
      1) 道路ノード（頂点）
      2) 道路ネットワーク（辺）
      3) OD（始点と終点ノードID）の組み合わせ
    2 Processing
    """
    
    # 1 Import
    allnodes = pd.read_csv(nodefilename)
    allnodes["node_id"] = allnodes["node_id"].astype(int)

    edges = load_topology(edgefilename)
    targets = load_targets(targetfilename)


    # summary of data
    print('Number of all nodes: {:,d}'.format(len(allnodes)))
    print('Number of all edges: {:,d}'.format(len(edges)))
    print('Number of OD: {:,d}'.format(len(targets)))
    print('-' * 80)
    print('Started at {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))

    # 2 Processing
    out_list = getShortestPath(allnodes, edges, targets)

    # 3 Export
    #header = ['NodeNo1', 'NodeNo2', 'Distance'	, 'PathNodeNo_List']
    header = ['都道府県','市区町村','町丁目','番地・号','築年','築月','構造','マンション最上階数','間取別平均平米単価①','間取別平均平米単価②','間取別平均平米単価③','間取別平均平米単価④','間取別平均平米単価⑤','key_code','id_building','lat','lon','station_name','station_lat','station_lon','geom','node_id1','node_id2','geom_station','Distance', 'PathNodeNo_List']
    out_df = pd.DataFrame(out_list, columns=header)
    out_df.to_csv(outputfilename, index=False, quotechar='"')

    print('Finished at {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))


    
def load_topology(filename):
    """
        道路ネットワーク（位相情報）を読み込み、各リンクの長さが入ったリストを返す
        サンプルファイル：　osm_roads_13112.csv
        
        必要なパラメータ：
        始点 node1_id
        終点 node2_id
        リンク長 distance
    """
    #列
    ROW_NODE_NUMBER1 = 5
    ROW_NODE_NUMBER2 = 6
    ROW_EDGE_LENGTH = 0
    
    edges = {}

    reader = csv.reader(open(filename))
    row = next(reader)

    line_count = 0
    for row in reader:
        if len(row) == 0: continue
        if row[ROW_NODE_NUMBER1] == "": continue
        line_count += 1

        node_number1 = int(row[ROW_NODE_NUMBER1])
        node_number2 = int(row[ROW_NODE_NUMBER2])
        edge_length = float(row[ROW_EDGE_LENGTH])
        index1 = node_number1
        index2 = node_number2

        if index1 not in edges:
            edges[index1] = {}
        if index2 not in edges:
            edges[index2] = {}
        edges[index1][index2] = edges[index2][index1] = edge_length

    return edges


def load_targets(filename):
    """
        最短経路を求めたい経路の始点と終点になり得る全ての点を読み込む。
        サンプルファイル： target_node.csv
        
        下北沢、三軒茶屋の例を記載。
    """

    df = pd.read_csv(filename, dtype = {'node_id':'object', 'node_id2':'object'})
    df.dropna(subset=['node_id', 'node_id2'], inplace=True)
    df = df.rename(columns={'node_id': 'node_id1'})
    df['node_id2'] = df.apply(lambda x: str(x['node_id2'])[:8] + str(x['node_id2'])[9:16] , axis=1).astype(int)
    df['node_id1'] = df.apply(lambda x: str(x['node_id1'])[:8] + str(x['node_id1'])[9:16] , axis=1).astype(int)
    #print(df['node_id1'])

    df = df.drop_duplicates(keep='last', subset=['node_id1','node_id2'])

    return df

def getShortestPath(allnodes, edges, targets):
    """
    経路リストを返す
    
    parameter
    allnodes
    edges
    targets(od) 
    """
    _t = time.time()
    _count = 0
    out_list = [] #['NodeNo1', 'NodeNo2', 'Distance', 'geometry', 'PathNodeNo_List']


    for idx1, v in targets.iterrows():
        #if _count == 5: break
        node_number1 = int(v["node_id1"])
        node_number2 = int(v["node_id2"])

        # dijkstra
        index_in_nodes1 = node_number1
        index_in_nodes2 = node_number2

        distance, path = dijkstra_find(allnodes, index_in_nodes1, index_in_nodes2, edges)
        

        if path == None:
            print(node_number2)
            continue

        out = list(v.values)
        #out = [
        #        node_number1,
        #        node_number2,
        #]
        # path
        if path is None:
            out.extend(['0','None'])
        else:

            #
            out.extend([
                str(distance),
                '_'.join(
                    '{}'.format(n)
                    for n in path
                ),
            ])

        out_list.append(out)
		

        # 進捗を表示
        _count += 1
        if 3.0 < time.time() - _t:
            #n = len(targets) * (len(targets) - 1) / 2
            n = len(targets)
            print('    calculating {} / {} ({:.2f}%)'.format(
                _count, n, _count * 100.0 / n,
            ))
            _t = time.time()
    return out_list

main()
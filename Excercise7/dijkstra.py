# -*- coding: utf-8 -*-

import heapq


def dijkstra_find(num_nodes, end, start, edges):
    """
        無向グラフの全ノード間の最短距離と最短経路をダイクストラ法で計算する。

        返り値は (距離, [ノード, ノード, ..., ノード]) というtupleを要素とする
        サイズN*Nの2次元配列となる。（Nはノード数）
        
        dist[i] ... startからiまでの最短距離
        prev[i] ... iまでの最短経路においてiの直前に通過するノード

    """

    dist = {}
    node_id_list = num_nodes.node_id
    for v in node_id_list.values:
        dist[int(v)] = 99999999
    
    dist[start] = 0
    prev = {}

    q = []
    # 始点追加
    heapq.heappush(q, (0, start))

    
    # 空になったら止まる 全件探索
    while q:
        # 取り出す
        current_cost, current_node = heapq.heappop(q)
        # 始点ノードとリンクするノードを取得
        adjacent_nodes = edges.get(current_node, {}).keys()
        
        for next_node in adjacent_nodes:
            next_cost = edges[current_node][next_node] #始点-終点のノードを入れてコストを取得
            
            # 更新する 最小距離
            if dist[next_node] > dist[current_node] + next_cost:
                
                dist[next_node] = dist[current_node] + next_cost
                heapq.heappush(q, (dist[next_node], next_node))
                prev[next_node] = current_node # 直前に通過するノード

    # 終点を入れると探索的に取得
    # 最後の列を経路配列に挿入。最後の列が初期のメッシュでない限り

    path = [end]
    n = 0
    while path[-1] != start:

        if n == 10000:
            return (-1, None)
        n += 1

        if not path[-1] in prev: continue
        
        prev_node = prev[path[-1]]
        
        if prev_node is None:
            return (-1, None)
        path.append(prev_node)
        
    return (dist[end], path[::-1])

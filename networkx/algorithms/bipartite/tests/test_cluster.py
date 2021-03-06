import networkx as nx
from nose.tools import *
from networkx.algorithms.bipartite.cluster import cc_dot,cc_min,cc_max
import networkx.algorithms.bipartite as bipartite

def test_pairwise_bipartite_cc_functions():
    # Test functions for different kinds of bipartite clustering coefficients
    # between pairs of nodes using 3 example graphs from figure 5 p. 40 
    # Latapy et al (2008)
    G1 = nx.Graph([(0,2),(0,3),(0,4),(0,5),(0,6),(1,5),(1,6),(1,7)])
    G2 = nx.Graph([(0,2),(0,3),(0,4),(1,3),(1,4),(1,5)])
    G3 = nx.Graph([(0,2),(0,3),(0,4),(0,5),(0,6),(1,5),(1,6),(1,7),(1,8),(1,9)])
    result = {0:[1/3.0, 2/3.0, 2/5.0], 1:[1/2.0, 2/3.0, 2/3.0], 2:[2/8.0, 2/5.0, 2/5.0]}
    for i, G in enumerate([G1, G2, G3]):
        assert(bipartite.is_bipartite(G))
        assert(cc_dot(set(G[0]), set(G[1])) == result[i][0])
        assert(cc_min(set(G[0]), set(G[1])) == result[i][1])
        assert(cc_max(set(G[0]), set(G[1])) == result[i][2])

def test_star_graph():
    G=nx.star_graph(3)
    # all modes are the same
    answer={0:0,1:1,2:1,3:1}
    assert_equal(bipartite.clustering(G,mode='dot'),answer)
    assert_equal(bipartite.clustering(G,mode='min'),answer)
    assert_equal(bipartite.clustering(G,mode='max'),answer)

def test_path_graph():
    G=nx.path_graph(4)
    answer={0:0.5,1:0.5,2:0.5,3:0.5}
    assert_equal(bipartite.clustering(G,mode='dot'),answer)
    assert_equal(bipartite.clustering(G,mode='max'),answer)
    answer={0:1,1:1,2:1,3:1}
    assert_equal(bipartite.clustering(G,mode='min'),answer)


def test_average_path_graph():
    G=nx.path_graph(4)
    assert_equal(bipartite.average_clustering(G,mode='dot'),0.5)
    assert_equal(bipartite.average_clustering(G,mode='max'),0.5)
    assert_equal(bipartite.average_clustering(G,mode='min'),1)





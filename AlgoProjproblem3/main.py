import mcdm
import graphrank

if __name__ == '__main__':
    distance = {'City-Link Express': 30, 'DHL': 80, 'GDEX': 55, 'J&T': 63, 'Pos Laju': 70}
    semantic = {'City-Link Express': 8.5, 'DHL': 6.4, 'GDEX': 9.3, 'J&T': 1.87, 'Pos Laju': 4.86}
    # lists from dict for mcdm
    courier_company = list(semantic.keys())
    distance_list = list(distance.values())
    semantic_list = list(semantic.values())
    # multi criteria decision making
    mcdm.min_normalize(distance_list)
    mcdm.max_normalize(semantic_list)
    mcdm_list = mcdm.mcdm_weighted_sum(distance_list, 0.5, semantic_list, 0.5)  # result
    mcdm_dict = dict(zip(courier_company, mcdm_list))
    print("multi criteria decision making result: ", mcdm_dict)
    # plot graph for most to least recommended ranking
    graphrank.plot_graph_rank(mcdm_dict)

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def choose_num_of_clusters(dataframe):
    close_prices = np.array(dataframe.Close)
    close_prices = close_prices.reshape(-1, 1)
    possible_clusters = [-1]*(21)
    for i in range(3, 20):
        desired_clusters = i
        kmeans_model = KMeans(n_clusters=desired_clusters)
        clusters = kmeans_model.fit_predict(close_prices)  # this data is a series data of all the clusters eacgh data point is assigned in
        silhouette_score_avg = silhouette_score(close_prices, clusters)
        possible_clusters.append(silhouette_score_avg)
    optimal_num_of_clusters = max(x for x in possible_clusters)  # the most optimal number pf clusters
    return possible_clusters.index(optimal_num_of_clusters)

def get_Support_and_Resistance(dataframe, optimal_cluster_size):
    OpenPrices = np.array(dataframe.Open.copy())
    ClosePrices = np.array(dataframe.Close.copy())
    open_and_closeprices = OpenPrices + ClosePrices  # Sum of Open and Close prices is unlikely to be meaningful
    open_and_closeprices = open_and_closeprices.reshape(-1, 1)
    kmeans_model = KMeans(n_clusters=optimal_cluster_size)
    clusters = kmeans_model.fit_predict(open_and_closeprices)
    clusters = np.array(clusters)

    cluster_and_prices_dict = {}
    for cluster in range(optimal_cluster_size):
        cluster_and_prices_dict[cluster] = []
    for index, cluster in enumerate(clusters):
        cluster_and_prices_dict[cluster].append(open_and_closeprices[index])

    supp_and_resis = []
    for cluster in cluster_and_prices_dict.keys():
        if cluster == 0:
            supp_and_resis.append(min(cluster_and_prices_dict[cluster]))
        else:
            supp_and_resis.append(max(cluster_and_prices_dict[cluster - 1]) + min(cluster_and_prices_dict[cluster]) / 2)
            if cluster == list(cluster_and_prices_dict.keys())[-1]:
                supp_and_resis.append(max(cluster_and_prices_dict[cluster]))

    return supp_and_resis.sort()







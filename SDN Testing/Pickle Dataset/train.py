import pickle
import bz2
import cPickle

import classifiers
import warnings
import numpy

data_path_test = 'Hostpairs-one-second-bursts-test.pbz2'
data_path_train = 'Hostpairs-one-second-bursts-train.pbz2'

results_file = "results_all"

#this function extracts a list of tuples of the form [ (website label, [array of pkt lens]) ]
def read_data_from_pickles(path_):
    data_ = bz2.BZ2File(path_, 'rb')
    data_ = cPickle.load(data_)
    X_flows, labels = [], []
    for label, flow in data_:
        #print(len(flow))
        X_flows.append(flow)
        labels.append(label)

    return X_flows, labels


def train_it():

    results = {}
    x_train_flows, y_train_labels = read_data_from_pickles(data_path_train)
    x_test_flows, y_test_labels = read_data_from_pickles(data_path_test) #data_path_test
    results['my dataset'] = {}

    #X_tr_flow = x_train_flows[0:]
    # print(len(X_tr_flow))
    #y_tr_labels = y_train_labels[0:]
    #X_te_flow = x_test_flows[0:]
    #y_te_labels = y_test_labels[0:]


    #####################################################################
    classifier_name = "liberatoreNB2006"
    print("running", classifier_name)
    y_test, y_pred = classifiers.liberatore_2006.classifier_liberatore_NB(x_train_flows,
                                                              y_train_labels,
                                                              x_test_flows,
                                                              y_test_labels,
                                                              )
    
    results = classifiers.common_utils.get_results(results, 'my dataset', classifier_name, y_test, y_pred, results_file)
    #####################################################################
    #print(results)


    #####################################################################
    classifier_name = "liberatoreJaccard2006"
    print("running", classifier_name)
    y_test, y_pred = classifiers.liberatore_2006.classifier_liberatore_jaccard(x_train_flows,
                                                                   y_train_labels,
                                                                   x_test_flows,
                                                                   y_test_labels,
                                                                   )
    results = classifiers.get_results(results, 'my dataset', classifier_name, y_test, y_pred, results_file)
    #####################################################################

    #####################################################################
    classifier_name = "panchenko_2011"
    print("running", classifier_name)
    y_test, y_pred = classifiers.panchenko_2011.classifier_panchenko2011(x_train_flows,
                                                                         y_train_labels,
                                                                         x_test_flows,
                                                                         y_test_labels,
                                                                         )
    results = classifiers.get_results(results, 'my dataset', classifier_name, y_test, y_pred, results_file)
    #####################################################################


    #####################################################################
    classifier_name = "panchenko_2016"
    print("running", classifier_name)

    #print(len(x_test_flows))
    # print(y_test_labels)
    # print(len(y_train_labels))
    y_test, y_pred = classifiers.panchenko_2016.classifier_panchenko2016(x_train_flows,
                                                                         y_train_labels,
                                                                         x_test_flows,
                                                                         y_test_labels,
                                                                         )

    results = classifiers.get_results(results, 'my dataset', classifier_name, y_test, y_pred, results_file)
    #####################################################################


    
    #####################################################################
    classifier_name = "dyer_2012_notime"
    print("running", classifier_name)
    y_test, y_pred = classifiers.dyer_2012.classifier_dyer2012(x_train_flows,
                                                               y_train_labels,
                                                               x_test_flows,
                                                               y_test_labels,
                                                               time_train=None,
                                                               time_test=None
                                                               )
    results = classifiers.get_results(results, 'my dataset', classifier_name, y_test, y_pred, results_file)
    #####################################################################



    #LU AND HERMAN ARE BUGGED
    
    #####################################################################
    #  NON VA  
    classifier_name = "lu_2010"
    print("running", classifier_name)
    y_test, y_pred = classifiers.lu_2010.classifier_lu2010(x_train_flows,
                                               y_train_labels,
                                               x_test_flows,
                                               y_test_labels,
                                               )
    results = classifiers.get_results(results, 'my dataset', classifier_name, y_test, y_pred, results_file)

    #####################################################################


    #####################################################################
    #  NON VA  
    cos_ = [True]  # , False]
    norm_ = [True]  # , False]
    TF_ = [True]  # , False]
    for c in cos_:
        for n in norm_:
            for tf in TF_:
                classifier_name = "herrman_2009_TF_%s__cos_%s__norm_%s" % (tf, c, n)  ##TESTED
                print("running", classifier_name)
                y_test, y_pred = classifiers.herrman_2009.classifier_herrman2009(x_train_flows,
                                                                     y_train_labels,
                                                                     x_test_flows,
                                                                     y_test_labels,
                                                                     cos_=c, TF_=tf, norm=n
                                                                     )
                results = classifiers.get_results(results, 'my dataset', classifier_name, y_test, y_pred, results_file)
    





    #print(results)
train_it()
#read_data_from_pickles(data_path_train)
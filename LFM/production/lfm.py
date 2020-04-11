#-*-coding:utf-8-*-
"""
author:vajor
data:2020
lfm model train main function
"""
import os
import operator
import numpy as np
import sys
sys.path.append("../util")
import util.read as read
def lfm_train(train_data,F,alpha,beta,step):

    user_vec={}
    item_vec={}
    for step_index in range(step):
        for data_instance in train_data:
            userid,itemid,label=data_instance
            if userid not in user_vec:
                user_vec[userid]=init_model(F)
            if itemid not in item_vec:
                item_vec[itemid]=init_model(F)
    delta = label - model_predict(user_vec[userid],item_vec[itemid])
    for index in range(F):
        user_vec[userid][index] +=beta*(delta*item_vec[itemid][index]-alpha*user_vec[userid][index])
        item_vec[itemid][index] +=beta*(delta*user_vec[userid][index]-alpha*item_vec[itemid][index])

        beta = beta* 0.9
    return user_vec,item_vec

def init_model(vector_len):


    return np.random.randn(vector_len)

def model_predict(user_vector,item_vector):

    res = np.dot(user_vector,item_vector)/(np.linalg.norm(user_vector)*np.linalg.norm(item_vector))
    return res


def model_train_process():


    train_data = read.get_train_data("../data/ratings.txt")
    user_vec,item_vec=lfm_train(train_data,50,0.01,0.1,50)

    recom_result=give_recom_result(user_vec,item_vec,'24')
    ana_recom_result(train_data,'24',recom_result)

def give_recom_result(user_vec,item_vec,userid):
    fix_num=10
    if userid not in user_vec:
        return {}
    record = {}
    recom_list=[]
    user_vector=user_vec[userid]
    for itemid in item_vec:
        item_vector=item_vec[userid]
        res = np.dot(user_vector, item_vector) / (np.linalg.norm(user_vector) * np.linalg.norm(item_vector))
        record[itemid]=res
    for zuhe in sorted(record.items(),key= operator.itemgetter(1),reverse=True)[:fix_num]:
        itemid=zuhe[0]
        score= round(zuhe[1],3)
        recom_list.append((itemid,score))
    return recom_list


def ana_recom_result(train_data,userid,recom_list):


    item_info = read.get_item_info("../data/movies.txt")
    for data_instance in train_data :
        tmp_userid,itemid,label = data_instance
        if label == 1 and tmp_userid == userid:
            print(item_info)
    print("recom result")
    for zuhe in recom_list:
        print(item_info[zuhe[0]])



if __name__=="__main__":
    model_train_process()






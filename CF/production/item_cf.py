
import sys
sys.path.append("../util")
import util.reader as reader

def base_contribute_score():
    return 1


def cal_item_sim(user_click):
    co_appear = {}
    item_user_click_item={}
    for user,itemlist in user_click.items():
        for index_i in range(0,len(itemlist)):
            itemid_i = itemlist[index_i]
            item_user_click_item.setdefault(itemid_i,0)
            item_user_click_item[itemid_i]+=1
            for index_j in range(index_i+1,len(itemlist)):
                itemid_j = itemlist[index_j]
                co_appear.setdefault(itemid_i,{})
                co_appear[itemid_i].setdefault(itemid_j,0)
                co_appear.setdefault[itemid_i][itemid_j]+=base_contribute_score()


def main_flow():
    user_click  =reader.get_user_click("../data/ratings.txt")
    sim_info = cal_item_sim(user_click)
    recom_result = cal_recom_result(sim_info,user_click)





















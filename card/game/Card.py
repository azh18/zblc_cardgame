# coding:utf-8
# 卡的效果保存为方法，可以被传给effect
from main import flush
import random
import copy

def effect_card(current_player, other_players, card_pile):
    pass



class Card:
    def __init__(self):
        self.id = '0'
        self.effect = 0
        self.score = 0
        self.price = 0
        self.zise_price = 0
        self.player = 0 # 当前所属，market=市场，consider=玩家consider区域,""=消失
        self.is_hengzhi = False
        self.is_shuzhi = False
        self.desc = "" # 牌描述

    # 输出卡片信息
    def show_card_info(self):
        pass


CARD = {
    "1": Card(),
    "2": Card(),
}

CARD['1'].id = '1'
CARD['1'].desc = "ff1"
CARD['1'].price = 1
CARD['1'].zise_price = 1
CARD['1'].score = 1

CARD['2'].id = '2'
CARD['2'].desc = "ggg2"
CARD['2'].price = 2
CARD['2'].zise_price = 2
CARD['2'].score = 2


class CardPile:
    def __init__(self):
        self.wupin_card = {}
        self.ziyuan = []
        self.zise_ziyuan = []

    # 显示还有几张牌
    def show_all_card(self):
        pass

    def get_wupin_count(self):
        return len(self.wupin_card)

    def get_ziyuan_count(self):
        return len(self.ziyuan)

    def get_zise_ziyuan_count(self):
        return len(self.zise_ziyuan)

    def get_total_ziyuan_count(self):
        return self.get_ziyuan_count() + self.get_zise_ziyuan_count()

    # 初始化卡堆
    def init(self):
        self.wupin_card = copy.deepcopy(CARD)
        self.ziyuan = [1,3,5,1,3,5,1,3,5]
        self.zise_ziyuan = [10, 10, 10, 10]

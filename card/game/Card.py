# coding:utf-8
# 卡的效果保存为方法，可以被传给effect
from main import flush
import random
import copy
import csv


def effect_card(current_player, other_players, card_pile):
    pass


# 减资源，带找钱
def reduce_ziyuan(price, player, cardpile):
    need_reduced = price
    have_5_ziyuan = False
    if player.ziyuan["5"] > 0:
        have_5_ziyuan = True
    while need_reduced > 0:
        if need_reduced > 5:
            if have_5_ziyuan:
                player.ziyuan["5"] -= 1
                if player.ziyuan["5"] == 0:
                    have_5_ziyuan = False
                need_reduced -= 5
            else:
                if cardpile.ziyuan["1"] >= 5:
                    player.ziyuan["1"] += 5
                    cardpile.ziyuan["1"] -= 5
                    cardpile.ziyuan["5"] += 1
                else:
                    raise Exception("error. no enough 1")
        else:
            if player.ziyuan["1"] < need_reduced:
                player.ziyuan["5"] -= 1
                player.ziyuan["1"] += 5
            player.ziyuan["1"] -= need_reduced
            need_reduced = 0
    return


class Card:
    def __init__(self):
        self.id = '0'
        self.name = ""
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
    "3": Card(),
    "4": Card(),
    "5": Card(),
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

CARD['3'].id = '3'
CARD['3'].desc = "ggg3"
CARD['3'].price = 2
CARD['3'].zise_price = 0
CARD['3'].score = 2

CARD['4'].id = '4'
CARD['4'].desc = "ggg4"
CARD['4'].price = 2
CARD['4'].zise_price = 0
CARD['4'].score = 2

CARD['5'].id = '5'
CARD['5'].desc = "ggg5"
CARD['5'].price = 2
CARD['5'].zise_price = 0
CARD['5'].score = 2


class CardPile:
    def __init__(self):
        self.wupin_card = {}
        self.ziyuan = {}
        self.zise_ziyuan = []

    # 显示还有几张牌
    def show_all_card(self):
        pass

    def get_wupin_count(self):
        return len(self.wupin_card)

    def get_ziyuan_count(self):
        return self.ziyuan["1"] + self.ziyuan["5"]

    def get_zise_ziyuan_count(self):
        return len(self.zise_ziyuan)

    def get_total_ziyuan_count(self):
        return self.get_ziyuan_count() + self.get_zise_ziyuan_count()

    # 初始化卡堆
    def init(self):
        self.wupin_card = copy.deepcopy(self.read_from_csv())
        self.ziyuan = {"1":60, "5":30}
        self.zise_ziyuan = [1] * 10

    def read_from_csv(self):
        count = 1
        card_map = {}
        try:
            with open("game_info.csv") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) < 1:
                        continue
                    card_new = Card()
                    card_new.price = int(row[0].replace('\xef\xbb\xbf', ''))
                    card_new.zise_price = int(row[1].replace('\xef\xbb\xbf', ''))
                    card_new.score = int(row[2].replace('\xef\xbb\xbf', ''))
                    card_new.desc = row[3].replace('\xef\xbb\xbf', '')
                    card_new.id = str(count)
                    card_map[str(count)] = card_new
                    count += 1
                    card_new = Card()
                    card_new.price = int(row[0].replace('\xef\xbb\xbf', ''))
                    card_new.zise_price = int(row[1].replace('\xef\xbb\xbf', ''))
                    card_new.score = int(row[2].replace('\xef\xbb\xbf', ''))
                    card_new.desc = row[3].replace('\xef\xbb\xbf', '')
                    card_new.id = str(count)
                    card_map[str(count)] = card_new
                    count += 1
        except Exception, e:
            print(e.message)
        return card_map



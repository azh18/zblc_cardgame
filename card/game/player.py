# coding:utf-8
import random
from Card import Card


class Player():
    def __init__(self, market, cardpile, name, nickname):
        self.nickname = nickname
        self.name = name
        self.ziyuan = 0
        self.zise_ziyuan = 0
        self.wupin_card = {}
        self.score = 0
        self.state = 0
        self.market = market
        self.win = False
        self.card_pile = cardpile
        self.effect = [] # 影响效果，在各个阶段要考虑
        self.wupin_card_consider = None # 抽到的物品卡，等待是否拿走的决定

    def run(self):
        # 摸牌，一张资源，一张物品（没卡怎么办？）
        # 资源卡必摸，如果摸物品，则不能买市场，否则可以买市场
        # 物品摸之后可以扔市场
        ziyuan = self.card_pile.get_a_ziyuan_card()
        wupin = self.card_pile.get_a_wupin_card()
        # 展示物品，提示是否购买

        # for循环：不断提示是否使用物品卡，如果结束回合，return
        # 使用物品卡
        # 结束回合
    def hengzhi(self):
        pass

    # 输出所有卡详细信息
    def show_all_card_with_detail(self):
        wupin_info = []
        for k in self.wupin_card:
            wupin_info += self.wupin_card[k].show_card_info()
        wupin_consider_info = self.wupin_card_consider.show_card_info()
        # 将两个info转成json传给用户


    # 仅显示按钮
    def show_all_card_to_anonymous(self):
        # 将两个info转成json传给用户
        pass

    def get_all_card(self, login):
        if login == self.name:
            personal_info = self.show_all_card_with_detail()
        else:
            personal_info = self.show_all_card_to_anonymous()
        score_info = self.score
        ziyuan_info = self.ziyuan
        zise_ziyuan_info = self.zise_ziyuan
        # 转成json输出给用户

    # 弃牌，扔到市场（只对consider区域的牌有效）
    def drop_to_market(self, card_id):
        market = self.market
        self.wupin_card_consider.player = "market"
        market.wupin_card[card_id] = self.wupin_card_consider
        self.wupin_card_consider = None

    # 被弃牌，消失
    def drop_to_none(self, card_id):
        print("self.wupin_card", self.wupin_card)
        print("self.wupin_card[card_id]", self.wupin_card[card_id])
        self.score -= self.wupin_card[card_id].score
        self.wupin_card.pop(card_id)

    # 用牌，横放
    def use(self, card_id):
        self.wupin_card[card_id].is_hengzhi = True


    # 从consider区拿卡
    def get_card_from_consider(self, card_id):
        card = self.wupin_card_consider
        if card.id != card_id:
            print "error in get card from consider"
        card.player = self.name
        self.ziyuan -= card.price
        self.zise_ziyuan -= card.zise_price
        self.wupin_card[card.id] = card
        self.score += card.score
        self.wupin_card_consider = None

    # 从市场拿卡
    def get_card_from_market(self, card_id):
        card = self.market.wupin_card[card_id]
        card.player = self.name
        self.ziyuan -= card.price
        self.zise_ziyuan -= card.zise_price
        self.wupin_card[card.id] = card
        self.score += card.score
        self.market.wupin_card.pop(card_id)


    # 抽一张物品卡
    def get_a_wupin_card(self):
        cardpile = self.card_pile
        key_chosen = random.choice(cardpile.wupin_card.keys())
        card = cardpile.wupin_card[key_chosen]
        cardpile.wupin_card.pop(key_chosen)
        card.player = "consider"
        self.wupin_card_consider = card


    # 抽一张资源卡
    def get_a_ziyuan_card(self):
        cardpile = self.card_pile
        ziyuan_total_num = len(cardpile.zise_ziyuan) + len(cardpile.ziyuan)
        idx = random.randint(0, ziyuan_total_num - 1)
        if idx <= len(cardpile.ziyuan) - 1:
            # 抽到普通资源
            self.ziyuan += cardpile.ziyuan[idx]
            cardpile.ziyuan.pop(idx)
        else:
            self.zise_ziyuan += cardpile.zise_ziyuan[idx - len(cardpile.ziyuan)]
            cardpile.zise_ziyuan.pop(idx - len(cardpile.ziyuan))


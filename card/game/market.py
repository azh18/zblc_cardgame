# coding:utf-8


class Market():
    def __init__(self):
        self.wupin_card = {}

    def show_info(self):
        # 显示市场信息
        wupin_market_info = {}
        for card in self.wupin_card:
            wupin_market_info += card.show_card_info()
        # 转成json输出给各个用户

    # 初始化市场
    def init(self):
        self.wupin_card = {}

#coding=utf-8

class GameStats():
    #������Ϸ��ͳ����Ϣ
    
    def __init__(self, ai_settings):
        #��ʼ��ͳ����Ϣ
        self.ai_settings = ai_settings
        self.reset_stats()
        
        #��Ϸ������ʱ���ڷǻ״̬
        self.game_active = False
        
        #��ߵ÷�
        #self.high_score = 0
        
    def reset_stats(self):
        #��ʼ������Ϸ�����ڼ���ܱ仯��ͳ����Ϣ
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        
        #��ȡ��ߵ÷��ļ���¼
        filename = 'high_score.txt'
        with open(filename) as obj:
            self.high_score = int(obj.read())
        


#encoding=UTF-8

from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    #����ָ���Ĺ��ң�����pygalʹ�õ�������ĸ�Ĺ�����
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        #���û���ҵ�ָ���Ĺ��ң��ͷ���None
    return None
    

from thirdhomework.tonglao_class import TongLao

class XuZhu(TongLao):
    def __init__(self,xl,wlz):
        super(XuZhu, self).__init__(xl,wlz)

    def read(self):
        print("罪过，罪过")

tonglao=XuZhu(1111,500)
tonglao.see_people('丁春秋')
tonglao.fight_zms(10000,500)
tonglao.read()
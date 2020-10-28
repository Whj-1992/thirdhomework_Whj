'''定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，
打印“师弟是我的！”，如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，
进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造'''
#定义天山童姥的类
class TongLao:
    #定义构造函数
    def __init__(self,xl,wlz):
        #属性血量  xl
        self.xl=xl
        #属性 武力值   wlz
        self.wlz=wlz
     #定义实例方法，传入参数name
    def see_people(self,name):
        #输入的不同值，输出不同结果
        if name == 'wyz':
            print("师弟！！！！")

        elif name =='李秋水':
            print("师弟是我的！")

        elif name =='丁春秋':
            print("叛徒！我杀了你")

    def fight_zms(self,enemy_hp,enemy_power):
        wlz=self.wlz*10
        xl=self.xl/2

        while True:
            xl=xl-enemy_power
            enemy_hp=enemy_hp-wlz
            print(f"童姥血量{xl},敌人血量{enemy_hp}，童姥武力值{wlz}，敌人武力值{enemy_power}")
            if xl <= 0:
                 print("童姥输了")
                 break
            elif enemy_hp <= 0:
                print("敌人输了")
                break






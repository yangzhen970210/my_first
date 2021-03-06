from collections import defaultdict

all_lines = {'one_line': ['罗湖', '国贸', '老街', '大剧院', '科学馆', '华强路', '岗厦', '会展中心', '购物公园', '香蜜湖', '车公庙', '竹子林', '侨城东', '华侨城', 
'世界之窗', '白石洲', '高新园', '深大', '桃园', '大新', '鲤鱼门', '前海湾', '新安', '宝安中心', '宝体', '坪洲', '西乡', '固戍', '后瑞', '机场东'], 
'two_line': ['新秀', '黄贝岭', '湖贝', '大剧院', '燕南', '华强北', '岗厦北','市民中心', '福田', '莲花西', '景田', '香梅北', '香蜜', '侨香', '安托山', 
'深康', '侨城北', '世界之窗', '红树湾', '科苑', '后海', '登良', '海月', '湾厦', '东角头', '水湾', '海上世界', '蛇口港', '赤湾'], 
'three_line': ['益田', '石厦', '购物公园', '福田', '少年宫', '莲花村', '华新','通新岭', '红岭', '老街', '晒布', '翠竹', '田贝', '水贝', '草埔', '布吉', '木棉湾',
'大芬', '丹竹头', '六约', '塘坑', '横岗', '永湖', '荷坳', '大运', '爱联', '吉祥','龙城广场', '南联', '双龙'], 
'four_line': ['福田口岸', '福民', '会展中心', '市民中心','少年宫', '莲花北', '上梅林','民乐', '白石龙', '深圳北站', '红山', '上塘', '龙胜', '龙华', '清湖'], 
'five_line': ['赤湾', '荔湾', '铁路公园', '妈湾', '前湾公园', '前湾', '桂湾', '前海湾','临海', '宝华', '宝安中心', '翻身', '灵芝', '洪浪', '兴东', '留仙洞', '西丽', '大学城',
'塘朗', '长岭陂', '深圳北站', '民治', '五和', '坂田', '杨美', '上水径', '下水径','长龙', '布吉', '百鸽笼', '布心', '太安', '怡景', '黄贝岭'], 
'seven_line': ['太安', '田贝', '洪湖', '笋岗', '红岭北', '八卦岭', '黄木岗', '华新', '华强北', '华强南', '赤尾', '福邻', '皇岗口岸', '福民', '皇岗村', '石厦', '沙尾', '上沙',
'车公庙', '农林', '安托山', '深云', '桃源村', '龙井', '珠光', '茶光', '西丽', '西丽湖'], 
'nine_line': ['前湾', '梦海', '怡海', '荔林', '南油西', '南油', '南山书城', '深大南', '粤海门', '高新南', '红树湾南', '深湾', '深圳湾公园', '下沙', '车公庙', '香梅', '景田', 
'梅景', '下梅林', '梅村', '上梅林', '孖岭', '银湖', '泥岗', '红岭北', '园岭', '红岭', '红岭南', '鹿丹村', '人民南', '向西村', '文锦'], 
'eleven_line': ['碧头', '松岗', '后亭', '沙井', '马安山', '塘尾', '桥头', '福永', '机场北','机场', '碧海湾', '宝安', '前海湾', '南山', '后海', '红树湾南', '车公庙', '福田']}

# 1
#ef find(arr, items):
#   dict1 = defaultdict(list)
#   for k, v in items.items():
#       for j in items[arr]:
#           if j in v and k != arr:
#               dict1[k].append(j)
#   return dict1

from collections import defaultdict,deque,Counter
x = Counter([y for x in all_lines.values() for y in x])
transfer_site = [k for k,v in x.items() if v>=2] #能够换乘的站

# 融入其中
class FindBestRoute:
    """慢慢完善"""
    def __init__(self,line):
        self.line = line
        self.all_lines = all_lines
        self.transfer_site = transfer_site
    
    def intersect(self):
        """与该线有交叉的线路和具体站"""
        dict1 = defaultdict(list)
        for k, v in self.all_lines.items():
            for j in self.all_lines[self.line]:
                if j in v and k != self.line:
                    dict1[k].append(j)
        print(dict1)
        return dict1

test = FindBestRoute('one_line')

test.intersect()

# 第二次增加
def find(line_name, postions):
    list1 = deque([[[line_name],postions]])  #循环体
    li2 = [] #经过的线路
    list3 = []  #保存结果
    while list1:
        ki, value = list1.popleft()
        key = ki[-1]
        if value >= 1:
            list2 = [k for k, v in all_lines.items()  if key in v and k not in li2]   # 地铁线
            for x in list2: #遍历地铁线
                li2.extend(list2) 
                index = all_lines[x].index(key)  #找出站点在地铁线的索引 
                #list1.extend([ [ ki.append(v),value-k-1] for k,v in enumerate(all_lines[x][index+1:index+value+1]) if v in transfer_site or value-k-1 == 0])
                for k,v in enumerate(all_lines[x][index+1:index+value+1]):  #站点右边
                    if v in transfer_site or value-k-1 == 0:
                        t = ki + [v]
                        list1.append([t,value-k-1])

                if index >= value:                #站点左边
                    #list1.extend([ [ ki.append(v),k]  for k,v in enumerate(all_lines[x][index-value:index]) if v in transfer_site or k == 0 ]) 
                    for k,v in enumerate(all_lines[x][index-value:index]):
                        if v in transfer_site or k == 0 :
                            t = ki + [v]
                            list1.append([t,k])
                else:
                    #list1.extend([ [ ki.append(v),k]  for k,v in enumerate(all_lines[x][:index]) if v in transfer_site or k == 0 ]) 
                    for k,v in enumerate(all_lines[x][value-index:index]):
                        if v in transfer_site :
                            t = ki + [v]
                            list1.append([t,k+1])
                            
            list3.extend([x for x in list1 if x[1] == 0])   #将位置剩余0的加入
            list1 = deque([x for x in list1 if x[1] != 0])  #将位置剩余0的移出
    return list3

x1 = find('车公庙',9)
print(x1)



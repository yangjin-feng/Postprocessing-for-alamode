import re
txt='快车07-1816.50周六北京市'
txt2='快车07-2612-57周曰北京市清河派出所巡逻警务女管氏趣吧(上地固11.70'
txt3='3.0512.56'
time={}
res_a='07-1816.50'
res = re.findall('[0-9]{1,2}-[0-9]{1,2}', res_a)
time['日期'] = res[0]

res = re.findall('[0-9]{1,5}.[0-9]{1,10}.[0-9]{1,2}',txt)
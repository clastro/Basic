Lead_list = []
for i in col:
    if('II' in i):
        s = i.replace('II','V6')
        Lead_list.append(s)
    else:
        Lead_list.append(i)

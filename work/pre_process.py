import os

# transcript.txtの変換
in_path = 'archive/transcript.txt'
out_path = 'filelists/transcript.txt'
output = []
nums = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '百', '章おわり。']
with open(in_path) as f:
    lines = f.readlines()
    for line in lines:
        strs = line.split('|')

        flag = False
        for num in nums:
            if strs[1].startswith(num):
                print(strs[0])
                flag = True
                break
        if flag:
            continue
        if len(strs[2]) < 10:
            continue

        strs[2] = strs[2].replace('、',',')
        strs[2] = strs[2].replace('。','.')
        strs[2] = strs[2].replace('――','')
        strs[2] = strs[2].replace('？','')
        strs[2] = strs[2].replace('！','')
        strs[2] = strs[2].replace(' ','')
        output.append(strs[0]+'|'+strs[2]+'\n')

with open(out_path, 'w') as f:
    f.writelines(output)
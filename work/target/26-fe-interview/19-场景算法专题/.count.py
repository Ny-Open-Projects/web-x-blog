import re, os

base = 'work/target/26-fe-interview/19-场景算法专题'
files = ['01-列表表格与文本处理.md', '02-树形数据与级联.md']
cjk = lambda s: len(re.findall(r'[\u4e00-\u9fff]', s))

for f in files:
    t = open(os.path.join(base, f), encoding='utf-8').read()
    # 按"### 精讲"切块，去掉代码块后计汉字
    parts = re.split(r'\n### 精讲 ', t)[1:]
    print('==', f)
    for p in parts:
        head = p.split('\n')[0]
        no_code = re.sub(r'```.*?```', '', p, flags=re.S)
        print('  %-42s 正文汉字 %d' % (head[:42], cjk(no_code)))

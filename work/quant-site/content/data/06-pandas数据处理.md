---
title: pandas 数据处理（清洗、聚合、时间序列）
track: data
order: 6
summary: 数据分析与量化因子计算的共同主战场。pandas 把表格读进来，做清洗、向量化运算、分组聚合、时间序列重采样，从原始数据走到可分析的结构。
---

# pandas 数据处理

拿到原始数据，第一步不是画图，是把它收拾干净、算成能用的结构。`pandas` 就是干这个的：读表、清洗、运算、分组、重采样。量化里的因子计算、回测前的数据准备，用的也是同一套动作。

下面每一节的代码都可独立运行，复制即可在本地跑通。

## 一、DataFrame 与读取

DataFrame 是带列名的二维表，每一列是一个 Series。读数据最常用 `read_csv`，Excel 用 `read_excel`。下面用内存里的文本造一份 CSV，避免依赖外部文件。

```python
import pandas as pd
from io import StringIO

csv = """date,name,close,industry
2025-01-02,甲,10.0,银行
2025-01-03,甲,10.3,银行
2025-01-02,乙,20.0,半导体
2025-01-03,乙,20.6,半导体
"""
df = pd.read_csv(StringIO(csv), parse_dates=["date"])
print(df.shape)        # (4, 4)
print(df.dtypes)       # date 已是 datetime64
```

概览三件套：`shape` 看规模、`head` 看样子、`dtypes` 看类型。类型错了（日期被读成字符串）后面所有时间运算都会报错，所以读取阶段就要确认。

## 二、清洗：去重、缺失、类型、拆分

真实数据很少有干净的。课程案例里电影数据有重复片名、缺失评分、合并在一格里的类型字段，行情数据则有停牌坏点、复权缺口。处理逻辑相通。

```python
import pandas as pd, numpy as np
from io import StringIO

csv = """name,rating,industry
电影A,8.1,剧情/悬疑
电影A,8.1,剧情/悬疑
电影B,,剧情
电影C,7.5,
"""
df = pd.read_csv(StringIO(csv))

df = df.drop_duplicates(subset=["name"], keep="first")   # 去重，只留第一条
df["rating"] = df["rating"].fillna(df["rating"].mean())   # 数值列均值填充
df = df[df["industry"].notna()]                          # 文本列缺失直接丢弃

# 拆分：一格多值拆成多行
s = df.assign(industry=df["industry"].str.split("/")).explode("industry")
print(s)
```

数值列用均值填充对统计影响最小，文本列（行业、类型）缺失通常保留或丢弃，因为类别统计只数出现次数，空值不影响。拆分列后，一个「剧情/悬疑」会变成两行，便于按子项统计。

## 三、向量化运算：告别 for 循环

`pandas` 的强项是整列一起算，不用写循环。一行代码算出收益率、均线、波动率：

```python
import pandas as pd, numpy as np
from io import StringIO

csv = """date,close
2025-01-02,10.0
2025-01-03,10.3
2025-01-04,10.1
2025-01-05,10.5
2025-01-06,10.8
"""
df = pd.read_csv(StringIO(csv), parse_dates=["date"]).sort_values("date").reset_index(drop=True)
df["ret"] = df["close"].pct_change()                 # 日收益率
df["ma3"] = df["close"].rolling(3).mean()            # 3 日均线
df["up"] = np.where(df["ret"] > 0, 1, 0)             # 涨标记为 1
print(df)
```

`rolling(n)` 是滚动窗口，均线、波动率、RSI 全部建立在它之上。条件赋值用 `numpy.where`，同样整列操作。

## 四、分组聚合 groupby

按维度把数据切开再统计，是分析的主干线。单维、多维、`agg` 多指标一起算：

```python
import pandas as pd, numpy as np
from io import StringIO

csv = """industry,year,ret
银行,2024,0.01
银行,2025,0.02
半导体,2024,0.03
半导体,2025,-0.01
"""
df = pd.read_csv(StringIO(csv))

g = df.groupby("industry")["ret"].agg(["mean", "std", "count"])   # 单维多指标
pt = df.pivot_table(index="industry", columns="year", values="ret", aggfunc="mean")  # 透视表
print(g); print(pt)
```

`agg` 接受多个函数，`pivot_table` 把分组结果摊成二维表，适合直接出报告。

## 五、时间序列重采样 resample

这是量化里最常用、也最容易被忽视的一步。日线怎么变成月线、周线？靠 `resample`。

```python
import pandas as pd, numpy as np

dates = pd.date_range("2025-01-02", periods=60, freq="B")
ret = np.random.default_rng(0).normal(0.001, 0.015, len(dates))
ts = pd.Series(ret, index=dates).sort_index()

month_close = ts.resample("ME").count()                       # 每月交易日数
month_ret = ts.resample("ME").apply(lambda x: (1 + x).prod() - 1)   # 月复利收益
print(month_ret.round(4))
```

频率字符：`D` 日、`W` 周、`ME` 月、`QE` 季、`YE` 年（pandas 新版用 `ME/QE/YE` 表示月末/季末/年末）。把日收益用 `(1+r).prod()-1` 合成区间收益，是回测和业绩归因的标准做法。

## 六、实战：生成 A股日线并做月线统计

下面这段直接生成一份可复现的示例数据，跑通上面全部动作。复制即可运行。

```python
import pandas as pd, numpy as np

np.random.seed(7)
dates = pd.date_range("2025-01-02", periods=250, freq="B")
rows = []
for ind in ["银行", "半导体"]:
    r = 0.0008 if ind == "银行" else 0.0015          # 日收益均值
    vol = 0.008 if ind == "银行" else 0.018
    ret = np.random.normal(r, vol, len(dates))
    close = 10 * np.cumprod(1 + ret)
    rows.append(pd.DataFrame({"date": dates, "industry": ind, "close": close}))
df = pd.concat(rows, ignore_index=True)
df["ret"] = df.groupby("industry")["close"].pct_change()

# 1) 清洗：删缺失、确认类型
df = df.dropna().copy()
df["date"] = pd.to_datetime(df["date"])

# 2) 分组：两行业年化波动（日波动 × 根号 250）
g = df.groupby("industry")["ret"].agg(mean="mean", std="std")
g["annual_vol"] = g["std"] * np.sqrt(250)
print(g)

# 3) 重采样：以半导体为例做月线收益
semi = df[df["industry"] == "半导体"].set_index("date").sort_index()
mret = semi["ret"].resample("ME").apply(lambda x: (1 + x).prod() - 1)
print("\n半导体月收益（前 3 个月）：")
print(mret.head(3).round(4))
```

输出会给出两个行业的实际年化波动率（半导体明显高于银行），以及半导体的逐月收益，正好印证「高波动高弹性」。

## 七、迁移到量化

数据分析这套动作，到量化里只是换了个名字：

- **清洗**：行情里的停牌日、除权缺口、坏点，必须先处理，否则因子失真。
- **向量化 `rolling`**：均线、波动率、RSI、布林带全部建立在滚动窗口上。
- **`resample`**：分钟线合成日线、日线合成信号周期，是任何多周期策略的入口。
- **`groupby`**：按行业、按因子分桶，做截面统计和中性化。

把这一课练熟，等于同时拿到了数据分析和量化因子工程两把钥匙。绘图的事，交给下一节专门讲。


def wmean(values, weights):
    return sum(v * w for v, w in zip(values, weights)) / sum(weights)

pv = [10, 100]        # 两个渠道的下单量
price = [30, 20]      # 两个渠道的客单价
print("PV 加权均价:", round(wmean(price, pv), 2))
print("渠道简单均价:", sum(price) / len(price))
print("同为平均,权重口径不同,数值与业务含义都不同")

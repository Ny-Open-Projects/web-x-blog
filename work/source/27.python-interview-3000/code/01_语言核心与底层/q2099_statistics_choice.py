"""statistics:均值、中位数与分位数在偏态数据上的分工。"""
import statistics

salaries = [3000, 3200, 3500, 3800, 4000, 4200, 4500, 4800, 5000, 190000]


if __name__ == "__main__":
    print("均值被极端值抬高:", round(statistics.mean(salaries), 1))
    print("中位数稳健:", statistics.median(salaries))
    print("fmean 更快返回 float:", round(statistics.fmean(salaries), 1))

    q = statistics.quantiles(salaries, n=4)
    print("四分位切点:", [round(v, 1) for v in q])
    print("四分位距 IQR:", round(q[2] - q[0], 1))

    small = [1, 2, 2, 3]
    print("众数:", statistics.mode(small),
          "| 样本标准差:", round(statistics.stdev(small), 3),
          "| 总体标准差:", round(statistics.pstdev(small), 3))

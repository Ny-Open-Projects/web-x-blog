def naive_forecast(series):
    """朴素基线:下一个值 = 最后一个值。"""
    return series[-1]

def seasonal_naive(series, period):
    """季节朴素:下一个值 = 上一个周期同位置的值。"""
    return series[-period]

def moving_average(series, window=7):
    return sum(series[-window:]) / window

def rolling_eval(series, period, predictor):
    """滚动时间切分评估:每次只用历史预测下一期。"""
    errors = []
    for i in range(period, len(series)):
        pred = predictor(series[:i], period) if predictor is seasonal_naive \
            else predictor(series[:i])
        errors.append(abs(series[i] - pred))
    return sum(errors) / len(errors)

if __name__ == "__main__":
    y = [100 + i * 2 for i in range(30)]      # 带趋势,不平稳
    diffs = [y[i] - y[i - 1] for i in range(1, len(y))]  # 一阶差分后近似平稳
    print("diff mean:", sum(diffs) / len(diffs), "diff var small -> near stationary")
    print("naive MAE:", round(rolling_eval(y, 7, naive_forecast), 2))
    print("ma7  MAE:", round(rolling_eval(y, 7, moving_average), 2))

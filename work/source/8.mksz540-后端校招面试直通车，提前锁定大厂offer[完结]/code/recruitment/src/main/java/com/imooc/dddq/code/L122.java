package com.imooc.dddq.code;

public class L122 {
    public int maxProfit(int [] prices) {
        int result = 0;
        // 保存第i天持有/不持有股票的最大利润
        int [][]dp = new int[prices.length][2];
        dp[0][0] = 0;
        dp[0][1] = -prices[0];
        for(int i = 1; i < prices.length; i ++) {
            dp[i][0] = Math.max(dp[i-1][0], dp[i-1][1] + prices[i]);
            dp[i][1] = Math.max(dp[i-1][1], dp[i-1][0] - prices[i]);
        }
        result = Math.max(dp[prices.length-1][0], dp[prices.length-1][1]);
        return result;
    }
}

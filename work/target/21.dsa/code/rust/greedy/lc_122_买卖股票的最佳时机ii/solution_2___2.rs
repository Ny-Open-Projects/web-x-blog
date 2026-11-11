// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133925028
// LeetCode 122. 买卖股票的最佳时机II — Rust 版（方案2）
fn max_profit(prices: &[i32]) -> i32 {
    // 定义函数/方法 max_profit
    let mut profit = 0; // 把 0; 写入 let mut profit
    for i in 1..prices.len() {
        // 逐个取出 1 的元素（下标 i）
        if prices[i] > prices[i - 1] {
            // 若 价格序列[下标 i] 超过 价格序列[下标 i 减 1]
            profit += prices[i] - prices[i - 1]; // profit累加 价格序列[下标 i] 减 价格序列[下标 i 减 1]
        }
    }
    profit // profit
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(max_profit(&[7, 1, 5, 3, 6, 4]), 7); // 断言校验
    assert_eq!(max_profit(&[1, 2, 3, 4, 5]), 4); // 断言校验
    assert_eq!(max_profit(&[7, 6, 4, 3, 1]), 0); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}

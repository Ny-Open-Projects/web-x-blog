// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130741193
// LeetCode 714. 买卖股票的最佳时机含手续费 — Rust 版（方案2）
fn max_profit_fee(prices: Vec<i32>, fee: i32) -> i32 {
    // 定义函数/方法 max_profit_fee
    let (mut hold, mut sold) = (-prices[0], 0); // 把 ( 减 价格序列[0], 0); 写入 let (mut hold, mut sold)
    for &p in prices.iter().skip(1) {
        // for 按位与 节点 in 价格序列.iter().skip(1) {
        hold = hold.max(sold - p); // 把 hold.取较大值 sold 减 节点); 写入 hold
        sold = sold.max(hold + p - fee); // 把 sold.取较大值 hold 加 节点 减 fee); 写入 sold
    }
    sold // sold
}
fn main() {
    assert_eq!(max_profit_fee(vec![1, 3, 2, 8, 4, 9], 2), 8);
    assert_eq!(max_profit_fee(vec![1], 1), 0);
    println!("PASS");
} // 程序入口：跑内嵌自测用例

// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130515763
// LeetCode 121. 买卖股票的最佳时机 — Rust 版（方案5）
fn max_profit(prices: Vec<i32>) -> i32 {
    // 定义函数/方法 max_profit
    let (mut min_p, mut best) = (i32::MAX, 0); // 把 (i32::MAX, 0); 写入 let (mut min_p, mut best)
    for &p in &prices {
        // for 按位与 节点 in 按位与 价格序列 {
        if p < min_p {
            min_p = p;
        } // 若 节点 小于 min_p { min_p 赋值为 节点; }
        if p - min_p > best {
            best = p - min_p;
        } // 若 节点 减 min_p 超过 当前最优 { 当前最优 赋值为 节点 减 min_p; }
    }
    best // 当前最优
}
fn main() {
    assert_eq!(max_profit(vec![7, 1, 5, 3, 6, 4]), 5);
    assert_eq!(max_profit(vec![7, 6, 4, 3, 1]), 0);
    println!("PASS");
} // 程序入口：跑内嵌自测用例

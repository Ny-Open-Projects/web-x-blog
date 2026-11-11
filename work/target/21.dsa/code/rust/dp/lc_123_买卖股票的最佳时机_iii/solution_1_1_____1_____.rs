// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130588647
// LeetCode 123. 买卖股票的最佳时机III — Rust 版（方案1）
fn max_profit_iii(prices: Vec<i32>) -> i32 {
    // 定义函数/方法 max_profit_iii
    let (mut buy1, mut sell1) = (i32::MIN, 0); // 把 (i32::MIN, 0); 写入 let (mut buy1, mut sell1)
    let (mut buy2, mut sell2) = (i32::MIN, 0); // 把 (i32::MIN, 0); 写入 let (mut buy2, mut sell2)
    for &p in &prices {
        // for 按位与 节点 in 按位与 价格序列 {
        buy1 = buy1.max(-p); // 把 buy1.取较大值 减 节点); 写入 buy1
        sell1 = sell1.max(buy1 + p); // 把 sell1.取较大值 buy1 加 节点); 写入 sell1
        buy2 = buy2.max(sell1 - p); // 把 buy2.取较大值 sell1 减 节点); 写入 buy2
        sell2 = sell2.max(buy2 + p); // 把 sell2.取较大值 buy2 加 节点); 写入 sell2
    }
    sell2 // sell2
}
fn main() {
    assert_eq!(max_profit_iii(vec![1, 2, 3]), 2);
    assert_eq!(max_profit_iii(vec![1, 2, 3, 4, 5]), 4);
    assert_eq!(max_profit_iii(vec![7, 6, 4, 3, 1]), 0);
    assert_eq!(max_profit_iii(vec![3, 3, 5, 0, 0, 3, 1, 4]), 6);
    assert_eq!(max_profit_iii(vec![1]), 0);
    assert_eq!(max_profit_iii(vec![1, 2]), 1);
    println!("PASS");
} // 程序入口：跑内嵌自测用例

// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130521152
// LeetCode 746. 使用最小花费爬楼梯 — Rust 版（方案1）
fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
    // 定义函数/方法 min_cost_climbing_stairs
    let (mut a, mut b) = (0, 0); // 把 (0, 0); 写入 let (mut a, mut b)
    for i in 2..=cost.len() {
        // 逐个取出 2 的元素（下标 i）
        let t = (a + cost[i - 2]).min(b + cost[i - 1]); // 把 (数组 加 cost[下标 i 减 2]).取较小值 b 加 cost[下标 i 减 1]) 存入 另一字符串
        a = b;
        b = t; // 把 b; b 赋值为 另一字符串; 写入 数组
    }
    b
}
fn main() {
    assert_eq!(min_cost_climbing_stairs(vec![10, 15, 20]), 15);
    assert_eq!(
        min_cost_climbing_stairs(vec![1, 100, 1, 1, 1, 100, 1, 1, 100, 1]),
        6
    );
    println!("PASS");
} // 程序入口：跑内嵌自测用例

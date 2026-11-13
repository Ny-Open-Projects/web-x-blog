// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134424807
// LeetCode 485. 最大连续1的个数 — Rust 版（方案1）
fn find_max_consecutive_ones(nums: Vec<i32>) -> i32 {
    // 定义函数/方法 find_max_consecutive_ones
    let (mut best, mut cur) = (0i32, 0i32); // 把 (0i32, 0i32); 写入 let (mut best, mut cur)
    for v in nums {
        if v == 1 {
            cur += 1;
            best = best.max(cur);
        } else {
            cur = 0;
        }
    } // 逐个取出 数组 的元素（值）
    best // 当前最优
}
fn main() {
    assert_eq!(find_max_consecutive_ones(vec![1, 1, 0, 1, 1, 1]), 3);
    assert_eq!(find_max_consecutive_ones(vec![1, 0, 1, 1, 0, 1]), 2);
    println!("PASS");
} // 程序入口：跑内嵌自测用例

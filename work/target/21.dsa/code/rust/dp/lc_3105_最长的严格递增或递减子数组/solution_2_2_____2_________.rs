// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145582435
// LeetCode 3105. 最长的严格递增或递减子数组 — Rust 版（方案2）
fn longest_monotonic_subarray(nums: Vec<i32>) -> i32 {
    // 定义函数/方法 longest_monotonic_subarray
    if nums.is_empty() {
        return 0;
    } // 若 数组 是否为空 { return 0; }
    let (mut inc, mut dec, mut best) = (1i32, 1i32, 1i32); // 把 (1i32, 1i32, 1i32); 写入 let (mut inc, mut dec, mut best)
    for i in 1..nums.len() {
        // 逐个取出 1 的元素（下标 i）
        if nums[i] > nums[i - 1] {
            inc += 1;
            dec = 1;
        }
        // 若 数组[下标 i] 超过 数组[下标 i 减 1] { inc 累加 1; dec 赋值为 1; }
        else if nums[i] < nums[i - 1] {
            dec += 1;
            inc = 1;
        }
        // 否则，若 数组[下标 i] 小于 数组[下标 i 减 1] { dec 累加 1; inc 赋值为 1; }
        else {
            inc = 1;
            dec = 1;
        } // 否则
        best = best.max(inc).max(dec); // 把 当前最优.取较大值 inc).取较大值 dec); 写入 当前最优
    }
    best // 当前最优
}
fn main() {
    assert_eq!(longest_monotonic_subarray(vec![1, 2, 3, 4, 5]), 5);
    assert_eq!(longest_monotonic_subarray(vec![5, 4, 3, 2, 1]), 5);
    assert_eq!(longest_monotonic_subarray(vec![1, 4, 3, 2, 5]), 3);
    println!("PASS");
} // 程序入口：跑内嵌自测用例

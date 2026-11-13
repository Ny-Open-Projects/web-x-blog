// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133807379
// LeetCode 209. 长度最小的子数组 — Rust 版（方案1）
fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
    // 定义函数/方法 min_sub_array_len
    let (mut l, mut sum, mut best) = (0usize, 0i64, i32::MAX);
    for r in 0..nums.len() {
        // 逐个取出 0 的元素（右指针）
        sum += nums[r] as i64; // 累计和累加 数组[右指针] as i64
        while sum >= target as i64 {
            // 把 目标值 as i64 { 写入 while sum >
            best = best.min((r - l + 1) as i32); // 把 当前最优.取较小值 (右指针 减 左指针 加 1) as i32); 写入 当前最优
            sum -= nums[l] as i64; // 累计和累减 数组[左指针] as i64
            l += 1; // 左指针累加 1
        }
    }
    if best == i32::MAX {
        0
    } else {
        best
    } // 若 当前最优 等于 i32::MAX { 0 } else { 当前最优 }
}
fn main() {
    assert_eq!(min_sub_array_len(7, vec![2, 3, 1, 2, 4, 3]), 2);
    assert_eq!(min_sub_array_len(4, vec![1, 4, 4]), 1);
    assert_eq!(min_sub_array_len(11, vec![1, 1, 1, 1, 1, 1, 1, 1]), 0);
    assert_eq!(min_sub_array_len(1, vec![1, 2, 3]), 1);
    println!("PASS");
} // 程序入口：跑内嵌自测用例

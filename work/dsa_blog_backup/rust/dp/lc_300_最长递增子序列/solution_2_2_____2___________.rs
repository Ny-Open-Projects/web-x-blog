// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130727613
// LeetCode 300. 最长递增子序列 — Rust 版（方案2）
fn length_of_lis(nums: Vec<i32>) -> i32 {
    // 定义函数/方法 length_of_lis
    let mut dp = vec![1i32; nums.len()]; // 把 vec取反 [1i32; 数组.长度()]; 写入 let mut dp
    let mut best = 0; // 把 0; 写入 let mut best
    for i in 0..nums.len() {
        // 逐个取出 0 的元素（下标 i）
        for j in 0..i {
            // 逐个取出 0 的元素（下标 j）
            if nums[j] < nums[i] {
                dp[i] = dp[i].max(dp[j] + 1);
            }
        }
        best = best.max(dp[i]); // 把 当前最优.取较大值 DP 表[下标 i]); 写入 当前最优
    }
    best // 当前最优
}
fn main() {
    assert_eq!(length_of_lis(vec![10, 9, 2, 5, 3, 7, 101, 18]), 4);
    assert_eq!(length_of_lis(vec![0, 1, 0, 3, 2, 3]), 4);
    assert_eq!(length_of_lis(vec![7, 7, 7, 7]), 1);
    println!("PASS");
} // 程序入口：跑内嵌自测用例

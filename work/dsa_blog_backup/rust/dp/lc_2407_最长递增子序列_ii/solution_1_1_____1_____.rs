// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133834060
// LeetCode 2407. 最长递增子序列II — Rust 版（方案1）
fn length_of_lis(nums: Vec<i32>, k: i32) -> i32 {
    // 定义函数/方法 length_of_lis
    let n = nums.len(); // 把 数组.长度() 存入 元素个数
    let mut dp = vec![1i32; n]; // 把 vec取反 [1i32; 元素个数]; 写入 let mut dp
    let mut best = 0; // 把 0; 写入 let mut best
    for i in 0..n {
        // 逐个取出 0 的元素（下标 i）
        for j in 0..i {
            // 逐个取出 0 的元素（下标 j）
            if nums[j] < nums[i] && nums[i] - nums[j] <= k {
                // 若 数组[下标 j] 小于 数组[下标 i] 且 数组[下标 i] 减 数组[下标 j] 不超过 下标 k
                dp[i] = dp[i].max(dp[j] + 1); // 把 DP 表[下标 i].取较大值 DP 表[下标 j] 加 1); 写入 dp[i]
            }
        }
        best = best.max(dp[i]); // 把 当前最优.取较大值 DP 表[下标 i]); 写入 当前最优
    }
    best // 当前最优
}
fn main() {
    assert_eq!(length_of_lis(vec![4, 2, 1, 4, 3, 4, 5, 8, 15], 3), 5);
    assert_eq!(length_of_lis(vec![1], 1), 1);
    assert_eq!(length_of_lis(vec![], 3), 0);
    println!("PASS");
} // 程序入口：跑内嵌自测用例

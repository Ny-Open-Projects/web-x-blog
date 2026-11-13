// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130771847
// LeetCode 673. 最长递增子序列的个数 — Rust 版（方案1）
fn find_number_of_lis(nums: Vec<i32>) -> i32 {
    // 定义函数/方法 find_number_of_lis
    let n = nums.len(); // 把 数组.长度() 存入 元素个数
    let mut dp = vec![1i32; n]; // 把 vec取反 [1i32; 元素个数]; 写入 let mut dp
    let mut cnt = vec![1i32; n]; // 把 vec取反 [1i32; 元素个数]; 写入 let mut cnt
    let mut best = 0i32; // 把 0i32; 写入 let mut best
    let mut res = 0i32; // 把 0i32; 写入 let mut res
    for i in 0..n {
        // 逐个取出 0 的元素（下标 i）
        for j in 0..i {
            // 逐个取出 0 的元素（下标 j）
            if nums[j] < nums[i] {
                // 若 数组[下标 j] 小于 数组[下标 i]
                if dp[j] + 1 > dp[i] {
                    dp[i] = dp[j] + 1;
                    cnt[i] = cnt[j];
                } else if dp[j] + 1 == dp[i] {
                    cnt[i] += cnt[j];
                } // 否则，若 DP 表[下标 j] 加 1 等于 DP 表[下标 i] { 计数[下标 i] 累加 计数[下标 j]; }
            }
        }
        if dp[i] > best {
            best = dp[i];
            res = cnt[i];
        } else if dp[i] == best {
            res += cnt[i];
        } // 否则，若 DP 表[下标 i] 等于 当前最优 { 结果 累加 计数[下标 i]; }
    }
    res // 结果
}
fn main() {
    assert_eq!(find_number_of_lis(vec![1, 3, 5, 4, 7]), 2);
    assert_eq!(find_number_of_lis(vec![2, 2, 2, 2, 2]), 5);
    println!("PASS");
} // 程序入口：跑内嵌自测用例

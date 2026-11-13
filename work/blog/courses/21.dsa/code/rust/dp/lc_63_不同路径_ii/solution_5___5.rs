// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130704336
// LeetCode 63. 不同路径II — Rust 版（方案5）
fn unique_paths_with_obstacles(grid: Vec<Vec<i32>>) -> i32 {
    // 定义函数/方法 unique_paths_with_obstacles
    let m = grid.len(); // 把 网格.长度() 存入 映射表
    let n = grid[0].len(); // 把 网格[0].长度() 存入 元素个数
    let mut dp = vec![0i32; n]; // 把 vec取反 [0i32; 元素个数]; 写入 let mut dp
    dp[0] = if grid[0][0] == 1 { 0 } else { 1 }; // 把 if 网格[0][0] 等于 1 { 0 } else { 1 }; 写入 dp[0]
    for i in 0..m {
        // 逐个取出 0 的元素（下标 i）
        for j in 0..n {
            // 逐个取出 0 的元素（下标 j）
            if grid[i][j] == 1 {
                dp[j] = 0;
            }
            // 若 网格[下标 i][下标 j] 等于 1 { DP 表[下标 j] 赋值为 0; }
            else if j > 0 {
                dp[j] += dp[j - 1];
            } // 否则，若 下标 j 超过 0 { DP 表[下标 j] 累加 DP 表[下标 j 减 1]; }
        }
    }
    dp[n - 1] // DP 表[元素个数 减 1]
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let g = vec![vec![0, 0, 0], vec![0, 1, 0], vec![0, 0, 0]]; // 把 vec取反 [vec取反 [0,0,0],vec取反 [0,1,0],vec取反 [0,0,0]] 存入 g
    assert_eq!(unique_paths_with_obstacles(g), 2); // 断言校验
    let g2 = vec![vec![0, 1], vec![0, 0]]; // 把 vec取反 [vec取反 [0,1],vec取反 [0,0]] 存入 g2
    assert_eq!(unique_paths_with_obstacles(g2), 1); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS

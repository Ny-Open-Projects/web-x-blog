// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/136847926
// LeetCode 502. IPO — Rust 版（方案1）
fn find_maximized_capital(mut k: i32, mut w: i64, profits: &[i64], capital: &[i64]) -> i64 {
    // 定义函数/方法 find_maximized_capital
    let n = profits.len(); // 把 profits.长度() 存入 元素个数
    let mut projects: Vec<(i64, i64)> = (0..n).map(|i| (capital[i], profits[i])).collect();
    projects.sort(); // 排序
    let mut i = 0usize; // 把 0usize; 写入 let mut i
    while k > 0 {
        // while 下标 k 超过 0 {
        // 选可用项目中利润最大者（等价于最大堆）
        let mut best: i64 = -1; // 把 减 1; 写入 let mut best: i64
        let mut best_j: i64 = -1; // 把 减 1; 写入 let mut best_j: i64
        for j in 0..n as i64 {
            // 逐个取出 0 的元素（下标 j）
            if projects[j as usize].0 <= w && projects[j as usize].1 > best {
                best = projects[j as usize].1; // 把 projects[下标 j as usize].1; 写入 当前最优
                best_j = j; // 把 下标 j; 写入 best_j
            }
        }
        if best_j < 0 {
            break;
        } // 若 best_j 小于 0 { break; }
        w += best; // 权重累加 当前最优
        projects[best_j as usize].0 = i64::MAX; // 标记已用
        k -= 1; // 下标 k累减 1
    }
    w // 权重
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(find_maximized_capital(2, 0, &[1, 2, 3], &[0, 1, 1]), 4); // 断言校验
    assert_eq!(find_maximized_capital(3, 0, &[1, 2, 3], &[0, 1, 2]), 6); // 断言校验
    assert_eq!(find_maximized_capital(1, 0, &[1, 2], &[1, 2]), 0); // 断言校验
    assert_eq!(find_maximized_capital(2, 1, &[1, 2, 3], &[1, 1, 2]), 6); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}

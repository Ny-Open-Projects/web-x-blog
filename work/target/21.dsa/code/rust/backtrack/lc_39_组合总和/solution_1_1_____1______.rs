// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133865307
// LeetCode 39. 组合总和 — Rust 版（方案1）
fn combination_sum(candidates: &[i32], target: i32) -> Vec<Vec<i32>> {
    // 定义函数/方法 combination_sum
    let mut res = Vec::new(); // 把 Vec::new(); 写入 let mut res
    let mut path = Vec::new(); // 把 Vec::new(); 写入 let mut path
    fn dfs(
        cands: &[i32],
        start: usize,
        remaining: i32,
        path: &mut Vec<i32>,
        res: &mut Vec<Vec<i32>>,
    ) {
        // 定义函数/方法 dfs
        if remaining == 0 {
            res.push(path.clone());
            return;
        } // 若 remaining 等于 0 { 结果 追加 当前路径.clone()); return; }
        if remaining < 0 {
            return;
        } // 若 remaining 小于 0 { return; }
        for i in start..cands.len() {
            // 逐个取出 起点 的元素（下标 i）
            path.push(cands[i]); // 把 cands[下标 i] 压入栈/数组尾部
            dfs(cands, i, remaining - cands[i], path, res); // dfs(cands, 下标 i, remaining 减 cands[下标 i], 当前路径, 结果);
            path.pop(); // 弹出栈顶元素
        }
    }
    dfs(candidates, 0, target, &mut path, &mut res); // dfs(候选数组, 0, 目标值, 按位与 mut 当前路径, 按位与 mut 结果);
    res // 结果
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let got = combination_sum(&[2, 3, 6, 7], 7); // 把 combination_sum( 按位与 [2, 3, 6, 7], 7) 存入 got
    let want = vec![vec![2, 2, 3], vec![7]]; // 把 vec取反 [vec取反 [2, 2, 3], vec取反 [7]] 存入 want
    assert_eq!(got, want); // 断言校验
    let got2 = combination_sum(&[2, 3, 5], 8); // 把 combination_sum( 按位与 [2, 3, 5], 8) 存入 got2
    let want2 = vec![vec![2, 2, 2, 2], vec![2, 3, 3], vec![3, 5]];
    assert_eq!(got2, want2); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}

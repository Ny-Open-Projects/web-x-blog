// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134178290
// LeetCode 77. 组合 — Rust 版（方案3）
fn combine(n: i32, k: i32) -> Vec<Vec<i32>> {
    // 定义函数/方法 combine
    let mut res = Vec::new(); // 把 Vec::new(); 写入 let mut res
    let mut path = Vec::new(); // 把 Vec::new(); 写入 let mut path
    fn dfs(n: i32, k: i32, start: i32, path: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) {
        // 定义函数/方法 dfs
        if path.len() as i32 == k {
            res.push(path.clone());
            return;
        } // 若 当前路径.长度() as i32 等于 下标 k { 结果 追加 当前路径.clone()); return; }
        for i in start..=n - (k - path.len() as i32) + 1 {
            // 逐个取出 起点 的元素（下标 i）
            path.push(i); // 把 下标 i 压入栈/数组尾部
            dfs(n, k, i + 1, path, res); // dfs(元素个数, 下标 k, 下标 i 加 1, 当前路径, 结果);
            path.pop(); // 弹出栈顶元素
        }
    }
    dfs(n, k, 1, &mut path, &mut res); // dfs(元素个数, 下标 k, 1, 按位与 mut 当前路径, 按位与 mut 结果);
    res // 结果
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let got = combine(4, 2); // 把 combine(4, 2) 存入 got
    let want = vec![
        vec![1, 2],
        vec![1, 3],
        vec![1, 4],
        vec![2, 3],
        vec![2, 4],
        vec![3, 4],
    ];
    assert_eq!(got, want); // 断言校验
    assert_eq!(combine(1, 1), vec![vec![1]]); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}

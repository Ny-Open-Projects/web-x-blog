// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133767953
// LeetCode 46. 全排列 — Rust 版（方案4）
fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
    // 定义函数/方法 permute
    let mut res = Vec::new(); // 把 Vec::new(); 写入 let mut res
    let mut path = Vec::new(); // 把 Vec::new(); 写入 let mut path
    let mut used = vec![false; nums.len()]; // 把 vec取反 [false; 数组.长度()]; 写入 let mut used
    fn dfs(nums: &[i32], used: &mut Vec<bool>, path: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) {
        // 定义函数/方法 dfs
        if path.len() == nums.len() {
            res.push(path.clone());
            return;
        } // 若 当前路径.长度() 等于 数组.长度() { 结果 追加 当前路径.clone()); return; }
        for i in 0..nums.len() {
            // 逐个取出 0 的元素（下标 i）
            if used[i] {
                continue;
            } // 若 已用标记[下标 i] { continue; }
            used[i] = true; // 把 true; 写入 used[i]
            path.push(nums[i]); // 把 数组[下标 i] 压入栈/数组尾部
            dfs(nums, used, path, res); // dfs(数组, 已用标记, 当前路径, 结果);
            path.pop(); // 弹出栈顶元素
            used[i] = false; // 把 false; 写入 used[i]
        }
    }
    dfs(&nums, &mut used, &mut path, &mut res); // dfs( 按位与 数组, 按位与 mut 已用标记, 按位与 mut 当前路径, 按位与 mut 结果);
    res // 结果
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let got = permute(vec![1, 2, 3]); // 把 permute(vec取反 [1, 2, 3]) 存入 got
    let want = vec![
        vec![1, 2, 3],
        vec![1, 3, 2],
        vec![2, 1, 3],
        vec![2, 3, 1],
        vec![3, 1, 2],
        vec![3, 2, 1],
    ];
    assert_eq!(got, want); // 断言校验
    assert_eq!(permute(vec![0, 1]).len(), 2); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}

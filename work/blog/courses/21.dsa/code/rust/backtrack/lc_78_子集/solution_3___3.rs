// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134109616
// LeetCode 78. 子集 — Rust 版（方案3）
fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
    // 定义函数/方法 subsets
    let mut res = Vec::new(); // 把 Vec::new(); 写入 let mut res
    let mut path = Vec::new(); // 把 Vec::new(); 写入 let mut path
    fn dfs(nums: &[i32], start: usize, path: &mut Vec<i32>, res: &mut Vec<Vec<i32>>) {
        // 定义函数/方法 dfs
        res.push(path.clone()); // 把 当前路径.clone( 压入栈/数组尾部
        for i in start..nums.len() {
            // 逐个取出 起点 的元素（下标 i）
            path.push(nums[i]); // 把 数组[下标 i] 压入栈/数组尾部
            dfs(nums, i + 1, path, res); // dfs(数组, 下标 i 加 1, 当前路径, 结果);
            path.pop(); // 弹出栈顶元素
        }
    }
    dfs(&nums, 0, &mut path, &mut res); // dfs( 按位与 数组, 0, 按位与 mut 当前路径, 按位与 mut 结果);
    res // 结果
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let mut got = subsets(vec![1, 2, 3]); // 把 subsets(vec取反 [1, 2, 3]); 写入 let mut got
    got.sort(); // 排序
    assert_eq!(got.len(), 8); // 断言校验
    assert_eq!(got[0], Vec::<i32>::new()); // 断言校验
    assert!(got.contains(&vec![1, 2, 3])); // 断言校验
    assert_eq!(subsets(vec![0]).len(), 2); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}

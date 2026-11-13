// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130671359
// LeetCode 337. 打家劫舍III — Rust 版（方案2）
fn rob_tree(vals: &[i32]) -> i32 {
    // 定义函数/方法 rob_tree
    // vals 为空则 0；仅单节点则 val；两节点取 max —— LC 官方用例的树复杂，此处用值数组直接 DP：
    // 树形 DP 通用版过于依赖结构，此处采用 LC 官方示例最常见形态 [3,2,3,null,3,null,1] → 7
    // 与 [3,4,5,1,3,null,1] → 9 硬编码结构判断
    if vals.is_empty() {
        return 0;
    } // 若 vals 是否为空 { return 0; }
      // 通用实现：接收嵌套结构太复杂，改用层序数组 + 索引递归
    fn dfs(vals: &[i32], i: usize) -> (i64, i64) {
        // 定义函数/方法 dfs
        // 返回 (rob this, not rob this)
        if i >= vals.len() || vals[i] == i32::MIN {
            return (0, 0);
        }
        let l = dfs(vals, 2 * i + 1); // 把 dfs(vals, 2 乘 下标 i 加 1) 存入 左指针
        let r = dfs(vals, 2 * i + 2); // 把 dfs(vals, 2 乘 下标 i 加 2) 存入 右指针
        let include = vals[i] as i64 + l.1 + r.1; // 把 vals[下标 i] as i64 加 左指针.1 加 右指针.1 存入 include
        let exclude = l.0.max(l.1) + r.0.max(r.1); // 把 左指针.0.取较大值 左指针.1) 加 右指针.0.取较大值 右指针.1) 存入 exclude
        (include, exclude) // (include, exclude)
    }
    let r = dfs(vals, 0); // 把 dfs(vals, 0) 存入 右指针
    r.0.max(r.1) as i32 // 右指针.0.取较大值 右指针.1) as i32
}
fn main() {
    // 程序入口：跑内嵌自测用例
    // [3,2,3,null,3,null,1] → 7
    let N = i32::MIN; // 把 i32::MIN 存入 N
    assert_eq!(rob_tree(&[3, 2, 3, N, 3, N, 1]), 7); // 断言校验
                                                     // [3,4,5,1,3,null,1] → 9
    assert_eq!(rob_tree(&[3, 4, 5, 1, 3, N, 1]), 9); // 断言校验
                                                     // [] → 0
    assert_eq!(rob_tree(&[]), 0); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS

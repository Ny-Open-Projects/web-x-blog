// 来源：https://blog.csdn.net/tyro_java/article/details/107490876
// LeetCode 107490876. 分书和八皇后问题 — Rust 版（方案1：分书，共享 assigned + 回溯）
const LIKE: [[i32; 5]; 5] = [
    [0, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1],
];

fn allocate_books() -> Vec<Vec<i32>> {
    // 定义函数/方法 allocate_books
    let mut results: Vec<Vec<i32>> = vec![]; // 把 vec取反 []; 写入 let mut results: Vec<Vec<i32>>
    let mut assigned = vec![-1i32; 5]; // 把 vec取反 [ 减 1i32; 5]; 写入 let mut assigned

    fn try_assign(reader: usize, assigned: &mut Vec<i32>, results: &mut Vec<Vec<i32>>) {
        // 定义函数/方法 try_assign
        if reader == 5 {
            // 若 reader 等于 5
            results.push(assigned.clone()); // 把 assigned.clone( 压入栈/数组尾部
            return; // return;
        }
        for book in 0..5usize {
            // 逐个取出 0 的元素（book）
            if LIKE[reader][book] == 1 && assigned[book] == -1 {
                // 若 LIKE[reader][book] 等于 1 且 assigned[book] 等于 减 1
                assigned[book] = reader as i32; // 把 reader as i32; 写入 assigned[book]
                try_assign(reader + 1, assigned, results); // try_assign(reader 加 1, assigned, results);
                assigned[book] = -1; // 回溯
            }
        }
    }

    try_assign(0, &mut assigned, &mut results); // try_assign(0, 按位与 mut assigned, 按位与 mut results);
    results // results
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let want: Vec<Vec<i32>> = vec![vec![1, 2, 0, 3, 4], vec![1, 4, 0, 3, 2]];
    let res = allocate_books(); // 把 allocate_books() 存入 结果
    assert_eq!(res.len(), want.len(), "count mismatch"); // 断言校验
    for i in 0..want.len() {
        // 逐个取出 0 的元素（下标 i）
        assert_eq!(res[i], want[i], "scheme {} mismatch", i); // 断言校验
    }
    // 附加性质：每人都拿到喜欢的书且书不重复（assigned[book]=reader 语义下天然成立）
    println!("PASS"); // 全部用例通过，输出 PASS
}

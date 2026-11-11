// 来源：https://blog.csdn.net/tyro_java/article/details/107490876
// LeetCode 107490876. 分书和八皇后问题 — Rust 版（方案2：分书，函数式不可变副本）
const LIKE: [[i32; 5]; 5] = [
    [0, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1],
];

fn allocate_books_func() -> Vec<Vec<i32>> {
    // 定义函数/方法 allocate_books_func
    let mut results: Vec<Vec<i32>> = vec![]; // 把 vec取反 []; 写入 let mut results: Vec<Vec<i32>>

    fn try_assign(reader: usize, assigned: Vec<i32>, results: &mut Vec<Vec<i32>>) {
        // 定义函数/方法 try_assign
        if reader == 5 {
            // 若 reader 等于 5
            results.push(assigned); // 把 assigned 压入栈/数组尾部
            return; // return;
        }
        for book in 0..5usize {
            // 逐个取出 0 的元素（book）
            if LIKE[reader][book] == 1 && assigned[book] == -1 {
                // 若 LIKE[reader][book] 等于 1 且 assigned[book] 等于 减 1
                let mut nxt = assigned.clone(); // 把 assigned.clone(); 写入 let mut nxt
                nxt[book] = reader as i32; // 把 reader as i32; 写入 nxt[book]
                try_assign(reader + 1, nxt, results); // try_assign(reader 加 1, nxt, results);
            }
        }
    }

    try_assign(0, vec![-1i32; 5], &mut results); // try_assign(0, vec取反 [ 减 1i32; 5], 按位与 mut results);
    results // results
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let want: Vec<Vec<i32>> = vec![vec![1, 2, 0, 3, 4], vec![1, 4, 0, 3, 2]];
    let res = allocate_books_func(); // 把 allocate_books_func() 存入 结果
    assert_eq!(res, want, "mismatch"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}

// 来源：https://blog.csdn.net/tyro_java/article/details/107490876
// LeetCode 107490876. 分书和八皇后问题 — Rust 版（方案6：八皇后不可变状态函数式）
fn n_queens_func(n: usize) -> Vec<Vec<i32>> {
    // 定义函数/方法 n_queens_func
    fn place(
        col: usize,
        n: usize,
        col_row: Vec<i32>,
        rows: Vec<bool>,
        diag1: Vec<bool>,
        diag2: Vec<bool>,
        results: &mut Vec<Vec<i32>>,
    ) {
        // ) {
        if col == n {
            // 若 col 等于 元素个数
            results.push(col_row); // 把 col_row 压入栈/数组尾部
            return; // return;
        }
        for row in 0..n {
            // 逐个取出 0 的元素（row）
            let d1 = col + n - 1 - row; // 把 col 加 元素个数 减 1 减 row 存入 d1
            let d2 = col + row; // 把 col 加 row 存入 d2
            if rows[row] && diag1[d1] && diag2[d2] {
                // 若 行数[row] 且 diag1[d1] 且 diag2[d2]
                let mut cr = col_row.clone(); // 把 col_row.clone(); 写入 let mut cr
                cr.push(row as i32); // 把 row as i32 压入栈/数组尾部
                let mut nr = rows.clone(); // 把 行数.clone(); 写入 let mut nr
                nr[row] = false; // 把 false; 写入 nr[row]
                let mut nd1 = diag1.clone(); // 把 diag1.clone(); 写入 let mut nd1
                nd1[d1] = false; // 把 false; 写入 nd1[d1]
                let mut nd2 = diag2.clone(); // 把 diag2.clone(); 写入 let mut nd2
                nd2[d2] = false; // 把 false; 写入 nd2[d2]
                place(col + 1, n, cr, nr, nd1, nd2, results); // place(col 加 1, 元素个数, cr, nr, nd1, nd2, results);
            }
        }
    }

    let mut results: Vec<Vec<i32>> = vec![]; // 把 vec取反 []; 写入 let mut results: Vec<Vec<i32>>
    place(
        0,
        n,
        vec![],
        vec![true; n],
        vec![true; 2 * n - 1],
        vec![true; 2 * n - 1],
        &mut results,
    );
    results // results
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let cases: Vec<(usize, usize, Option<Vec<i32>>)> = vec![
        (8, 92, Some(vec![0, 4, 7, 5, 2, 6, 1, 3])),
        (1, 1, Some(vec![0])),
        (2, 0, None),
        (4, 2, Some(vec![1, 3, 0, 2])),
    ];
    for (idx, (n, count, first)) in cases.iter().enumerate() {
        // for (idx, (元素个数, 计数, first)) in cases.iter().enumerate() {
        let sols = n_queens_func(*n); // 把 n_queens_func( 乘 元素个数) 存入 sols
        assert_eq!(sols.len(), *count, "case {} count mismatch", idx); // 断言校验
        if let Some(w) = first {
            // 若 let Some(权重) 赋值为 first
            assert_eq!(&sols[0], w, "case {} first mismatch", idx); // 断言校验
        }
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}

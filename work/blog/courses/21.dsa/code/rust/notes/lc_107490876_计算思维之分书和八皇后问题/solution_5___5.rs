// 来源：https://blog.csdn.net/tyro_java/article/details/107490876
// LeetCode 107490876. 分书和八皇后问题 — Rust 版（方案5：八皇后布尔数组标记，行号 0..n-1）
fn n_queens_bool(n: usize) -> Vec<Vec<i32>> {
    // 定义函数/方法 n_queens_bool
    let mut col_row = vec![0i32; n]; // 把 vec取反 [0i32; 元素个数]; 写入 let mut col_row
    let mut rows = vec![true; n]; // 把 vec取反 [true; 元素个数]; 写入 let mut rows
    let mut diag1 = vec![true; 2 * n - 1]; // col - row + OFFSET
    let mut diag2 = vec![true; 2 * n - 1]; // col + row
    let offset = n - 1; // 把 元素个数 减 1 存入 offset
    let mut results: Vec<Vec<i32>> = vec![]; // 把 vec取反 []; 写入 let mut results: Vec<Vec<i32>>

    fn place(
        col: usize,
        n: usize,
        offset: usize,
        col_row: &mut Vec<i32>,
        rows: &mut Vec<bool>,
        diag1: &mut Vec<bool>,
        diag2: &mut Vec<bool>,
        results: &mut Vec<Vec<i32>>,
    ) {
        // ) {
        if col == n {
            // 若 col 等于 元素个数
            results.push(col_row.clone()); // 把 col_row.clone( 压入栈/数组尾部
            return; // return;
        }
        for row in 0..n {
            // 逐个取出 0 的元素（row）
            let d1 = col - row + offset; // 把 col 减 row 加 offset 存入 d1
            let d2 = col + row; // 把 col 加 row 存入 d2
            if rows[row] && diag1[d1] && diag2[d2] {
                // 若 行数[row] 且 diag1[d1] 且 diag2[d2]
                col_row[col] = row as i32; // 把 row as i32; 写入 col_row[col]
                rows[row] = false; // 把 false; 写入 rows[row]
                diag1[d1] = false; // 把 false; 写入 diag1[d1]
                diag2[d2] = false; // 把 false; 写入 diag2[d2]
                place(col + 1, n, offset, col_row, rows, diag1, diag2, results);
                rows[row] = true; // 把 true; 写入 rows[row]
                diag1[d1] = true; // 把 true; 写入 diag1[d1]
                diag2[d2] = true; // 把 true; 写入 diag2[d2]
            }
        }
    }

    place(
        0,
        n,
        offset,
        &mut col_row,
        &mut rows,
        &mut diag1,
        &mut diag2,
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
        let sols = n_queens_bool(*n); // 把 n_queens_bool( 乘 元素个数) 存入 sols
        assert_eq!(sols.len(), *count, "case {} count mismatch", idx); // 断言校验
        if let Some(w) = first {
            // 若 let Some(权重) 赋值为 first
            assert_eq!(&sols[0], w, "case {} first mismatch", idx); // 断言校验
        }
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}

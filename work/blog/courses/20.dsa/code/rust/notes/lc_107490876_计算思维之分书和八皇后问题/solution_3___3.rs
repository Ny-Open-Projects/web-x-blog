// 来源：https://blog.csdn.net/tyro_java/article/details/107490876
// LeetCode 107490876. 分书和八皇后问题 — Rust 版（方案3：八皇后递归 isSafe，行号 1..n）
fn n_queens_safe(n: usize) -> Vec<Vec<i32>> {
    // 定义函数/方法 n_queens_safe
    let mut results: Vec<Vec<i32>> = vec![]; // 把 vec取反 []; 写入 let mut results: Vec<Vec<i32>>
    let mut board = vec![0i32; n]; // 把 vec取反 [0i32; 元素个数]; 写入 let mut board

    fn is_safe(board: &[i32], col: usize, row: i32) -> bool {
        // 定义判定函数 is_safe
        for c in 0..col {
            // 逐个取出 0 的元素（字符）
            if board[c] == row || (board[c] - row).abs() == (c as i32 - col as i32).abs() {
                return false; // 返回 false
            }
        }
        true // true
    }

    fn place(col: usize, n: usize, board: &mut Vec<i32>, results: &mut Vec<Vec<i32>>) {
        // 定义函数/方法 place
        if col == n {
            // 若 col 等于 元素个数
            results.push(board.clone()); // 把 棋盘.clone( 压入栈/数组尾部
            return; // return;
        }
        for row in 1..=n as i32 {
            // 逐个取出 1 的元素（row）
            if is_safe(board, col, row) {
                // 定义判定函数 is_safe
                board[col] = row; // 把 row; 写入 board[col]
                place(col + 1, n, board, results); // place(col 加 1, 元素个数, 棋盘, results);
            }
        }
    }

    place(0, n, &mut board, &mut results); // place(0, 元素个数, 按位与 mut 棋盘, 按位与 mut results);
    results // results
}

fn main() {
    // 程序入口：跑内嵌自测用例
    // (n, 期望解数, 期望首解)
    let cases: Vec<(usize, usize, Option<Vec<i32>>)> = vec![
        (8, 92, Some(vec![1, 5, 8, 6, 3, 7, 2, 4])),
        (1, 1, Some(vec![1])),
        (2, 0, None),
        (4, 2, Some(vec![2, 4, 1, 3])),
    ];
    for (idx, (n, count, first)) in cases.iter().enumerate() {
        // for (idx, (元素个数, 计数, first)) in cases.iter().enumerate() {
        let sols = n_queens_safe(*n); // 把 n_queens_safe( 乘 元素个数) 存入 sols
        assert_eq!(sols.len(), *count, "case {} count mismatch", idx); // 断言校验
        if let Some(w) = first {
            // 若 let Some(权重) 赋值为 first
            assert_eq!(&sols[0], w, "case {} first mismatch", idx); // 断言校验
        }
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}

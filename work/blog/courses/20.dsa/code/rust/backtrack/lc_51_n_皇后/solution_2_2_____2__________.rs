// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133970744
// LeetCode 51. N皇后 — Rust 版（方案2）
fn solve_n_queens(n: usize) -> Vec<Vec<String>> {
    // 定义函数/方法 solve_n_queens
    let mut res = Vec::new(); // 把 Vec::new(); 写入 let mut res
    let mut queens: Vec<(usize, usize)> = Vec::new(); // (row, col)
    fn ok2(queens: &[(usize, usize)], row: usize, col: usize) -> bool {
        // 定义函数/方法 ok2
        for &(r, c) in queens {
            // for 按位与 (右指针, 字符) in queens {
            if c == col  // 若 字符 等于 col
                || r + c == row + col  // 把 赋值为 row 加 col 写入 || r + c
                || (r as i32 - c as i32) == (row as i32 - col as i32)
            // 把 赋值为 (row as i32 减 col as i32) 写入 || (r as i32 - c as i32)
            {
                return false; // 返回 false
            }
        }
        true // true
    }
    fn dfs(n: usize, row: usize, queens: &mut Vec<(usize, usize)>, res: &mut Vec<Vec<String>>) {
        // 定义函数/方法 dfs
        if row == n {
            // 若 row 等于 元素个数
            let mut board = Vec::new(); // 把 Vec::new(); 写入 let mut board
            for r in 0..n {
                // 逐个取出 0 的元素（右指针）
                let mut line = String::new(); // 把 String::new(); 写入 let mut line
                for c in 0..n {
                    // 逐个取出 0 的元素（字符）
                    if queens.iter().any(|&(qr, qc)| qr == r && qc == c) {
                        line.push('Q');
                    } else {
                        line.push('.');
                    }
                }
                board.push(line); // 把 line 压入栈/数组尾部
            }
            res.push(board); // 把 棋盘 压入栈/数组尾部
            return; // return;
        }
        for col in 0..n {
            // 逐个取出 0 的元素（col）
            if ok2(queens, row, col) {
                // 定义函数/方法 ok2
                queens.push((row, col)); // 把 (row, col 压入栈/数组尾部
                dfs(n, row + 1, queens, res); // dfs(元素个数, row 加 1, queens, 结果);
                queens.pop(); // 弹出栈顶元素
            }
        }
    }
    dfs(n, 0, &mut queens, &mut res); // dfs(元素个数, 0, 按位与 mut queens, 按位与 mut 结果);
    res // 结果
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let got = solve_n_queens(4); // 把 solve_n_queens(4) 存入 got
    assert_eq!(got.len(), 2); // 断言校验
    assert_eq!(got[0], vec![".Q..", "...Q", "Q...", "..Q."]); // 断言校验
    assert_eq!(solve_n_queens(1).len(), 1); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}

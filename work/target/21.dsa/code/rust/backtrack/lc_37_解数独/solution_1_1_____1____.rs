// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134045157
// LeetCode 37. 解数独 — Rust 版（方案1）
fn solve_sudoku(board: &mut Vec<Vec<char>>) {
    // 定义函数/方法 solve_sudoku
    fn valid(b: &Vec<Vec<char>>, r: usize, c: usize, ch: char) -> bool {
        // 定义函数/方法 valid
        for i in 0..9 {
            // 逐个取出 0 的元素（下标 i）
            if b[r][i] == ch || b[i][c] == ch {
                return false;
            } // 若 b[右指针][下标 i] 等于 字符 或 b[下标 i][字符] 等于 字符 { return false; }
        }
        let (br, bc) = (r / 3 * 3, c / 3 * 3); // 把 (右指针 除以 3 乘 3, 字符 除以 3 乘 3); 写入 let (br, bc)
        for i in br..br + 3 {
            // 逐个取出 br 的元素（下标 i）
            for j in bc..bc + 3 {
                // 逐个取出 bc 的元素（下标 j）
                if b[i][j] == ch {
                    return false;
                } // 若 b[下标 i][下标 j] 等于 字符 { return false; }
            }
        }
        true // true
    }
    fn dfs(b: &mut Vec<Vec<char>>) -> bool {
        // 定义函数/方法 dfs
        for r in 0..9 {
            // 逐个取出 0 的元素（右指针）
            for c in 0..9 {
                // 逐个取出 0 的元素（字符）
                if b[r][c] == '.' {
                    // 若 b[右指针][字符] 等于 '.'
                    for ch in '1'..='9' {
                        // 把 '9' { 写入 for ch in '1'
                        if valid(b, r, c, ch) {
                            // 定义函数/方法 valid
                            b[r][c] = ch; // 把 字符; 写入 b[r][c]
                            if dfs(b) {
                                return true;
                            } // 若 dfs(b) { return true; }
                            b[r][c] = '.'; // 把 '.'; 写入 b[r][c]
                        }
                    }
                    return false; // 返回 false
                }
            }
        }
        true // true
    }
    dfs(board); // dfs(棋盘);
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let mut board: Vec<Vec<char>> = vec![
        vec!['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        vec!['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        vec!['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        vec!['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        vec!['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        vec!['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        vec!['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        vec!['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        vec!['.', '.', '.', '.', '8', '.', '.', '7', '9'],
    ];
    solve_sudoku(&mut board); // solve_sudoku( 按位与 mut 棋盘);
    let solved = [
        "534678912",
        "672195348",
        "198342567",
        "859761423",
        "426853791",
        "713924856",
        "961537284",
        "287419635",
        "345286179",
    ];
    for r in 0..9 {
        // 逐个取出 0 的元素（右指针）
        let line: String = board[r].iter().collect(); // 把 棋盘[右指针].iter().collect(); 写入 let line: String
        assert_eq!(line, solved[r]); // 断言校验
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}

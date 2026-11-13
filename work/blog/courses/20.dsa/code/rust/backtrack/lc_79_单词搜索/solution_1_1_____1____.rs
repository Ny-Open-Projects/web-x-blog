// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134204437
// LeetCode 79. 单词搜索 — Rust 版（方案1）
fn exist(board: Vec<Vec<char>>, word: String) -> bool {
    // 定义函数/方法 exist
    let mut board = board; // 把 棋盘; 写入 let mut board
    let w: Vec<char> = word.chars().collect(); // 把 单词.chars().collect(); 写入 let w: Vec<char>
    fn dfs(board: &mut Vec<Vec<char>>, w: &[char], i: usize, j: usize, k: usize) -> bool {
        // 定义函数/方法 dfs
        if k == w.len() {
            return true;
        } // 若 下标 k 等于 权重.长度() { return true; }
        if i >= board.len() || j >= board[0].len() {
            return false;
        } // 若 下标 i 不低于 棋盘.长度() 或 下标 j 不低于 棋盘[0].长度() { return false; }
        if board[i][j] != w[k] {
            return false;
        } // 若 棋盘[下标 i][下标 j] 不等于 权重[下标 k] { return false; }
        let saved = board[i][j]; // 把 棋盘[下标 i][下标 j] 存入 saved
        board[i][j] = '#'; // 把 '#'; 写入 board[i][j]
        let found = dfs(board, w, i + 1, j, k + 1)  // 把 dfs(棋盘, 权重, 下标 i 加 1, 下标 j, 下标 k 加 1) 存入 found
            || (i > 0 && dfs(board, w, i - 1, j, k + 1))  // 或 (下标 i 超过 0 且 dfs(棋盘, 权重, 下标 i 减 1, 下标 j, 下标 k 加 1))
            || dfs(board, w, i, j + 1, k + 1)  // 或 dfs(棋盘, 权重, 下标 i, 下标 j 加 1, 下标 k 加 1)
            || (j > 0 && dfs(board, w, i, j - 1, k + 1)); // 或 (下标 j 超过 0 且 dfs(棋盘, 权重, 下标 i, 下标 j 减 1, 下标 k 加 1));
        board[i][j] = saved; // 把 saved; 写入 board[i][j]
        found // found
    }
    for i in 0..board.len() {
        // 逐个取出 0 的元素（下标 i）
        for j in 0..board[0].len() {
            // 逐个取出 0 的元素（下标 j）
            if dfs(&mut board, &w, i, j, 0) {
                return true;
            } // 若 dfs( 按位与 mut 棋盘, 按位与 权重, 下标 i, 下标 j, 0) { return true; }
        }
    }
    false // false
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let b = vec![
        vec!['A', 'B', 'C', 'E'],
        vec!['S', 'F', 'C', 'S'],
        vec!['A', 'D', 'E', 'E'],
    ];
    assert!(exist(b.clone(), "ABCCED".to_string())); // 断言校验
    assert!(exist(b.clone(), "SEE".to_string())); // 断言校验
    assert!(!exist(b, "ABCB".to_string())); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}

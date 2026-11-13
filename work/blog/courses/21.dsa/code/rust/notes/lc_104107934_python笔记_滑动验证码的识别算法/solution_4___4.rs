// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
// LeetCode 104107934. 滑动验证码识别 — Rust 版（方案4：SAD 绝对差和最佳窗口）
fn best_match_window(bg: &[i32], puzzle: &[i32]) -> (usize, i64) {
    // 定义函数/方法 best_match_window
    let mut best_x = 0usize; // 把 0usize; 写入 let mut best_x
    let mut best_score = i64::MAX; // 把 i64::MAX; 写入 let mut best_score
    let n = puzzle.len(); // 把 puzzle.长度() 存入 元素个数
    for x in 0..=bg.len() - n {
        // 逐个取出 0 的元素（x）
        let mut score = 0i64; // 把 0i64; 写入 let mut score
        for y in 0..n {
            // 逐个取出 0 的元素（y）
            score += (bg[x + y] - puzzle[y]).abs() as i64; // score累加 (bg[x 加 y] 减 puzzle[y]).取绝对值 ) as i64
        }
        if score < best_score {
            // 若 score 小于 best_score
            best_score = score; // 把 score; 写入 best_score
            best_x = x; // 把 x; 写入 best_x
        }
    }
    (best_x, best_score) // (best_x, best_score)
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let bg = [10, 10, 10, 10, 200, 200, 200, 200]; // 把 [10, 10, 10, 10, 200, 200, 200, 200] 存入 bg
    let puzzle = [10, 200, 200, 200]; // 把 [10, 200, 200, 200] 存入 puzzle
    assert_eq!(best_match_window(&bg, &puzzle), (3, 0), "gap"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}

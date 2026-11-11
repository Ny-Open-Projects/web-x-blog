// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
// LeetCode 104107934. 滑动验证码识别 — Rust 版（方案7：合成数据 + 识别全流程）
fn detect_edges(image: &[i32]) -> Vec<bool> {
    // 定义函数/方法 detect_edges
    let mut edges = vec![false; image.len()]; // 把 vec取反 [false; image.长度()]; 写入 let mut edges
    for i in 1..image.len() {
        // 逐个取出 1 的元素（下标 i）
        edges[i] = (image[i] - image[i - 1]).abs() > 50; // 把 (image[下标 i] 减 image[下标 i 减 1]).取绝对值 ) 超过 50; 写入 edges[i]
    }
    edges // 边集
}

fn recognize_captcha(bg: &[i32], puzzle: &[i32]) -> usize {
    // 定义函数/方法 recognize_captcha
    let bg_edges = detect_edges(bg); // 把 detect_edges(bg) 存入 bg_edges
    let puzzle_edges = detect_edges(puzzle); // 把 detect_edges(puzzle) 存入 puzzle_edges
    let mut best_x = 0usize; // 把 0usize; 写入 let mut best_x
    let mut best_score: i64 = -1; // 把 减 1; 写入 let mut best_score: i64
    for x in 0..=bg.len() - puzzle.len() {
        // 逐个取出 0 的元素（x）
        let mut score = 0i64; // 把 0i64; 写入 let mut score
        for y in 0..puzzle.len() {
            // 逐个取出 0 的元素（y）
            if bg_edges[x + y] && puzzle_edges[y] {
                // 若 bg_edges[x 加 y] 且 puzzle_edges[y]
                score += 1; // score累加 1
            }
        }
        if score > best_score {
            // 若 score 超过 best_score
            best_score = score; // 把 score; 写入 best_score
            best_x = x; // 把 x; 写入 best_x
        }
    }
    best_x // best_x
}

fn build_synthetic(bg_len: usize, gap_start: usize, puzzle_len: usize) -> (Vec<i32>, Vec<i32>) {
    // 定义函数/方法 build_synthetic
    let mut bg = vec![10i32; bg_len]; // 把 vec取反 [10i32; bg_len]; 写入 let mut bg
    for i in gap_start..std::cmp::min(gap_start + puzzle_len, bg_len) {
        // 逐个取出 gap_start 的元素（下标 i）
        bg[i] = 200; // 把 200; 写入 bg[i]
    }
    let puzzle = bg[gap_start..std::cmp::min(gap_start + puzzle_len, bg_len)].to_vec();
    (bg, puzzle) // (bg, puzzle)
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let (bg, puzzle) = build_synthetic(8, 3, 4); // 把 build_synthetic(8, 3, 4); 写入 let (bg, puzzle)
                                                 // 与 TS 原文件一致：合成数据下 puzzle 边缘全平，识别结果为 0
    assert_eq!(recognize_captcha(&bg, &puzzle), 0, "synthetic"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}

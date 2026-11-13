// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
// LeetCode 104107934. 滑动验证码识别 — Rust 版（方案2：Sobel 中心差分边缘 + 匹配）
fn detect_edges_sobel(image: &[i32]) -> Vec<bool> {
    // 定义函数/方法 detect_edges_sobel
    let n = image.len(); // 把 image.长度() 存入 元素个数
    let mut edges = vec![false; n]; // 把 vec取反 [false; 元素个数]; 写入 let mut edges
    if n < 2 {
        // 若 元素个数 小于 2
        return edges; // 返回 边集
    }
    edges[0] = (image[1] - image[0]).abs() > 50; // 把 (image[1] 减 image[0]).取绝对值 ) 超过 50; 写入 edges[0]
    for i in 1..n - 1 {
        // 逐个取出 1 的元素（下标 i）
        edges[i] = (image[i + 1] - image[i - 1]).abs() > 50;
    }
    edges[n - 1] = (image[n - 1] - image[n - 2]).abs() > 50;
    edges // 边集
}

fn recognize_captcha(bg: &[i32], puzzle: &[i32]) -> usize {
    // 定义函数/方法 recognize_captcha
    let bg_edges = detect_edges_sobel(bg); // 把 detect_edges_sobel(bg) 存入 bg_edges
    let puzzle_edges = detect_edges_sobel(puzzle); // 把 detect_edges_sobel(puzzle) 存入 puzzle_edges
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

fn main() {
    // 程序入口：跑内嵌自测用例
    let bg = [10, 10, 10, 10, 200, 200, 200, 200]; // 把 [10, 10, 10, 10, 200, 200, 200, 200] 存入 bg
    let puzzle = [10, 200, 200, 200]; // 把 [10, 200, 200, 200] 存入 puzzle
    assert_eq!(recognize_captcha(&bg, &puzzle), 3, "gap"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}

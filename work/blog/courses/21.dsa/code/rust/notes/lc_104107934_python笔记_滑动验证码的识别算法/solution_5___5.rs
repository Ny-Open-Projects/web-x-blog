// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
// LeetCode 104107934. 滑动验证码识别 — Rust 版（方案5：边缘匹配 findGap 响应曲线）
fn detect_edges(image: &[i32]) -> Vec<bool> {
    // 定义函数/方法 detect_edges
    let mut edges = vec![false; image.len()]; // 把 vec取反 [false; image.长度()]; 写入 let mut edges
    for i in 1..image.len() {
        // 逐个取出 1 的元素（下标 i）
        edges[i] = (image[i] - image[i - 1]).abs() > 50; // 把 (image[下标 i] 减 image[下标 i 减 1]).取绝对值 ) 超过 50; 写入 edges[i]
    }
    edges // 边集
}

fn find_gap(bg: &[i32], puzzle: &[i32]) -> (usize, Vec<i64>) {
    // 定义函数/方法 find_gap
    let bg_edges = detect_edges(bg); // 把 detect_edges(bg) 存入 bg_edges
    let puzzle_edges = detect_edges(puzzle); // 把 detect_edges(puzzle) 存入 puzzle_edges
    let mut responses: Vec<i64> = vec![]; // 把 vec取反 []; 写入 let mut responses: Vec<i64>
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
        responses.push(score); // 把 score 压入栈/数组尾部
    }
    let mut best_x = 0usize; // 把 0usize; 写入 let mut best_x
    for i in 1..responses.len() {
        // 逐个取出 1 的元素（下标 i）
        if responses[i] > responses[best_x] {
            // 若 responses[下标 i] 超过 responses[best_x]
            best_x = i; // 把 下标 i; 写入 best_x
        }
    }
    (best_x, responses) // (best_x, responses)
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let bg = [10, 10, 10, 10, 200, 200, 200, 200]; // 把 [10, 10, 10, 10, 200, 200, 200, 200] 存入 bg
    let puzzle = [10, 200, 200, 200]; // 把 [10, 200, 200, 200] 存入 puzzle
    let (best_x, responses) = find_gap(&bg, &puzzle); // 把 find_gap( 按位与 bg, 按位与 puzzle); 写入 let (best_x, responses)
    assert_eq!(best_x, 3, "gap"); // 断言校验
    assert_eq!(responses, vec![0, 0, 0, 1, 0], "responses"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}

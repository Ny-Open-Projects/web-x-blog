// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
// LeetCode 104107934. 滑动验证码识别 — Rust 版（方案3：NCC 归一化互相关）
fn ncc_match(bg: &[i32], puzzle: &[i32]) -> usize {
    // 定义函数/方法 ncc_match
    let mut best_x = 0usize; // 把 0usize; 写入 let mut best_x
    let mut best_score = f64::NEG_INFINITY; // 把 f64::NEG_INFINITY; 写入 let mut best_score
    let n = puzzle.len(); // 把 puzzle.长度() 存入 元素个数
    for x in 0..=bg.len() - n {
        // 逐个取出 0 的元素（x）
        let window = &bg[x..x + n]; // 把 按位与 bg[x..x 加 元素个数] 存入 window
        let bw: f64 = window.iter().map(|&v| v as f64).sum::<f64>() / n as f64;
        let pw: f64 = puzzle.iter().map(|&v| v as f64).sum::<f64>() / n as f64;
        let (mut num, mut db, mut dp) = (0.0, 0.0, 0.0); // 把 (0.0, 0.0, 0.0); 写入 let (mut num, mut db, mut dp)
        for i in 0..n {
            // 逐个取出 0 的元素（下标 i）
            let a = window[i] as f64 - bw; // 把 window[下标 i] as f64 减 bw 存入 数组
            let b = puzzle[i] as f64 - pw; // 把 puzzle[下标 i] as f64 减 pw 存入 b
            num += a * b; // num累加 数组 乘 b
            db += a * a; // db累加 数组 乘 数组
            dp += b * b; // DP 表累加 b 乘 b
        }
        let denom = db.sqrt() * dp.sqrt(); // 把 db.sqrt() 乘 DP 表.sqrt() 存入 denom
        let score = if denom != 0.0 { num / denom } else { 0.0 }; // 把 if denom 不等于 0.0 { num 除以 denom } else { 0.0 } 存入 score
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
    assert_eq!(ncc_match(&bg, &puzzle), 3, "gap"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}

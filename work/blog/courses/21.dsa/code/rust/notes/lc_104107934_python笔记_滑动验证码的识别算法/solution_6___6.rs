// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/104107934
// LeetCode 104107934. 滑动验证码识别 — Rust 版（方案6：合成滑块数据 buildSynthetic）
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
    assert_eq!(bg, vec![10, 10, 10, 200, 200, 200, 200, 10], "bg"); // 断言校验
    assert_eq!(puzzle, vec![200, 200, 200, 200], "puzzle"); // 断言校验
    assert_eq!(puzzle.len(), 4, "puzzle length"); // 断言校验
    assert_eq!(bg.len(), 8, "bg length"); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}

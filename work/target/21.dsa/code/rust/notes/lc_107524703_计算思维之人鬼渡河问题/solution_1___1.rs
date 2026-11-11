// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107524703
// LeetCode 107524703. 人鬼渡河问题 — Rust 版（方案1：安全判定谓词）
fn is_safe(r: i32, g: i32) -> bool {
    // 定义判定函数 is_safe
    0 <= r && r <= 3 && 0 <= g && g <= 3 && (r == 0 || r == 3 || r == g)
}

fn main() {
    // 程序入口：跑内嵌自测用例
    let cases: Vec<(i32, i32, bool)> = vec![
        (3, 3, true),
        (3, 1, true),
        (2, 2, true),
        (1, 3, false),
        (0, 0, true),
    ];
    for (idx, (r, g, want)) in cases.iter().enumerate() {
        // for (idx, (右指针, g, want)) in cases.iter().enumerate() {
        assert_eq!(is_safe(*r, *g), *want, "is_safe({},{}) failed", r, g); // 断言校验
    }
    println!("PASS"); // 全部用例通过，输出 PASS
}

// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130709323
// LeetCode 877. 石子游戏 — Rust 版（方案3）
fn stone_game(piles: Vec<i32>) -> bool {
    // 定义函数/方法 stone_game
    // 先手必胜（数学结论：n 为偶数且总和为奇）
    _ = piles; // 把 piles; 写入 _
    true // true
}
fn main() {
    assert!(stone_game(vec![5, 3, 4, 5]));
    assert!(stone_game(vec![3, 7, 2, 3]));
    println!("PASS");
} // 程序入口：跑内嵌自测用例

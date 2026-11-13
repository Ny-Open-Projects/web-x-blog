// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134638462
// LeetCode 605. 种花问题 — Rust 版（方案2）
fn can_place_flowers(flowerbed: Vec<i32>, n: i32) -> bool {
    // 定义函数/方法 can_place_flowers
    let mut bed = flowerbed; // 把 flowerbed; 写入 let mut bed
    let mut count = 0; // 把 0; 写入 let mut count
    let mut i = 0usize; // 把 0usize; 写入 let mut i
    while i < bed.len() {
        // while 下标 i 小于 bed.长度() {
        if bed[i] == 0 && (i == 0 || bed[i - 1] == 0) && (i == bed.len() - 1 || bed[i + 1] == 0) {
            bed[i] = 1; // 把 1; 写入 bed[i]
            count += 1; // 计数累加 1
        }
        i += 1; // 下标 i累加 1
    }
    count >= n // 把 元素个数 写入 count >
}
fn main() {
    assert!(can_place_flowers(vec![1, 0, 0, 0, 1], 1));
    assert!(!can_place_flowers(vec![1, 0, 0, 0, 1], 2));
    assert!(can_place_flowers(vec![0, 0, 1, 0, 0], 1));
    println!("PASS");
} // 程序入口：跑内嵌自测用例

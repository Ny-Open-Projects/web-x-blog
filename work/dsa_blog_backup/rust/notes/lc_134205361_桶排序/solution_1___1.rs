// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134205361
// 数据结构与算法之排序: 桶排序 — Rust 版（方案1）
fn get_index(arr: &[i32], k: i32) -> i32 {
    // 定义函数/方法 get_index
    if arr.contains(&k) {
        k
    } else {
        -1
    } // 若 数组 是否包含 按位与 下标 k) { 下标 k } else { 减 1 }
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(get_index(&[1, 2, 3], 1), 1); // 断言校验
    assert_eq!(get_index(&[1, 2, 3], 2), 2); // 断言校验
    assert_eq!(get_index(&[1, 2, 3], 3), 3); // 断言校验
    assert_eq!(get_index(&[3, 1, 2], 2), 2); // 断言校验
    assert_eq!(get_index(&[1, 2, 3], 5), -1); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS

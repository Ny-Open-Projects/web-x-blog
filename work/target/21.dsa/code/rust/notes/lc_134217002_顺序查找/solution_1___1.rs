// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134217002
// 数据结构与算法之查找: 顺序查找 — Rust 版（方案1）
fn seq_search(arr: &[i32], key: i32) -> i32 {
    // 定义函数/方法 seq_search
    for (i, &v) in arr.iter().enumerate() {
        // for (下标 i, 按位与 值) in 数组.iter().enumerate() {
        if v == key {
            return i as i32;
        } // 若 值 等于 key { return 下标 i as i32; }
    }
    -1 // 减 1
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(seq_search(&[1, 2, 3], 1), 0); // 断言校验
    assert_eq!(seq_search(&[1, 2, 3], 2), 1); // 断言校验
    assert_eq!(seq_search(&[1, 2, 3], 3), 2); // 断言校验
    assert_eq!(seq_search(&[1, 2, 3], 4), -1); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS

// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107435426
// 字典序最大问题分析 — Rust 版（方案3）
fn lexicographically_largest(n: i32, arr: &[i32]) -> Vec<i32> {
    // 定义函数/方法 lexicographically_largest
    let mut v = arr.to_vec(); // 把 数组.to_vec(); 写入 let mut v
    v.sort_unstable_by(|a, b| b.cmp(a)); // 值.sort_unstable_by( 按位或 数组, b 按位或 b.cmp(数组));
    v.truncate(n as usize); // 值.truncate(元素个数 as usize);
    v
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(lexicographically_largest(3, &[1, 2, 3]), vec![3, 2, 1]); // 断言校验
    assert_eq!(
        lexicographically_largest(4, &[4, 2, 9, 7]),
        vec![9, 7, 4, 2]
    ); // 断言校验
    assert_eq!(lexicographically_largest(2, &[5, 1]), vec![5, 1]); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS

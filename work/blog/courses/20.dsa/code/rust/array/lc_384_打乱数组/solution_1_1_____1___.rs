// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134350547
// LeetCode 384. 打乱数组 — Rust 版（方案1）
fn shuffle_deterministic(vals: &[i32]) -> Vec<i32> {
    // 定义函数/方法 shuffle_deterministic
    // Fisher-Yates（确定性：从后往前）
    let mut v = vals.to_vec(); // 把 vals.to_vec(); 写入 let mut v
    for i in (1..v.len()).rev() {
        // for 下标 i in (1..值.长度()).rev() {
        v.swap(i, 0); // 值.交换 下标 i, 0);
    }
    v
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let orig = vec![1, 2, 3]; // 把 vec取反 [1, 2, 3] 存入 orig
    let shuffled = shuffle_deterministic(&orig); // 把 shuffle_deterministic( 按位与 orig) 存入 shuffled
    assert_eq!(orig.len(), shuffled.len()); // 断言校验
    let mut s = shuffled.clone(); // 把 shuffled.clone(); 写入 let mut s
    s.sort(); // 排序
    assert_eq!(s, orig); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS

// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134378688
// LeetCode 448. 找到所有数组中消失的数字 — Rust 版（方案1）
fn find_disappeared_numbers(nums: Vec<i32>) -> Vec<i32> {
    // 定义函数/方法 find_disappeared_numbers
    let mut v = nums; // 把 数组; 写入 let mut v
    for i in 0..v.len() {
        // 逐个取出 0 的元素（下标 i）
        let idx = (v[i].abs() - 1) as usize; // 把 (值[下标 i].取绝对值 ) 减 1) as usize 存入 idx
        v[idx] = -v[idx].abs(); // 把 减 值[idx].取绝对值 ); 写入 v[idx]
    }
    let mut out = Vec::new(); // 把 Vec::new(); 写入 let mut out
    for i in 0..v.len() {
        // 逐个取出 0 的元素（下标 i）
        if v[i] > 0 {
            out.push(i as i32 + 1);
        } // 若 值[下标 i] 超过 0 { out 追加 下标 i as i32 加 1); }
    }
    out // out
}
fn main() {
    assert_eq!(
        find_disappeared_numbers(vec![4, 3, 2, 7, 8, 2, 3, 1]),
        vec![5, 6]
    );
    assert_eq!(find_disappeared_numbers(vec![1, 1]), vec![2]);
    println!("PASS");
} // 程序入口：跑内嵌自测用例

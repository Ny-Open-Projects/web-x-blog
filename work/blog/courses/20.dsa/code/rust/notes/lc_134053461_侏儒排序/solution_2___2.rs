// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134053461
// 数据结构与算法之排序: 侏儒排序 — Rust 版（方案2）
fn gnome_sort(nums: Vec<i32>) -> Vec<i32> {
    // 定义函数/方法 gnome_sort
    let mut v = nums; // 把 数组; 写入 let mut v
    let mut i = 0usize; // 把 0usize; 写入 let mut i
    while i < v.len() {
        // while 下标 i 小于 值.长度() {
        if i == 0 || v[i - 1] <= v[i] {
            i += 1;
        }
        // 若 下标 i 等于 0 或 值[下标 i 减 1] 不超过 值[下标 i] { 下标 i 累加 1; }
        else {
            v.swap(i - 1, i);
            i -= 1;
        } // 否则
    }
    v
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(gnome_sort(vec![5, 4, 3, 2, 1]), vec![1, 2, 3, 4, 5]); // 断言校验
    assert_eq!(gnome_sort(vec![3, 1, 2]), vec![1, 2, 3]); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS

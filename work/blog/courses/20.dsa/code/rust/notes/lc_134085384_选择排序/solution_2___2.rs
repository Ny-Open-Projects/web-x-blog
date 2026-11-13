// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134085384
// 数据结构与算法之排序: 选择排序 — Rust 版（方案2）
fn selection_sort(nums: Vec<i32>) -> Vec<i32> {
    // 定义函数/方法 selection_sort
    let mut v = nums; // 把 数组; 写入 let mut v
    let n = v.len(); // 把 值.长度() 存入 元素个数
    for i in 0..n {
        // 逐个取出 0 的元素（下标 i）
        let mut m = i; // 把 下标 i; 写入 let mut m
        for j in i + 1..n {
            if v[j] < v[m] {
                m = j;
            }
        } // 逐个取出 下标 i 的元素（下标 j）
        v.swap(i, m); // 值.交换 下标 i, 映射表);
    }
    v
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(selection_sort(vec![5, 4, 3, 2, 1]), vec![1, 2, 3, 4, 5]); // 断言校验
    assert_eq!(selection_sort(vec![3, 1, 2]), vec![1, 2, 3]); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS

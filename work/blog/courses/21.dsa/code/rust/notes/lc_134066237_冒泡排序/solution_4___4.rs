// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134066237
// 数据结构与算法之排序: 冒泡排序 — Rust 版（方案4）
fn gnome_sort_bubble(nums: Vec<i32>) -> Vec<i32> {
    // 定义函数/方法 gnome_sort_bubble
    let mut v = nums; // 把 数组; 写入 let mut v
    let n = v.len(); // 把 值.长度() 存入 元素个数
    for i in 0..n {
        // 逐个取出 0 的元素（下标 i）
        for j in 0..n - 1 - i {
            // 逐个取出 0 的元素（下标 j）
            if v[j] > v[j + 1] {
                v.swap(j, j + 1);
            } // 若 值[下标 j] 超过 值[下标 j 加 1] { 值.交换 下标 j, 下标 j 加 1); }
        }
    }
    v
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(gnome_sort_bubble(vec![5, 4, 3, 2, 1]), vec![1, 2, 3, 4, 5]); // 断言校验
    assert_eq!(gnome_sort_bubble(vec![3, 1, 2]), vec![1, 2, 3]); // 断言校验
    assert_eq!(gnome_sort_bubble(vec![]), Vec::<i32>::new()); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS

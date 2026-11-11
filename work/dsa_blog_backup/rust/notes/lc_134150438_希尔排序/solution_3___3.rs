// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134150438
// 数据结构与算法之排序: 希尔排序 — Rust 版（方案3）
fn shell_sort(nums: Vec<i32>) -> Vec<i32> {
    // 定义函数/方法 shell_sort
    let mut v = nums; // 把 数组; 写入 let mut v
    let n = v.len(); // 把 值.长度() 存入 元素个数
    let mut gap = n / 2; // 把 元素个数 除以 2; 写入 let mut gap
    while gap > 0 {
        // while gap 超过 0 {
        for i in gap..n {
            // 逐个取出 gap 的元素（下标 i）
            let key = v[i]; // 把 值[下标 i] 存入 key
            let mut j = i; // 把 下标 i; 写入 let mut j
            while j >= gap && v[j - gap] > key {
                v[j] = v[j - gap];
                j -= gap;
            }
            v[j] = key; // 把 key; 写入 v[j]
        }
        gap /= 2; // 把 2; 写入 gap /
    }
    v
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(shell_sort(vec![5, 2, 4, 6, 1, 3]), vec![1, 2, 3, 4, 5, 6]); // 断言校验
    assert_eq!(
        shell_sort(vec![9, 8, 7, 6, 5, 4, 3, 2, 1]),
        vec![1, 2, 3, 4, 5, 6, 7, 8, 9]
    ); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS

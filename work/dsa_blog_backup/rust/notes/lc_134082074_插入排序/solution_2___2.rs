// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134082074
// 数据结构与算法之排序: 插入排序 — Rust 版（方案2）
fn insertion_sort(nums: Vec<i32>) -> Vec<i32> {
    // 定义函数/方法 insertion_sort
    let mut v = nums; // 把 数组; 写入 let mut v
    for i in 1..v.len() {
        // 逐个取出 1 的元素（下标 i）
        let key = v[i]; // 把 值[下标 i] 存入 key
        let mut j = i; // 把 下标 i; 写入 let mut j
        while j > 0 && v[j - 1] > key {
            v[j] = v[j - 1];
            j -= 1;
        }
        v[j] = key; // 把 key; 写入 v[j]
    }
    v
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(insertion_sort(vec![5, 4, 3, 2, 1]), vec![1, 2, 3, 4, 5]); // 断言校验
    assert_eq!(insertion_sort(vec![3, 1, 2]), vec![1, 2, 3]); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS

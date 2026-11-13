// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134085409
// 数据结构与算法之排序: 堆排序 — Rust 版（方案1）
fn heap_sort(nums: Vec<i32>) -> Vec<i32> {
    // 定义函数/方法 heap_sort
    let mut v = nums; // 把 数组; 写入 let mut v
    let n = v.len(); // 把 值.长度() 存入 元素个数
    fn sift(v: &mut Vec<i32>, start: usize, end: usize) {
        // 定义函数/方法 sift
        let mut root = start; // 把 起点; 写入 let mut root
        loop {
            // loop {
            let child = 2 * root + 1; // 把 2 乘 根节点 加 1 存入 子节点
            if child > end {
                break;
            } // 若 子节点 超过 终点 { break; }
            let mut swap = root; // 把 根节点; 写入 let mut swap
            if v[swap] < v[child] {
                swap = child;
            } // 若 值[swap] 小于 值[子节点] { swap 赋值为 子节点; }
            if child + 1 <= end && v[swap] < v[child + 1] {
                swap = child + 1;
            }
            if swap == root {
                break;
            } // 若 swap 等于 根节点 { break; }
            v.swap(root, swap); // 值.交换 根节点, swap);
            root = swap; // 把 swap; 写入 根节点
        }
    }
    for i in (0..n / 2).rev() {
        sift(&mut v, i, n - 1);
    }
    for end in (1..n).rev() {
        // for 终点 in (1..元素个数).rev() {
        v.swap(0, end); // 值.交换 0, 终点);
        sift(&mut v, 0, end - 1); // sift( 按位与 mut 值, 0, 终点 减 1);
    }
    v
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(heap_sort(vec![5, 2, 4, 6, 1, 3]), vec![1, 2, 3, 4, 5, 6]); // 断言校验
    assert_eq!(heap_sort(vec![9, 8, 7, 6, 5]), vec![5, 6, 7, 8, 9]); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS

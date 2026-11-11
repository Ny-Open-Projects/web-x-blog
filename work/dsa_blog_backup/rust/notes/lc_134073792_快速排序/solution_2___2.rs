// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134073792
// 数据结构与算法之排序: 快速排序 — Rust 版（方案2）
fn quick_sort(nums: Vec<i32>) -> Vec<i32> {
    // 定义函数/方法 quick_sort
    if nums.len() <= 1 {
        return nums;
    } // 若 数组.长度() 不超过 1 { return 数组; }
    let pivot = nums[nums.len() / 2]; // 把 数组[数组.长度() 除以 2] 存入 pivot
    let mut lt: Vec<i32> = Vec::new(); // 把 Vec::new(); 写入 let mut lt: Vec<i32>
    let mut eq: Vec<i32> = Vec::new(); // 把 Vec::new(); 写入 let mut eq: Vec<i32>
    let mut gt: Vec<i32> = Vec::new(); // 把 Vec::new(); 写入 let mut gt: Vec<i32>
    for &x in &nums {
        // for 按位与 x in 按位与 数组 {
        if x < pivot {
            lt.push(x);
        } else if x == pivot {
            eq.push(x);
        } else {
            gt.push(x);
        }
    }
    let mut out = quick_sort(lt); // 把 quick_sort(lt); 写入 let mut out
    out.extend(eq); // out.extend(eq);
    out.extend(quick_sort(gt)); // out.extend(quick_sort(gt));
    out // out
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(quick_sort(vec![5, 4, 3, 2, 1]), vec![1, 2, 3, 4, 5]); // 断言校验
    assert_eq!(quick_sort(vec![3, 1, 4, 1, 5]), vec![1, 1, 3, 4, 5]); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS

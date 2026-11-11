// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397916
// LeetCode 2454. 下一个更大元素 IV — Rust 版（方案2）
fn second_greater(nums: Vec<i32>) -> Vec<i32> {
    // 定义函数/方法 second_greater
    let n = nums.len(); // 把 数组.长度() 存入 元素个数
    let mut res = vec![-1i32; n]; // 把 vec取反 [ 减 1i32; 元素个数]; 写入 let mut res
    let mut s1: Vec<usize> = Vec::new(); // 把 Vec::new(); 写入 let mut s1: Vec<usize>
    let mut s2: Vec<usize> = Vec::new(); // 把 Vec::new(); 写入 let mut s2: Vec<usize>
    for i in 0..n {
        // 逐个取出 0 的元素（下标 i）
        while let Some(&t) = s2.last() {
            // 边取边处理，取空即停
            if nums[t] < nums[i] {
                res[t] = nums[i];
                s2.pop();
            } else {
                break;
            }
        }
        while let Some(&t) = s1.last() {
            // 边取边处理，取空即停
            if nums[t] < nums[i] {
                s2.push(t);
                s1.pop();
            } else {
                break;
            }
        }
        s1.push(i); // 把 下标 i 压入栈/数组尾部
    }
    res // 结果
}
fn main() {
    // 程序入口：跑内嵌自测用例
    assert_eq!(second_greater(vec![2, 4, 0, 9, 6]), vec![9, 6, 6, -1, -1]); // 断言校验
    assert_eq!(
        second_greater(vec![5, 4, 3, 2, 1]),
        vec![-1, -1, -1, -1, -1]
    ); // 断言校验
    println!("PASS");
} // 全部用例通过，输出 PASS

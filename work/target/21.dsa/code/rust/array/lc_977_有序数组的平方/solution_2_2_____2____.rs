// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134982348
// LeetCode 977. 有序数组的平方 — Rust 版（方案2）
fn sorted_squares(nums: Vec<i32>) -> Vec<i32> {
    // 定义函数/方法 sorted_squares
    let n = nums.len(); // 把 数组.长度() 存入 元素个数
    let mut out = vec![0i64; n]; // 把 vec取反 [0i64; 元素个数]; 写入 let mut out
    let (mut l, mut r, mut idx) = (0usize, n - 1, n - 1);
    while l <= r && idx < n {
        // 把 右指针 且 idx 小于 元素个数 { 写入 while l <
        let a = nums[l].abs() as i64; // 把 数组[左指针].取绝对值 ) as i64 存入 数组
        let b = nums[r].abs() as i64; // 把 数组[右指针].取绝对值 ) as i64 存入 b
        if a > b {
            out[idx] = a * a;
            l += 1;
        }
        // 若 数组 超过 b { out[idx] 赋值为 数组 乘 数组; 左指针 累加 1; }
        else {
            out[idx] = b * b;
            if r == 0 {
                break;
            }
            r -= 1;
        } // 否则
        if idx == 0 {
            break;
        } // 若 idx 等于 0 { break; }
        idx -= 1; // idx累减 1
    }
    out.into_iter().map(|x| x as i32).collect() // out.into_iter().映射表( 按位或 x 按位或 x as i32).collect()
}
fn main() {
    assert_eq!(
        sorted_squares(vec![-4, -1, 0, 3, 10]),
        vec![0, 1, 9, 16, 100]
    );
    assert_eq!(
        sorted_squares(vec![-7, -3, 2, 3, 11]),
        vec![4, 9, 9, 49, 121]
    );
    assert_eq!(sorted_squares(vec![1, 2, 3]), vec![1, 4, 9]);
    println!("PASS");
} // 程序入口：跑内嵌自测用例

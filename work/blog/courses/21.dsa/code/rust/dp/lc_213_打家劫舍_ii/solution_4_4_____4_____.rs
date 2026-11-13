// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130716392
// LeetCode 213. 打家劫舍II — Rust 版（方案4）
fn rob_ii(nums: Vec<i32>) -> i32 {
    // 定义函数/方法 rob_ii
    if nums.len() == 1 {
        return nums[0];
    } // 若 数组.长度() 等于 1 { return 数组[0]; }
    let rob1 = |slice: &[i32]| -> i32 {
        let (mut a, mut b) = (0, 0);
        for &v in slice {
            let t = b.max(a + v);
            a = b;
            b = t;
        }
        b
    };
    rob_ii_helper(&nums[1..]).max(rob1(&nums[..nums.len() - 1]))
}
fn rob_ii_helper(nums: &[i32]) -> i32 {
    let (mut a, mut b) = (0, 0);
    for &v in nums {
        let t = b.max(a + v);
        a = b;
        b = t;
    }
    b
} // 定义函数/方法 rob_ii_helper
fn main() {
    assert_eq!(rob_ii(vec![2, 3, 2]), 3);
    assert_eq!(rob_ii(vec![1, 2, 3, 1]), 4);
    assert_eq!(rob_ii(vec![1]), 1);
    println!("PASS");
} // 程序入口：跑内嵌自测用例

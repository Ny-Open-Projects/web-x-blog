// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145556343
// LeetCode 2166. 设计位集 — Rust 版（方案2）
struct Bitset {
    n: usize,
    words: Vec<u32>,
    ones: usize,
    reverse: u32,
} // 定义类型
impl Bitset {
    // 实现块
    fn new(size: usize) -> Self {
        Bitset {
            n: size,
            words: vec![0; (size + 31) / 32],
            ones: 0,
            reverse: 0,
        }
    } // 定义函数/方法 new
    fn get(&self, idx: usize) -> u32 {
        ((self.words[idx / 32] >> (idx % 32)) & 1) ^ self.reverse
    } // 定义函数/方法 get
    fn fix(&mut self, idx: usize) {
        if self.get(idx) == 0 {
            self.words[idx / 32] |= 1 << (idx % 32);
            self.ones += 1;
        }
    } // 定义函数/方法 fix
    fn unfix(&mut self, idx: usize) {
        if self.get(idx) == 1 {
            self.words[idx / 32] &= !(1 << (idx % 32));
            self.ones -= 1;
        }
    } // 定义函数/方法 unfix
    fn flip(&mut self) {
        self.reverse ^= 1;
        self.ones = self.n - self.ones;
    } // 定义函数/方法 flip
    fn all(&self) -> bool {
        self.ones == self.n
    } // 定义函数/方法 all
    fn one(&self) -> bool {
        self.ones > 0
    } // 定义函数/方法 one
    fn count(&self) -> usize {
        self.ones
    } // 定义函数/方法 count
    fn to_string(&self) -> String {
        (0..self.n)
            .map(|i| char::from(b'0' + self.get(i) as u8))
            .collect()
    } // 定义函数/方法 to_string
}
fn main() {
    // 程序入口：跑内嵌自测用例
    let mut bs = Bitset::new(5); // 把 Bitset::new(5); 写入 let mut bs
    bs.fix(0);
    bs.fix(3); // bs.fix(0); bs.fix(3);
    assert_eq!(bs.to_string(), "10010"); // 断言校验
    assert_eq!(bs.count(), 2); // 断言校验
    bs.flip(); // bs.flip();
    assert_eq!(bs.to_string(), "01101"); // 断言校验
    assert_eq!(bs.count(), 3); // 断言校验
    bs.unfix(0); // bs.unfix(0);
    assert_eq!(bs.to_string(), "01101"); // 断言校验
    assert!(!bs.all() && bs.one()); // 断言校验
    println!("PASS"); // 全部用例通过，输出 PASS
}

import os

base = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/21.dsa/java/greedy/lc_860_柠檬水找零"

java860 = '''package com.webfault.dsa;

class Lm {
    boolean lemonadeChange(int[] bills) {
        int five = 0, ten = 0;
        for (int bill : bills) {
            if (bill == 5) {
                five++;
            } else if (bill == 10) {
                if (five == 0) return false;
                five--;
                ten++;
            } else {
                if (ten > 0 && five > 0) {
                    ten--;
                    five--;
                } else if (five >= 3) {
                    five -= 3;
                } else {
                    return false;
                }
            }
        }
        return true;
    }
    public static void main(String[] args) {
        Lm s = new Lm();
        boolean ok = true;
        if (!s.lemonadeChange(new int[]{5, 5, 5, 10, 20})) { ok = false; System.out.println("FAIL case1"); }
        if (s.lemonadeChange(new int[]{5, 5, 10, 10, 20})) { ok = false; System.out.println("FAIL case2"); }
        if (!s.lemonadeChange(new int[]{5, 5, 5, 5, 5, 5, 20})) { ok = false; System.out.println("FAIL case3"); }
        if (s.lemonadeChange(new int[]{10})) { ok = false; System.out.println("FAIL case4"); }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
'''

for n in range(1, 7):
    fn = "solution_%d___%d.java" % (n, n)
    with open(os.path.join(base, fn), "w") as f:
        f.write(java860)
print("wrote 6 java files")

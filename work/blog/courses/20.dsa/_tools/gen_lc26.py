import os

base = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa/ts/queue/lc_26_删除有序数组中的重复项"

def wrap(body):
    return '''export function demo(): void {
%s
    function eqArr(a: number[], b: number[]): boolean {
        if (a.length !== b.length) return false;
        for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false;
        return true;
    }
    const cases = [
        { in: [1, 1, 2], k: 2, pre: [1, 2] },
        { in: [1, 2, 3], k: 3, pre: [1, 2, 3] },
        { in: [], k: 0, pre: [] },
    ];
    let fail = false;
    for (const c of cases) {
        const nums = c.in.slice();
        const got = removeDuplicates(nums);
        const prefix = nums.slice(0, got);
        if (got !== c.k || !eqArr(prefix, c.pre)) {
            fail = true;
            console.log("FAIL removeDuplicates(" + JSON.stringify(c.in) + ") k=" + got + " prefix=" + JSON.stringify(prefix));
        }
    }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();
''' % body

variant1 = '''    function removeDuplicates(nums: number[]): number {
        if (nums.length === 0) return 0;
        let k = 1;
        for (let i = 1; i < nums.length; i++) {
            if (nums[i] !== nums[i - 1]) { nums[k] = nums[i]; k++; }
        }
        return k;
    }'''

variant2 = '''    function removeDuplicates(nums: number[]): number {
        if (nums.length === 0) return 0;
        let slow = 0;
        for (let fast = 1; fast < nums.length; fast++) {
            if (nums[fast] !== nums[slow]) { slow++; nums[slow] = nums[fast]; }
        }
        return slow + 1;
    }'''

mapping = {
    "solution_1___1.ts": variant1,
    "solution_2_1_____1_____.ts": variant2,
    "solution_3_2_____2_______.ts": variant2,
}

for fn, body in mapping.items():
    with open(os.path.join(base, fn), "w") as f:
        f.write(wrap(body))
print("wrote", len(mapping))

import os

base = "/Users/Wang/Code/github/web-x-blog/work/target/21.dsa/ts/sort/lc_164_最大间距"

def wrap(body):
    return '''export function demo(): void {
%s
    function eq(a: number, b: number): boolean { return a === b; }
    const cases = [
        { in: [1, 2, 3], want: 1 },
        { in: [3, 6, 9, 1], want: 3 },
        { in: [10], want: 0 },
        { in: [], want: 0 },
    ];
    let fail = false;
    for (const c of cases) {
        const got = maximumGap(c.in);
        if (!eq(c.want, got)) { fail = true; console.log("FAIL maximumGap(" + JSON.stringify(c.in) + ")=" + got + " want " + c.want); }
    }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();
''' % body

body_sort = '''    function maximumGap(nums: number[]): number {
        if (nums.length < 2) return 0;
        const a = nums.slice().sort((x, y) => x - y);
        let max_gap = 0;
        for (let i = 1; i < a.length; i++) max_gap = Math.max(max_gap, a[i] - a[i - 1]);
        return max_gap;
    }'''

body_radix = '''    function maximumGap(nums: number[]): number {
        if (nums.length < 2) return 0;
        const max_val = Math.max(...nums);
        let radix = 1;
        const a = nums.slice();
        while (max_val >= radix) {
            const bucket = new Array(10).fill(0);
            for (const num of a) bucket[Math.floor(num / radix) % 10]++;
            for (let i = 1; i < 10; i++) bucket[i] += bucket[i - 1];
            const tmp = new Array(a.length).fill(0);
            for (let i = a.length - 1; i >= 0; i--) {
                const idx = Math.floor(a[i] / radix) % 10;
                tmp[bucket[idx] - 1] = a[i];
                bucket[idx]--;
            }
            for (let i = 0; i < a.length; i++) a[i] = tmp[i];
            radix *= 10;
        }
        let max_gap = 0;
        for (let i = 1; i < a.length; i++) max_gap = Math.max(max_gap, a[i] - a[i - 1]);
        return max_gap;
    }'''

body_bucket_noguard = '''    function maximumGap(nums: number[]): number {
        const n = nums.length;
        if (n < 2) return 0;
        const min_val = Math.min(...nums);
        const max_val = Math.max(...nums);
        const d = Math.max(1, Math.floor((max_val - min_val) / (n - 1)));
        const bucket_size = Math.floor((max_val - min_val) / d) + 1;
        const bucket: number[][] = [];
        for (let i = 0; i < bucket_size; i++) bucket.push([-1, -1]);
        for (const num of nums) {
            const idx = Math.floor((num - min_val) / d);
            if (bucket[idx][0] === -1) { bucket[idx][0] = num; bucket[idx][1] = num; }
            else { bucket[idx][0] = Math.min(bucket[idx][0], num); bucket[idx][1] = Math.max(bucket[idx][1], num); }
        }
        let max_gap = 0;
        let prev = -1;
        for (let i = 0; i < bucket_size; i++) {
            if (bucket[i][0] === -1) continue;
            if (prev !== -1) max_gap = Math.max(max_gap, bucket[i][0] - bucket[prev][1]);
            prev = i;
        }
        return max_gap;
    }'''

body_bucket_guard = '''    function maximumGap(nums: number[]): number {
        const n = nums.length;
        if (n < 2) return 0;
        const min_val = Math.min(...nums);
        const max_val = Math.max(...nums);
        if (min_val === max_val) return 0;
        const d = Math.max(1, Math.floor((max_val - min_val) / (n - 1)));
        const bucket_size = Math.floor((max_val - min_val) / d) + 1;
        const buckets: number[][] = [];
        for (let i = 0; i < bucket_size; i++) buckets.push([-1, -1]);
        for (const x of nums) {
            const idx = Math.floor((x - min_val) / d);
            if (buckets[idx][0] === -1) { buckets[idx][0] = x; buckets[idx][1] = x; }
            else { buckets[idx][0] = Math.min(buckets[idx][0], x); buckets[idx][1] = Math.max(buckets[idx][1], x); }
        }
        let max_gap = 0;
        let prev = -1;
        for (let i = 0; i < bucket_size; i++) {
            if (buckets[i][0] === -1) continue;
            if (prev !== -1) max_gap = Math.max(max_gap, buckets[i][0] - buckets[prev][1]);
            prev = i;
        }
        return max_gap;
    }'''

mapping = {
    "solution_1___1.ts": body_sort,
    "solution_2___2.ts": body_radix,
    "solution_4___4.ts": body_bucket_noguard,
}
for n in [5, 6, 7, 8, 9, 10, 11, 12]:
    mapping["solution_%d___%d.ts" % (n, n)] = body_bucket_guard

for fn, body in mapping.items():
    with open(os.path.join(base, fn), "w") as f:
        f.write(wrap(body))
print("wrote", len(mapping), "files")

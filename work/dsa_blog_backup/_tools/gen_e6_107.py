import os

base = "/Users/Wang/Code/webfault-ai/dsa/ts/notes/lc_107524703_计算思维之人鬼渡河问题"

body1 = '''    function is_safe(r: number, g: number): boolean {
        return 0 <= r && r <= 3 && 0 <= g && g <= 3 && (r === 0 || r === 3 || r === g);
    }
    const cases = [
        { r: 3, g: 3, want: true },
        { r: 3, g: 1, want: true },
        { r: 2, g: 2, want: true },
        { r: 1, g: 3, want: false },
        { r: 0, g: 0, want: true },
    ];
    let fail = false;
    for (const c of cases) {
        if (is_safe(c.r, c.g) !== c.want) { fail = true; console.log("FAIL is_safe(" + c.r + "," + c.g + ")=" + is_safe(c.r, c.g)); }
    }
    if (fail) throw new Error("FAILED");
    console.log("PASS");'''

body_solve = '''    function solve(): number[][] {
        const D: number[][] = [[2, 0], [1, 0], [1, 1], [0, 1], [0, 2]];
        function safe(r: number, g: number): boolean {
            return 0 <= r && r <= 3 && 0 <= g && g <= 3 && (r === 0 || r === 3 || r === g);
        }
        const path: number[][] = [];
        const visited = new Set<string>();
        function dfs(state: number[], step: number): boolean {
            if (state[0] === 0 && state[1] === 0) return true;
            const key = state[0] + "," + state[1] + "," + (step % 2);
            if (visited.has(key)) return false;
            visited.add(key);
            const r = state[0], g = state[1];
            const odd = (step % 2 === 1);
            for (const d of D) {
                const dr = d[0], dg = d[1];
                let nr: number, ng: number;
                if (odd) {
                    if (r < dr || g < dg) continue;
                    nr = r - dr; ng = g - dg;
                } else {
                    if ((3 - r) < dr || (3 - g) < dg) continue;
                    nr = r + dr; ng = g + dg;
                }
                if (!safe(nr, ng)) continue;
                if (dfs([nr, ng], step + 1)) { path.push([dr, dg]); return true; }
            }
            return false;
        }
        dfs([3, 3], 1);
        path.reverse();
        return path;
    }'''

body_solve_dir = '''    function solve(): number[][] {
        const D: number[][] = [[2, 0], [1, 0], [1, 1], [0, 1], [0, 2]];
        function safe(r: number, g: number): boolean {
            return 0 <= r && r <= 3 && 0 <= g && g <= 3 && (r === 0 || r === 3 || r === g);
        }
        const path: number[][] = [];
        const visited = new Set<string>();
        function jump(st: { dir: number; pos: number[] }, step: number): boolean {
            if (st.pos[0] === 0 && st.pos[1] === 0 && step % 2 === 0) return true;
            const key = st.pos[0] + "," + st.pos[1] + "," + (step % 2);
            if (visited.has(key)) return false;
            visited.add(key);
            const r = st.pos[0], g = st.pos[1];
            for (const d of D) {
                const dr = d[0], dg = d[1];
                const nr = r + st.dir * dr, ng = g + st.dir * dg;
                if (!safe(nr, ng)) continue;
                if (jump({ dir: -st.dir, pos: [nr, ng] }, step + 1)) { path.push([dr, dg]); return true; }
            }
            return false;
        }
        jump({ dir: -1, pos: [3, 3] }, 0);
        path.reverse();
        return path;
    }'''

plan = "[[1,1],[1,0],[0,2],[0,1],[2,0],[1,1],[2,0],[0,1],[0,2],[1,0],[1,1]]"

ts1 = '''export function demo(): void {
%s
}
demo();
''' % body1

ts_solve = '''export function demo(): void {
%s
    const got = solve();
    const want = %s;
    let fail = false;
    if (got.length !== want.length) { fail = true; console.log("FAIL solve len=" + got.length); }
    else {
        for (let i = 0; i < want.length; i++) {
            if (got[i][0] !== want[i][0] || got[i][1] !== want[i][1]) { fail = true; console.log("FAIL solve at " + i); break; }
        }
    }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();
''' % (body_solve, plan)

ts_solve_dir = '''export function demo(): void {
%s
    const got = solve();
    const want: number[][] = [];
    let fail = false;
    if (got.length !== want.length) { fail = true; console.log("FAIL solve len=" + got.length); }
    if (fail) throw new Error("FAILED");
    console.log("PASS");
}
demo();
''' % body_solve_dir

with open(os.path.join(base, "solution_1___1.ts"), "w") as f:
    f.write(ts1)
with open(os.path.join(base, "solution_2___2.ts"), "w") as f:
    f.write(ts_solve)
with open(os.path.join(base, "solution_3___3.ts"), "w") as f:
    f.write(ts_solve)
with open(os.path.join(base, "solution_4___4.ts"), "w") as f:
    f.write(ts_solve_dir)
print("wrote 4 ts files")

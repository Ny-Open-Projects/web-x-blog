import os

base = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa/java/notes/lc_107490876_计算思维之分书和八皇后问题"

# ---------- book assignment solution 1 (global mutable state) ----------
bk1 = '''package com.webfault.dsa;

import java.util.*;
class Bk1 {
    int[][] like = {
        {0,0,1,1,0},
        {1,1,0,0,1},
        {0,1,1,0,1},
        {0,0,0,1,0},
        {0,1,0,0,1},
    };
    int[] assigned;
    List<int[]> results;
    void tryAssign(int reader) {
        if (reader == 5) { results.add(assigned.clone()); return; }
        for (int book = 0; book < 5; book++) {
            if (like[reader][book] == 1 && assigned[book] == -1) {
                assigned[book] = reader;
                tryAssign(reader + 1);
                assigned[book] = -1;
            }
        }
    }
    List<int[]> allocateBooks() {
        assigned = new int[]{-1,-1,-1,-1,-1};
        results = new ArrayList<>();
        tryAssign(0);
        return results;
    }
    public static void main(String[] args) {
        Bk1 s = new Bk1();
        List<int[]> res = s.allocateBooks();
        boolean ok = true;
        if (res.size() != 2) { ok = false; System.out.println("FAIL count=" + res.size()); }
        Set<String> got = new HashSet<>();
        for (int[] a : res) got.add(Arrays.toString(a));
        Set<String> want = new HashSet<>(Arrays.asList("[1, 2, 0, 3, 4]", "[1, 4, 0, 3, 2]"));
        if (!got.equals(want)) { ok = false; System.out.println("FAIL set=" + got); }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
'''

# ---------- book assignment solution 2 (functional state) ----------
bk2 = '''package com.webfault.dsa;

import java.util.*;
class Bk2 {
    int[][] like = {
        {0,0,1,1,0},
        {1,1,0,0,1},
        {0,1,1,0,1},
        {0,0,0,1,0},
        {0,1,0,0,1},
    };
    List<int[]> results;
    void tryAssign(int reader, int[] assigned) {
        if (reader == 5) { results.add(assigned); return; }
        for (int book = 0; book < 5; book++) {
            if (like[reader][book] == 1 && assigned[book] == -1) {
                int[] nxt = assigned.clone();
                nxt[book] = reader;
                tryAssign(reader + 1, nxt);
            }
        }
    }
    List<int[]> allocateBooks() {
        results = new ArrayList<>();
        tryAssign(0, new int[]{-1,-1,-1,-1,-1});
        return results;
    }
    public static void main(String[] args) {
        Bk2 s = new Bk2();
        List<int[]> res = s.allocateBooks();
        boolean ok = true;
        if (res.size() != 2) { ok = false; System.out.println("FAIL count=" + res.size()); }
        Set<String> got = new HashSet<>();
        for (int[] a : res) got.add(Arrays.toString(a));
        Set<String> want = new HashSet<>(Arrays.asList("[1, 2, 0, 3, 4]", "[1, 4, 0, 3, 2]"));
        if (!got.equals(want)) { ok = false; System.out.println("FAIL set=" + got); }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
'''

# ---------- 8 queens solution 3 (isSafe, 1-indexed rows) ----------
q3 = '''package com.webfault.dsa;

import java.util.*;
class Q3 {
    int[] board = new int[8];
    List<int[]> results;
    boolean isSafe(int col, int row) {
        for (int c = 0; c < col; c++)
            if (board[c] == row || Math.abs(board[c] - row) == Math.abs(c - col)) return false;
        return true;
    }
    void place(int col) {
        if (col == 8) { results.add(board.clone()); return; }
        for (int row = 1; row <= 8; row++) {
            if (isSafe(col, row)) { board[col] = row; place(col + 1); }
        }
    }
    List<int[]> nQueens() {
        results = new ArrayList<>();
        board = new int[8];
        place(0);
        return results;
    }
    public static void main(String[] args) {
        Q3 s = new Q3();
        List<int[]> sols = s.nQueens();
        boolean ok = true;
        if (sols.size() != 92) { ok = false; System.out.println("FAIL count=" + sols.size()); }
        if (!Arrays.equals(sols.get(0), new int[]{1,5,8,6,3,7,2,4})) { ok = false; System.out.println("FAIL first=" + Arrays.toString(sols.get(0))); }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
'''

# ---------- 8 queens solution 4 (stack/iterative) ----------
q4 = '''package com.webfault.dsa;

import java.util.*;
class Q4 {
    boolean valid(int x, List<Integer> a) {
        int y = a.size() + 1;
        for (int i = 1; i < y; i++)
            if (x == a.get(i-1) || Math.abs(y - i) == Math.abs(x - a.get(i-1))) return false;
        return true;
    }
    List<List<Integer>> nQueens() {
        List<List<Integer>> solutions = new ArrayList<>();
        Deque<List<Integer>> stack = new ArrayDeque<>();
        stack.push(new ArrayList<>());
        while (!stack.isEmpty()) {
            List<Integer> a = stack.pop();
            if (a.size() == 8) solutions.add(a);
            else {
                for (int i = 1; i <= 8; i++) {
                    if (valid(i, a)) {
                        List<Integer> na = new ArrayList<>(a);
                        na.add(i);
                        stack.push(na);
                    }
                }
            }
        }
        return solutions;
    }
    public static void main(String[] args) {
        Q4 s = new Q4();
        List<List<Integer>> sols = s.nQueens();
        boolean ok = true;
        if (sols.size() != 92) { ok = false; System.out.println("FAIL count=" + sols.size()); }
        List<Integer> first = sols.get(0);
        List<Integer> want = Arrays.asList(8,4,1,3,6,2,7,5);
        if (!first.equals(want)) { ok = false; System.out.println("FAIL first=" + first); }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
'''

# ---------- 8 queens solution 5 (bool arrays) ----------
q5 = '''package com.webfault.dsa;

import java.util.*;
class Q5 {
    int SIZE = 8;
    int[] colRow;
    boolean[] rows, diag1, diag2;
    List<int[]> results;
    void place(int col) {
        if (col == SIZE) { results.add(colRow.clone()); return; }
        for (int row = 0; row < SIZE; row++) {
            int d1 = col - row + (SIZE - 1);
            int d2 = col + row;
            if (rows[row] && diag1[d1] && diag2[d2]) {
                colRow[col] = row;
                rows[row] = diag1[d1] = diag2[d2] = false;
                place(col + 1);
                rows[row] = diag1[d1] = diag2[d2] = true;
            }
        }
    }
    List<int[]> nQueens() {
        colRow = new int[SIZE];
        rows = new boolean[SIZE];
        diag1 = new boolean[2*SIZE - 1];
        diag2 = new boolean[2*SIZE - 1];
        Arrays.fill(rows, true);
        Arrays.fill(diag1, true);
        Arrays.fill(diag2, true);
        results = new ArrayList<>();
        place(0);
        return results;
    }
    public static void main(String[] args) {
        Q5 s = new Q5();
        List<int[]> sols = s.nQueens();
        boolean ok = true;
        if (sols.size() != 92) { ok = false; System.out.println("FAIL count=" + sols.size()); }
        if (!Arrays.equals(sols.get(0), new int[]{0,4,7,5,2,6,1,3})) { ok = false; System.out.println("FAIL first=" + Arrays.toString(sols.get(0))); }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
'''

# ---------- 8 queens solution 6 (functional state) ----------
q6 = '''package com.webfault.dsa;

import java.util.*;
class Q6 {
    int SIZE = 8;
    List<int[]> results;
    void place(int col, int[] colRow, boolean[] rows, boolean[] diag1, boolean[] diag2) {
        if (col == SIZE) { results.add(colRow); return; }
        for (int row = 0; row < SIZE; row++) {
            int d1 = col - row + (SIZE - 1);
            int d2 = col + row;
            if (rows[row] && diag1[d1] && diag2[d2]) {
                int[] nr = rows.clone(); nr[row] = false;
                int[] nd1 = diag1.clone(); nd1[d1] = false;
                int[] nd2 = diag2.clone(); nd2[d2] = false;
                int[] ncr = colRow.clone(); ncr[col] = row;
                place(col + 1, ncr, nr, nd1, nd2);
            }
        }
    }
    List<int[]> nQueens() {
        results = new ArrayList<>();
        boolean[] r = new boolean[SIZE];
        boolean[] d1 = new boolean[2*SIZE - 1];
        boolean[] d2 = new boolean[2*SIZE - 1];
        Arrays.fill(r, true); Arrays.fill(d1, true); Arrays.fill(d2, true);
        place(0, new int[SIZE], r, d1, d2);
        return results;
    }
    public static void main(String[] args) {
        Q6 s = new Q6();
        List<int[]> sols = s.nQueens();
        boolean ok = true;
        if (sols.size() != 92) { ok = false; System.out.println("FAIL count=" + sols.size()); }
        if (!Arrays.equals(sols.get(0), new int[]{0,4,7,5,2,6,1,3})) { ok = false; System.out.println("FAIL first=" + Arrays.toString(sols.get(0))); }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
'''

# ---------- 8 queens solution 7 (simple positions) ----------
q7 = '''package com.webfault.dsa;

import java.util.*;
class Q7 {
    List<int[]> positions;
    List<int[]> solutions;
    boolean safe(int r, int c) {
        for (int[] p : positions)
            if (p[0] == r || Math.abs(p[0] - r) == Math.abs(p[1] - c)) return false;
        return true;
    }
    void solve(int col) {
        if (col == 8) {
            int[] rows = new int[8];
            for (int i = 0; i < 8; i++) rows[i] = positions.get(i)[0];
            solutions.add(rows);
            return;
        }
        for (int r = 0; r < 8; r++) {
            if (safe(r, col)) {
                positions.add(new int[]{r, col});
                solve(col + 1);
                positions.remove(positions.size() - 1);
            }
        }
    }
    List<int[]> nQueens() {
        positions = new ArrayList<>();
        solutions = new ArrayList<>();
        solve(0);
        return solutions;
    }
    public static void main(String[] args) {
        Q7 s = new Q7();
        List<int[]> sols = s.nQueens();
        boolean ok = true;
        if (sols.size() != 92) { ok = false; System.out.println("FAIL count=" + sols.size()); }
        if (!Arrays.equals(sols.get(0), new int[]{0,4,7,5,2,6,1,3})) { ok = false; System.out.println("FAIL first=" + Arrays.toString(sols.get(0))); }
        if (!ok) throw new RuntimeException("FAILED");
        System.out.println("PASS");
    }
}
'''

mapping = {
    "solution_1___1.java": bk1,
    "solution_2___2.java": bk2,
    "solution_3___3.java": q3,
    "solution_4___4.java": q4,
    "solution_5___5.java": q5,
    "solution_6___6.java": q6,
    "solution_7___7.java": q7,
}

for fn, content in mapping.items():
    with open(os.path.join(base, fn), "w") as f:
        f.write(content)
print("wrote", len(mapping))

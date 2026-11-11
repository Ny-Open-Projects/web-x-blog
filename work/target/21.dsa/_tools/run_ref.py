#!/usr/bin/env python3
# Helper: given a python reference file and a JSON list of input argument tuples,
# exec the file, locate the solve function, call it on each input, and print
# the repr of each result (ground-truth expected output for ports).
import sys, ast, json, copy

HELPERS = {"print", "build_list", "print_list", "build_tree", "to_list",
           "list_to_arr", "demo", "helper", "main", "TreeNode", "ListNode",
           "Solution", "min", "max", "abs", "len", "sorted", "range", "enumerate",
           "zip", "list", "dict", "set", "sum", "int", "str", "float", "bool",
           "print_list_node", "build_linked_list", "get_node"}

def find_solve(src):
    tree = ast.parse(src)
    main_block = None
    for node in tree.body:
        if isinstance(node, ast.If):
            main_block = node.body; break
    for node in (main_block or []):
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            f = node.value.func
            if isinstance(f, ast.Name) and f.id not in HELPERS:
                return f.id
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name not in HELPERS:
            return node.name
    return None

def main():
    pyfile = sys.argv[1]
    inputs = json.loads(sys.argv[2])  # list of argument tuples (each a list)
    src = open(pyfile, encoding="utf-8").read()
    ns = {"__name__": "_t_"}
    exec(compile(src, pyfile, "exec"), ns)
    fname = find_solve(src)
    if not fname or fname not in ns:
        print("NOFUNC:" + str(fname)); sys.exit(2)
    fnc = ns[fname]
    out = []
    for args in inputs:
        cargs = copy.deepcopy(args)
        got = fnc(*cargs)
        if got is None:
            got = cargs[0] if len(cargs) == 1 else cargs
        out.append(repr(got))
    print(fname)
    print("\n".join(out))

if __name__ == "__main__":
    main()

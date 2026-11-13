#!/usr/bin/env python3
# Ground-truth runner supporting list/int/str AND tree/linked-list IO.
# Usage: run_ref2.py <pyfile> <mode> <json-inputs>
#   mode = "plain"  -> inputs are lists of python-evaluable arg tuples; prints repr of results
#   mode = "tree"   -> inputs are level-order arrays (with None); builds TreeNode, calls solve, serializes result (level order, no trailing nulls) OR bool/int
#   mode = "list"   -> inputs are arrays; builds ListNode, calls solve, serializes result list
import sys, ast, json, copy

HELPERS = {"print","build_list","print_list","build_tree","to_list","list_to_arr",
           "demo","helper","main","TreeNode","ListNode","Solution","min","max","abs",
           "len","sorted","range","enumerate","zip","list","dict","set","sum","int",
           "str","float","bool","print_list_node","build_linked_list","get_node"}

def find_solve(src):
    tree = ast.parse(src)
    main_block=None
    for node in tree.body:
        if isinstance(node, ast.If): main_block=node.body; break
    for node in (main_block or []):
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            f=node.value.func
            if isinstance(f, ast.Name) and f.id not in HELPERS: return f.id
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name not in HELPERS: return node.name
    return None

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val; self.left=left; self.right=right
class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val; self.next=next

def build_tree(vals):
    if not vals or vals[0] is None: return None
    root=TreeNode(vals[0]); q=[root]; i=1
    while q and i < len(vals):
        n=q.pop(0)
        if vals[i] is not None:
            n.left=TreeNode(vals[i]); q.append(n.left)
        i+=1
        if i < len(vals) and vals[i] is not None:
            n.right=TreeNode(vals[i]); q.append(n.right)
        i+=1
    return root

def serialize_tree(n):
    if n is None: return []
    out=[]; q=[n]
    while q:
        x=q.pop(0); 
        if x is None: out.append(None); continue
        out.append(x.val); 
        q.append(x.left); q.append(x.right)
    while out and out[-1] is None: out.pop()
    return out

def build_list(vals):
    if not vals: return None
    head=ListNode(vals[0]); p=head
    for v in vals[1:]: p.next=ListNode(v); p=p.next
    return head
def serialize_list(n):
    out=[]; p=n
    while p: out.append(p.val); p=p.next
    return out

def main():
    pyfile=sys.argv[1]; mode=sys.argv[2]; inputs=json.loads(sys.argv[3])
    src=open(pyfile, encoding="utf-8").read()
    ns={"__name__":"_t_","TreeNode":TreeNode,"ListNode":ListNode}
    exec(compile(src, pyfile, "exec"), ns)
    fname=find_solve(src)
    if not fname or fname not in ns:
        print("NOFUNC:"+str(fname)); sys.exit(2)
    fnc=ns[fname]
    out=[]
    for inp in inputs:
        try:
            if mode=="plain":
                cargs=copy.deepcopy(inp)
                got=fnc(*cargs)
                if got is None: got = cargs[0] if len(cargs)==1 else cargs
                out.append(repr(got))
            elif mode=="tree":
                cargs=[build_tree(a) if isinstance(a,list) else a for a in inp]
                got=fnc(*cargs)
                if isinstance(got, TreeNode): out.append(repr(serialize_tree(got)))
                elif isinstance(got, bool): out.append(repr(got))
                elif isinstance(got, int): out.append(repr(got))
                else: out.append(repr(got))
            elif mode=="list":
                cargs=[build_list(a) if isinstance(a,list) else a for a in inp]
                got=fnc(*cargs)
                if isinstance(got, ListNode): out.append(repr(serialize_list(got)))
                else: out.append(repr(got))
        except Exception as e:
            out.append("ERRCASE")
    print(fname)
    print("\n".join(out))

if __name__=="__main__":
    main()

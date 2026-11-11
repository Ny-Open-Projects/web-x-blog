#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Scale-up remediation transpiler (python ref -> ts/go/java) with embedded tests."""
import os, ast, json, re, subprocess, traceback

BASE = "/Users/Wang/Code/github/web-x-blog/work/target/21.dsa"
HELPER_NAMES = {"print", "build_list", "print_list", "build_tree", "to_list",
                "list_to_arr", "demo", "helper", "main", "__init__"}

def find_pydir(prob_folder):
    for topic in os.listdir(os.path.join(BASE, "python")):
        cand = os.path.join(BASE, "python", topic, prob_folder)
        if os.path.isdir(cand):
            return cand
    return None

# ----------------- serialization / test extraction -----------------
class SerError(Exception):
    pass

def py_serialize(val):
    if val is None: return ("none", None)
    if isinstance(val, bool): return ("bool", val)
    if isinstance(val, int): return ("int", val)
    if isinstance(val, float): return ("float", val)
    if isinstance(val, str): return ("str", val)
    if isinstance(val, (list, tuple)): return ("list", [py_serialize(v) for v in val])
    if hasattr(val, "val") and hasattr(val, "next") and not hasattr(val, "left"):
        out = []; cur = val
        while cur is not None:
            out.append(cur.val); cur = cur.next
        return ("listnode", out)
    if hasattr(val, "left") or hasattr(val, "right"):
        return ("treenode", tree_to_level(val))
    if isinstance(val, dict): return ("dict", [[py_serialize(k), py_serialize(v)] for k, v in val.items()])
    if isinstance(val, set): return ("set", sorted([py_serialize(v) for v in val], key=str))
    raise SerError("cannot serialize %r" % type(val))

def tree_to_level(root):
    if root is None: return []
    out = []; q = [root]
    while q:
        node = q.pop(0)
        if node is None:
            out.append(None); continue
        out.append(getattr(node, "val", None))
        q.append(getattr(node, "left", None)); q.append(getattr(node, "right", None))
    while out and out[-1] is None: out.pop()
    return out

def classify_type(val):
    return py_serialize(val)[0]

def extract_tests(pydir):
    files = sorted(f for f in os.listdir(pydir) if f.endswith(".py"))
    all_classes = {}
    result_map = {}  # sname -> list of (args_ser, ret_ser_or_poststate, ptypes, rtype, inplace)
    for fn in files:
        src = open(os.path.join(pydir, fn), encoding="utf-8").read()
        try: tree = ast.parse(src)
        except Exception: continue
        for c in tree.body:
            if isinstance(c, ast.ClassDef): all_classes[c.name] = c
        main_body = None
        for n in tree.body:
            if isinstance(n, ast.If) and isinstance(n.test, ast.Compare) and isinstance(n.test.left, ast.Name) and n.test.left.id == "__name__":
                main_body = n.body; break
        if main_body is None: continue
        funcs = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
        calls = []
        for st in main_body:
            for node in ast.walk(st):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                    f2 = node.func.id
                    if f2 in funcs and f2 not in HELPER_NAMES:
                        calls.append((f2, node))
        if not calls: continue
        ns = {}
        try: exec(compile(src, fn, "exec"), ns)
        except Exception: continue
        for fname, node in calls:
            live = ns.get(fname)
            if live is None: continue
            try: args = [eval(ast.unparse(a), ns) for a in node.args]
            except Exception: continue
            try: out = live(*args)
            except Exception: continue
            try:
                args_ser = [py_serialize(a) for a in args]
                # inplace detection: if out is None, capture post-state of primary mutable arg
                inplace = (out is None)
                if inplace:
                    post = py_serialize(args[0]) if args else ("none", None)
                    ret_ser = post
                else:
                    ret_ser = py_serialize(out)
            except SerError: continue
            ptypes = [classify_type(a) for a in args]
            rtype = classify_type(out) if not inplace else classify_type(args[0]) if args else "none"
            entry = (tuple(args_ser), ret_ser, tuple(ptypes), rtype, inplace)
            # dedupe per function
            seen = {e[0] for e in result_map.get(fname, [])}
            if entry[0] in seen: continue
            result_map.setdefault(fname, []).append(entry)
    if not result_map: return None, all_classes
    return result_map, all_classes

# ----------------- transpiler -----------------
class T:
    def __init__(self, lang, classes):
        self.lang = lang
        self.classes = classes or {}
        self.vt = {}
        self.helper_defs = []  # extra top-level helpers (listcomp etc.)
        self.lc_counter = 0

    def t(self, tag):
        L = self.lang
        if tag in ("int", "float"): return "number" if L == "ts" else ("int" if L == "go" else "int")
        if tag == "bool": return "boolean" if L == "ts" else ("bool" if L == "go" else "boolean")
        if tag == "str": return "string"
        if tag == "listnode": return "ListNode"
        if tag == "treenode": return "TreeNode"
        if tag == "list": return "any[]" if L == "ts" else ("[]interface{}" if L == "go" else "Object[]")
        if tag in ("dict", "set"): return "any" if L == "ts" else ("map[string]interface{}" if L == "go" else "Map")
        return "any" if L == "ts" else ("interface{}" if L == "go" else "Object")

    def is_listnode_cls(self, name):
        c = self.classes.get(name)
        if not c: return False
        attrs = {n.attr for n in ast.walk(c) if isinstance(n, ast.Attribute) and isinstance(n.value, ast.Name) and n.value.id == "self"}
        return "next" in attrs and "val" in attrs and "left" not in attrs

    def is_treenode_cls(self, name):
        c = self.classes.get(name)
        if not c: return False
        attrs = {n.attr for n in ast.walk(c) if isinstance(n, ast.Attribute) and isinstance(n.value, ast.Name) and n.value.id == "self"}
        return "left" in attrs or "right" in attrs

    def setvar(self, name, typ):
        if typ and typ != "any": self.vt[name] = typ

    # ---- expressions ----
    def expr(self, node):
        L = self.lang
        if isinstance(node, ast.Constant):
            v = node.value
            if v is None: return ("null" if L != "go" else "nil", "none")
            if isinstance(v, bool): return ("true" if v else "false", "bool")
            if isinstance(v, str):
                if L == "go": return ('"%s"' % v.replace('\\', '\\\\').replace('"', '\\"'), "str")
                return (json.dumps(v), "str")
            if isinstance(v, float): return (repr(v), "float")
            return (str(v), "int")
        if isinstance(node, ast.Name):
            return (node.id, self.vt.get(node.id, "any"))
        if isinstance(node, ast.Attribute):
            base, bt = self.expr(node.value)
            return ("%s.%s" % (base, node.attr), "any")
        if isinstance(node, ast.BinOp):
            a, ta = self.expr(node.left); b, tb = self.expr(node.right)
            op = {ast.Add: "+", ast.Sub: "-", ast.Mult: "*", ast.Div: "/",
                  ast.Mod: "%", ast.FloorDiv: "/", ast.Pow: "**",
                  ast.BitOr: "|", ast.BitAnd: "&", ast.BitXor: "^",
                  ast.LShift: "<<", ast.RShift: ">>"}[type(node.op)]
            if op == "**":
                f = "Math.pow" if L != "go" else "math.Pow"
                return ("%s(%s,%s)" % (f, a, b), "float")
            if op == "/":
                if L == "go" and ta == "int" and tb == "int":
                    return ("(%s/%s)" % (a, b), "int")
                return ("(%s/%s)" % (a, b), "float")
            rt = "int" if (ta == "int" and tb == "int") else "float"
            return ("(%s%s%s)" % (a, op, b), rt)
        if isinstance(node, ast.BoolOp):
            vals = [self.expr(v) for v in node.values]
            op = "&&" if isinstance(node.op, ast.And) else "||"
            return ("(" + op.join(x[0] for x in vals) + ")", "bool")
        if isinstance(node, ast.UnaryOp):
            v, tv = self.expr(node.operand)
            if isinstance(node.op, ast.Not): return ("(!" + v + ")", "bool")
            if isinstance(node.op, ast.USub): return ("(-" + v + ")", tv)
            return ("(+" + v + ")", tv)
        if isinstance(node, ast.Compare):
            left, lt = self.expr(node.left)
            parts = [left]; res = "bool"
            for op, comp in zip(node.ops, node.comparators):
                r, rt = self.expr(comp)
                m = {ast.Eq: "==", ast.NotEq: "!=", ast.Lt: "<", ast.LtE: "<=",
                     ast.Gt: ">", ast.GtE: ">=", ast.Is: "==", ast.IsNot: "!=",
                     ast.In: None, ast.NotIn: None}
                o = m[type(op)]
                if o is None:
                    neg = isinstance(op, ast.NotIn)
                    if rt in ("list", "str"):
                        if L == "ts": s = "(%s.indexOf(%s)>=0)" if not neg else "(%s.indexOf(%s)<0)"
                        elif L == "go": s = "(contains(%s,%s))" if not neg else "(!contains(%s,%s))"
                        else: s = "(%s.contains(%s))" if not neg else "(!%s.contains(%s))"
                        parts.append(s % (r, left))
                    else:
                        if L == "ts": s = "(%s.includes(%s))" if not neg else "(!%s.includes(%s))"
                        elif L == "go": s = "(contains(%s,%s))" if not neg else "(!contains(%s,%s))"
                        else: s = "(%s.contains(%s))" if not neg else "(!%s.contains(%s))"
                        parts.append(s % (r, left))
                    left = r; continue
                parts.append("%s%s%s" % (left, o, r)); left = r
            return ("(" + "&&".join(parts) + ")", res)
        if isinstance(node, ast.Call): return self.call(node)
        if isinstance(node, ast.Subscript): return self.subscript(node)
        if isinstance(node, ast.List):
            elems = [self.expr(e) for e in node.elts]
            et = "any"
            if elems:
                if elems[0][1] in ("int", "float"): et = "int"
                elif elems[0][1] == "str": et = "str"
            inner = ", ".join(e[0] for e in elems)
            if L == "ts": return ("[" + inner + "]", "list")
            if L == "go":
                if et == "int": return ("[]int{" + inner + "}", "list")
                if et == "str": return ("[]string{" + inner + "}", "list")
                return ("[]interface{}{" + inner + "}", "list")
            if et == "int": return ("new int[]{" + inner + "}", "list")
            if et == "str": return ("new String[]{" + inner + "}", "list")
            return ("new Object[]{" + inner + "}", "list")
        if isinstance(node, ast.Tuple):
            elems = [self.expr(e) for e in node.elts]
            inner = ", ".join(e[0] for e in elems)
            if L == "ts": return ("[" + inner + "]", "list")
            if L == "go": return ("[]interface{}{" + inner + "}", "list")
            return ("new Object[]{" + inner + "}", "list")
        if isinstance(node, ast.Set):
            elems = [self.expr(e) for e in node.elts]
            inner = ", ".join(e[0] for e in elems)
            if L == "ts": return ("new Set([" + inner + "])", "set")
            if L == "go": return ("setFrom([]interface{}{" + inner + "})", "set")
            return ("new HashSet<>(Arrays.asList(" + inner + "))", "set")
        if isinstance(node, ast.Dict):
            keys = [self.expr(k) for k in node.keys]
            vals = [self.expr(v) for v in node.values]
            if L == "ts":
                inner = ", ".join("%s:%s" % (k[0], v[0]) for k, v in zip(keys, vals))
                return ("({%s})" % inner, "dict")
            if L == "go":
                inner = ", ".join("\"%s\":%s" % (k[0].strip('"'), v[0]) for k, v in zip(keys, vals))
                return ("map[string]interface{}{" + inner + "}", "dict")
            inner = ";".join("%s.put(%s,%s)" % (HM, k[0], v[0]) for k, v in zip(keys, vals))
            return ("(new HashMap(){ { %s; } })" % inner, "dict")
        if isinstance(node, ast.IfExp):
            c, _ = self.expr(node.test); a, ta = self.expr(node.body); b, tb = self.expr(node.orelse)
            return ("(%s?%s:%s)" % (c, a, b), ta if ta != "any" else tb)
        if isinstance(node, ast.ListComp): return self.listcomp(node)
        raise NotImplementedError("expr %s" % ast.dump(node))

    def listcomp(self, node):
        L = self.lang
        gen = node.generators[0]
        iter_code, iter_t = self.expr(gen.iter)
        if isinstance(gen.target, ast.Name):
            vname = gen.target.id
        else:
            vname = "_it"
        elem, et = self.expr(node.elt)
        conds = gen.ifs
        # TS: map/filter
        if L == "ts":
            if conds:
                cc = "&&".join(self.expr(c)[0] for c in conds)
                return ("%s.filter(%s=>(%s)).map(%s=>%s)" % (iter_code, vname, cc, vname, elem), "list")
            return ("%s.map(%s=>%s)" % (iter_code, vname, elem), "list")
        # go/java: build helper
        self.lc_counter += 1
        hname = "lc%d" % self.lc_counter
        # free vars
        free = set()
        for n in ast.walk(node.elt):
            if isinstance(n, ast.Name) and n.id != vname: free.add(n.id)
        for c in conds:
            for n in ast.walk(c):
                if isinstance(n, ast.Name) and n.id != vname: free.add(n.id)
        free = sorted(f for f in free if f not in ("True", "False", "None"))
        # generate helper
        if L == "go":
            params = ", ".join("%s %s" % (f, self.t(self.vt.get(f, "any"))) for f in free)
            sig = "func %s(it []interface{}, %s) []interface{}" % (hname, params)
            body = "  r := []interface{}{}\n  for _, %s := range it {\n" % vname
            cond = "&&".join(self.expr(c)[0] for c in conds)
            if cond: body += "    if %s {\n" % cond
            body += "      r = append(r, %s)\n" % elem
            if cond: body += "    }\n"
            body += "  }\n  return r\n"
            self.helper_defs.append(sig + " {\n" + body + "}")
            fargs = ", ".join(f for f in free)
            return ("%s(%s, %s)" % (hname, iter_code, fargs), "list")
        else:
            params = ", ".join("%s %s" % (self.t(self.vt.get(f, "any")), f) for f in free)
            sig = "static Object[] %s(Object[] it, %s)" % (hname, params)
            body = "  ArrayList<Object> r = new ArrayList<>();\n  for (Object %s : it) {\n" % vname
            cond = "&&".join(self.expr(c)[0] for c in conds)
            if cond: body += "    if (%s) {\n" % cond
            body += "      r.add(%s);\n" % elem
            if cond: body += "    }\n"
            body += "  }\n  return r.toArray(new Object[0]);\n"
            self.helper_defs.append(sig + " {\n" + body + "}")
            fargs = ", ".join(f for f in free)
            return ("%s(%s, %s)" % (hname, iter_code, fargs), "list")

    def subscript(self, node):
        L = self.lang
        base, bt = self.expr(node.value)
        if isinstance(node.slice, ast.Slice):
            low = self.expr(node.slice.lower)[0] if node.slice.lower else ("0" if L != "go" else "0")
            high = self.expr(node.slice.upper)[0] if node.slice.upper else None
            if L == "ts": return ("%s.slice(%s,%s)" % (base, low, high if high else "undefined"), "list")
            if L == "go": return ("%s[%s:%s]" % (base, low, high if high else "len(%s)" % base), "list")
            h = high if high else ("%s.length" % base)
            return ("Arrays.copyOfRange(%s,%s,%s)" % (base, low, h), "list")
        idx, it = self.expr(node.slice)
        return ("%s[%s]" % (base, idx), "any")

    def call(self, node):
        L = self.lang
        f = node.func
        args = [self.expr(a) for a in node.args]
        argstr = ", ".join(a[0] for a in args)
        if isinstance(f, ast.Attribute):
            base, bt = self.expr(f.value)
            m = f.attr
            meth = {
                "append": ("%s.push(%s)" if L=="ts" else ("append(%s,%s)" if L=="go" else "%s.add(%s)")),
                "pop": ("%s.pop()" if L=="ts" else ("pop(%s)" if L=="go" else "%s.remove(%s.size()-1)")),
                "extend": ("%s.push(...%s)" if L=="ts" else ("append(%s,...)" if L=="go" else "%s.addAll(Arrays.asList(%s))")),
                "add": ("%s.add(%s)" if L=="ts" else ("%s[%s]=true" if L=="go" else "%s.add(%s)")),
                "get": ("%s.get(%s)" if L!="go" else "%s[%s]"),
                "split": ("%s.split(%s)" if L!="go" else "strings.Split(%s,%s)"),
                "join": ("%s.join(%s)" if L!="go" else "strings.Join(%s,%s)"),
                "lower": ("%s.toLowerCase()" if L!="go" else "strings.ToLower(%s)"),
                "upper": ("%s.toUpperCase()" if L!="go" else "strings.ToUpper(%s)"),
                "strip": ("%s.trim()" if L!="go" else "strings.TrimSpace(%s)"),
                "startswith": ("%s.startsWith(%s)" if L!="go" else "strings.HasPrefix(%s,%s)"),
                "endswith": ("%s.endsWith(%s)" if L!="go" else "strings.HasSuffix(%s,%s)"),
            }
            if m in meth:
                if m == "pop" and args:
                    if L == "ts": return ("%s.splice(%s,1)[0]" % (base, args[0][0]), "any")
                    if L == "go": return ("popAt(%s,%s)" % (base, args[0][0]), "any")
                    return ("%s.remove((int)%s)" % (base, args[0][0]), "any")
                if m == "extend":
                    if L == "ts": return (meth[m] % (base, args[0][0]), "none")
                    if L == "go": return ("append(%s, %s...)" % (base, args[0][0]), "none")
                    return (meth[m] % (base, args[0][0]), "none")
                if m in ("split", "join", "lower", "upper", "strip", "startswith", "endswith"):
                    return (meth[m] % (base, args[0][0]), "str" if m in ("join","lower","upper","strip") else "list" if m=="split" else "bool")
                return (meth[m] % (base, args[0][0] if args else ""), "none" if m in ("append","add") else "any")
            if m in ("keys", "values", "items"):
                if L == "ts":
                    return (("Object.keys(%s)" if m=="keys" else "Object.values(%s)" if m=="values" else "Object.entries(%s)") % base, "list")
                if L == "go":
                    return (("keys(%s)" if m=="keys" else "vals(%s)" if m=="values" else "items(%s)") % base, "list")
                return (("%s.keySet()" if m=="keys" else "%s.values()" if m=="values" else "%s.entrySet()") % base, "list")
            if m == "count" and L == "go":
                return ("strings.Count(%s,%s)" % (base, args[0][0]), "int")
            return ("%s.%s(%s)" % (base, m, argstr), "any")
        if isinstance(f, ast.Name):
            name = f.id
            if name == "print":
                if L == "ts": return ("console.log(%s)" % argstr, "none")
                if L == "go": return ("fmt.Println(%s)" % argstr, "none")
                return ("System.out.println(%s)" % argstr, "none")
            B = {
                "len": ("%s.length" if L!="go" else "len(%s)"),
                "sorted": ("%s.slice().sort((a,b)=>a-b)" if L=="ts" else ("sortedCopy(%s)" if L=="go" else "sortedCopy(%s)")),
                "abs": ("Math.abs(%s)" if L!="go" else "abs(%s)"),
                "int": ("Math.trunc(%s)" if L=="ts" else ("int(%s)" if L=="go" else "(int)(%s)")),
                "str": ("String(%s)" if L=="ts" else ("fmt.Sprint(%s)" if L=="go" else "String.valueOf(%s)")),
                "list": ("Array.from(%s)" if L=="ts" else ("toSlice(%s)" if L=="go" else "new ArrayList<>(Arrays.asList(%s))")),
                "set": ("new Set(%s)" if L=="ts" else ("setFrom(%s)" if L=="go" else "new HashSet<>(%s)")),
            }
            if name in B: return (B[name] % args[0][0], "int" if name in ("len","abs","int") else "list" if name in ("sorted","list") else "str" if name=="str" else "set")
            if name in self.classes:
                inner = ", ".join(a[0] for a in args)
                return ("new %s(%s)" % (name, inner), name.lower())
            return ("%s(%s)" % (name, argstr), "any")
        return ("__CALL__", "any")

    # ---- statements ----
    def stmt(self, node, ind):
        L = self.lang
        pad = "  " * ind
        if isinstance(node, ast.FunctionDef): return self.funcdef(node, ind)
        if isinstance(node, ast.ClassDef): return self.classdef(node, ind)
        if isinstance(node, ast.Assign): return self.assign(node, ind)
        if isinstance(node, ast.AugAssign): return self.augassign(node, ind)
        if isinstance(node, ast.If): return self.ifstmt(node, ind)
        if isinstance(node, ast.For): return self.forstmt(node, ind)
        if isinstance(node, ast.While): return self.whilestmt(node, ind)
        if isinstance(node, ast.Return):
            if node.value is None: return pad + ("return;" if L != "go" else "return")
            v, vt = self.expr(node.value)
            if L == "java": return pad + "return %s;" % v
            return pad + "return %s" % v
        if isinstance(node, ast.Expr):
            e, et = self.expr(node.value)
            if et == "none": return pad + e + (";" if L == "java" else "")
            return pad + e + (";" if L == "java" else "")
        if isinstance(node, ast.Pass): return ""
        if isinstance(node, ast.Break): return pad + "break" + (";" if L == "java" else "")
        if isinstance(node, ast.Continue): return pad + "continue" + (";" if L == "java" else "")
        if isinstance(node, (ast.Global, ast.Nonlocal)): return ""
        raise NotImplementedError("stmt %s" % ast.dump(node))

    def funcdef(self, node, ind, param_types=None, ret_type=None):
        L = self.lang
        pad = "  " * ind
        params = []
        for i, a in enumerate(node.args.args):
            pname = a.arg
            ptype = (param_types[i] if param_types and i < len(param_types) else self.vt.get(pname, "any"))
            params.append((pname, ptype))
        rtype = ret_type if ret_type and ret_type != "any" else "any"
        oldvt = self.vt; self.vt = {}
        for pname, ptype in params: self.vt[pname] = ptype
        body_lines = [self.stmt(s, ind + 1) for s in node.body]
        self.vt = oldvt
        body = "\n".join(body_lines)
        if L == "ts":
            ps = ", ".join("%s: %s" % (p, self.t(t)) for p, t in params)
            return "%sfunction %s(%s): %s {\n%s\n%s}" % (pad, node.name, ps, self.t(rtype), body, pad)
        if L == "go":
            ps = ", ".join("%s %s" % (p, self.t(t)) for p, t in params)
            return "%sfunc %s(%s) %s {\n%s\n%s}" % (pad, node.name, ps, self.t(rtype), body, pad)
        ps = ", ".join("%s %s" % (self.t(t), p) for p, t in params)
        return "%s%s %s(%s) {\n%s\n%s}" % (pad, self.t(rtype), node.name, ps, body, pad)

    def classdef(self, node, ind):
        L = self.lang
        pad = "  " * ind
        cname = node.name
        if self.is_listnode_cls(cname):
            if L == "ts":
                return (pad + "class ListNode {\n" + pad + "  val: number;\n" + pad +
                        "  next: ListNode | null;\n" + pad +
                        "  constructor(val?: number, next?: ListNode | null) {\n" + pad +
                        "    this.val = (val===undefined?0:val);\n" + pad +
                        "    this.next = (next===undefined?null:next);\n" + pad + "  }\n" + pad + "}")
            if L == "go":
                return pad + "type ListNode struct {\n" + pad + "  Val int\n" + pad + "  Next *ListNode\n" + pad + "}"
            return (pad + "static class ListNode {\n" + pad + "  int val;\n" + pad + "  ListNode next;\n" + pad +
                    "  ListNode() {}\n" + pad + "  ListNode(int val) { this.val = val; }\n" + pad +
                    "  ListNode(int val, ListNode next) { this.val = val; this.next = next; }\n" + pad + "}")
        if self.is_treenode_cls(cname):
            if L == "ts":
                return (pad + "class TreeNode {\n" + pad + "  val: number;\n" + pad +
                        "  left: TreeNode | null;\n" + pad + "  right: TreeNode | null;\n" + pad +
                        "  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {\n" + pad +
                        "    this.val = (val===undefined?0:val);\n" + pad +
                        "    this.left = (left===undefined?null:left);\n" + pad +
                        "    this.right = (right===undefined?null:right);\n" + pad + "  }\n" + pad + "}")
            if L == "go":
                return pad + "type TreeNode struct {\n" + pad + "  Val int\n" + pad + "  Left *TreeNode\n" + pad + "  Right *TreeNode\n" + pad + "}"
            return (pad + "static class TreeNode {\n" + pad + "  int val;\n" + pad +
                    "  TreeNode left;\n" + pad + "  TreeNode right;\n" + pad + "  TreeNode() {}\n" + pad +
                    "  TreeNode(int val) { this.val = val; }\n" + pad +
                    "  TreeNode(int val, TreeNode left, TreeNode right) { this.val = val; this.left = left; this.right = right; }\n" + pad + "}")
        return ""

    def assign(self, node, ind):
        L = self.lang
        pad = "  " * ind
        targets = node.targets
        val, vt = self.expr(node.value)
        if len(targets) == 1 and isinstance(targets[0], ast.Name):
            name = targets[0].id
            self.setvar(name, vt)
            if L == "ts": return pad + "let %s = %s;" % (name, val)
            if L == "go": return pad + "var %s = %s" % (name, val)
            return pad + "%s %s = %s;" % (self.t(vt), name, val)
        if len(targets) == 1 and isinstance(targets[0], ast.Subscript):
            base, _ = self.expr(targets[0].value); idx, _ = self.expr(targets[0].slice)
            return pad + "%s[%s] = %s" % (base, idx, val) + (";" if L == "java" else "")
        if len(targets) == 1 and isinstance(targets[0], ast.Attribute):
            base, _ = self.expr(targets[0].value)
            return pad + "%s.%s = %s" % (base, targets[0].attr, val) + (";" if L == "java" else "")
        if isinstance(targets[0], (ast.Tuple, ast.List)):
            names = []
            for elt in targets[0].elts:
                names.append(elt.id if isinstance(elt, ast.Name) else "_")
            for n in names: self.setvar(n, "any")
            if L == "ts": return pad + "let [%s] = %s;" % (", ".join(names), val)
            if L == "go":
                return "\n".join(pad + "var %s = %s[%d]" % (n, val, i) for i, n in enumerate(names))
            return "\n".join(pad + "Object %s = %s[%d];" % (n, val, i) for i, n in enumerate(names))
        raise NotImplementedError("assign %s" % ast.dump(node))

    def augassign(self, node, ind):
        L = self.lang; pad = "  " * ind
        target = node.target
        val, _ = self.expr(node.value)
        op = {ast.Add: "+", ast.Sub: "-", ast.Mult: "*", ast.Div: "/", ast.Mod: "%"}[type(node.op)]
        if isinstance(target, ast.Name):
            return pad + "%s %s= %s" % (target.id, op, val) + (";" if L == "java" else "")
        if isinstance(target, ast.Subscript):
            base, _ = self.expr(target.value); idx, _ = self.expr(target.slice)
            return pad + "%s[%s] %s= %s" % (base, idx, op, val) + (";" if L == "java" else "")
        raise NotImplementedError("augassign")

    def ifstmt(self, node, ind):
        L = self.lang; pad = "  " * ind
        test, _ = self.expr(node.test)
        out = pad + "if (%s) {\n" % test
        for s in node.body: out += self.stmt(s, ind + 1) + "\n"
        out += pad + "}"
        rest = node.orelse
        i = 0
        while i < len(rest):
            els = rest[i]
            if isinstance(els, ast.If):
                t2, _ = self.expr(els.test)
                out += " else if (%s) {\n" % t2
                for s in els.body: out += self.stmt(s, ind + 1) + "\n"
                out += pad + "}"
                rest = els.orelse
                i = 0
                continue
            else:
                out += " else {\n"
                out += self.stmt(els, ind + 1) + "\n"
                out += pad + "}"
                i += 1
        return out

    def forstmt(self, node, ind):
        L = self.lang; pad = "  " * ind
        target = node.target; iter_node = node.iter
        if isinstance(iter_node, ast.Call) and isinstance(iter_node.func, ast.Name) and iter_node.func.id == "range":
            args = iter_node.args
            if len(args) == 1:
                hi, _ = self.expr(args[0]); lo, hi2 = "0", hi
            else:
                lo, _ = self.expr(args[0]); hi, _ = self.expr(args[1])
            v = target.id if isinstance(target, ast.Name) else "_i"
            self.setvar(v, "int")
            if L == "ts": return pad + "for (let %s = %s; %s < %s; %s++) {\n%s\n%s}" % (v, lo, v, hi, v, "", pad)
            if L == "go": return pad + "for %s := %s; %s < %s; %s++ {\n%s\n%s}" % (v, lo, v, hi, v, "", pad)
            return pad + "for (int %s = %s; %s < %s; %s++) {\n%s\n%s}" % (v, lo, v, hi, v, "", pad)
        iter_code, iter_t = self.expr(iter_node)
        vname = target.id if isinstance(target, ast.Name) else "_it"
        self.setvar(vname, "any")
        if L == "ts": out = pad + "for (const %s of %s) {\n" % (vname, iter_code)
        elif L == "go": out = pad + "for _, %s := range %s {\n" % (vname, iter_code)
        else: out = pad + "for (Object %s : %s) {\n" % (vname, iter_code)
        for s in node.body: out += self.stmt(s, ind + 1) + "\n"
        out += pad + "}"
        return out

    def whilestmt(self, node, ind):
        L = self.lang; pad = "  " * ind
        test, _ = self.expr(node.test)
        out = pad + "while (%s) {\n" % test
        for s in node.body: out += self.stmt(s, ind + 1) + "\n"
        out += pad + "}"
        return out

# placeholder imports to satisfy linters
import math


# ----------------- file assembly -----------------
def make_ts_value(ser):
    """Emit a JS literal for a serialized value."""
    tag, v = ser
    if tag == "none": return "null"
    if tag == "bool": return "true" if v else "false"
    if tag == "int": return str(v)
    if tag == "float": return repr(v)
    if tag == "str": return json.dumps(v)
    if tag == "list": return "[" + ", ".join(make_ts_value(x) for x in v) + "]"
    if tag in ("listnode", "treenode"):
        return json.dumps(v)
    if tag == "set": return "new Set(" + json.dumps(v) + ")"
    if tag == "dict": return "({})"
    return "null"

def build_ts(solve_name, func_node, classes, tests, lang="ts"):
    tr = T("ts", classes)
    body = tr.funcdef(func_node, 0, param_types=list(tests[0][2]), ret_type=tests[0][3])
    helper_defs = "\n".join(tr.helper_defs)
    lines = []
    lines.append("export function demo(): void {")
    for cname, cnode in classes.items():
        cd = tr.classdef(cnode, 1)
        if cd: lines.append(cd); lines.append("")
    # helpers
    lines.append("  function build(nums: any): ListNode | null {")
    lines.append("    let dummy = new ListNode(0); let cur = dummy;")
    lines.append("    if (nums != null) for (const n of nums) { cur.next = new ListNode(n); cur = cur.next; }")
    lines.append("    return dummy.next; }")
    lines.append("  function toList(head: any): any { const r: any[] = []; while (head) { r.push(head.val); head = head.next; } return r; }")
    lines.append("  function buildTree(vals: any): TreeNode | null {")
    lines.append("    if (!vals || !vals.length) return null; const root = new TreeNode(vals[0]); const q: any[] = [root]; let i = 1;")
    lines.append("    while (q.length && i < vals.length) { const node = q.shift();")
    lines.append("      if (i < vals.length && vals[i] !== null && vals[i] !== undefined) { node.left = new TreeNode(vals[i]); q.push(node.left); } i++;")
    lines.append("      if (i < vals.length && vals[i] !== null && vals[i] !== undefined) { node.right = new TreeNode(vals[i]); q.push(node.right); } i++; }")
    lines.append("    return root; }")
    lines.append("  function toLevel(root: any): any { if (!root) return []; const r: any[] = []; const q: any[] = [root];")
    lines.append("    while (q.length) { const n = q.shift(); if (!n) { r.push(null); continue; }")
    lines.append("      r.push(n.val); q.push(n.left); q.push(n.right); }")
    lines.append("    while (r.length && r[r.length-1] === null) r.pop(); return r; }")
    lines.append("  function eqArr(a: any, b: any): boolean {")
    lines.append("    if (a === b) return true;")
    lines.append("    if (Array.isArray(a) && Array.isArray(b)) { if (a.length !== b.length) return false; for (let i=0;i<a.length;i++) if (!eqArr(a[i],b[i])) return false; return true; }")
    lines.append("    if (typeof a === 'object' && typeof b === 'object' && a && b) return JSON.stringify(a) === JSON.stringify(b);")
    lines.append("    return false; }")
    lines.append("")
    lines.append("  " + body.replace("\n", "\n  "))
    lines.append("")
    lines.append("  const cases: any[] = [")
    for arg_ser, ret_ser, ptypes, rtype, inplace in tests:
        in_raw = "[" + ", ".join(make_ts_value(a) for a in arg_ser) + "]"
        want_raw = make_ts_value(ret_ser)
        lines.append("    { inRaw: %s, wantRaw: %s, ptypes: %s, rtype: %s, inplace: %s }," % (
            in_raw, want_raw, json.dumps(list(ptypes)), json.dumps(rtype), "true" if inplace else "false"))
    lines.append("  ];")
    lines.append("  let fail = false;")
    lines.append("  for (const c of cases) {")
    lines.append("    const args = c.inRaw.map((v: any, i: number) => {")
    lines.append("      const tp = c.ptypes[i];")
    lines.append("      if (tp === 'listnode') return build(v);")
    lines.append("      if (tp === 'treenode') return buildTree(v);")
    lines.append("      return v; });")
    lines.append("    let got: any;")
    lines.append("    if (c.inplace) {")
    lines.append("      (%s as any)(...args);" % solve_name)
    lines.append("      const tp = c.ptypes[0];")
    lines.append("      got = (tp === 'listnode') ? toList(args[0]) : (tp === 'treenode') ? toLevel(args[0]) : args[0];")
    lines.append("    } else {")
    lines.append("      let r = (%s as any)(...args);" % solve_name)
    lines.append("      got = (c.rtype === 'listnode') ? toList(r) : (c.rtype === 'treenode') ? toLevel(r) : r;")
    lines.append("    }")
    lines.append("    if (!eqArr(got, c.wantRaw)) { fail = true; console.log('FAIL', JSON.stringify(got), 'want', JSON.stringify(c.wantRaw)); }")
    lines.append("  }")
    lines.append("  if (fail) throw new Error('FAILED');")
    lines.append("  console.log('PASS');")
    lines.append("}")
    lines.append("demo();")
    return "\n".join(lines)


# ----------------- verify -----------------
def verify(lang, filepath):
    if lang == "ts":
        cmd = ["/Users/Wang/.workbuddy/binaries/node/versions/22.22.2-6/bin/node", "--experimental-strip-types", filepath]
        r = subprocess.run(cmd, capture_output=True, text=True, cwd=BASE)
        return r.returncode, r.stdout, r.stderr
    if lang == "go":
        cmd = ["/usr/local/go1.26.5/bin/go", "run", filepath]
        env = dict(os.environ, GO111MODULE="off")
        r = subprocess.run(cmd, capture_output=True, text=True, env=env, cwd=BASE)
        return r.returncode, r.stdout, r.stderr
    cls = os.path.splitext(os.path.basename(filepath))[0]
    javac = "/Library/Java/JavaVirtualMachines/jdk-12.jdk/Contents/Home/bin/javac"
    java = "/Library/Java/JavaVirtualMachines/jdk-12.jdk/Contents/Home/bin/java"
    rc = subprocess.run([javac, "-d", "/tmp/jout", filepath], capture_output=True, text=True, cwd=BASE)
    if rc.returncode != 0:
        return rc.returncode, rc.stdout, rc.stderr
    r = subprocess.run([java, "-cp", "/tmp/jout", "com.webfault.dsa." + cls], capture_output=True, text=True, cwd=BASE)
    return r.returncode, r.stdout, r.stderr


def build_go(solve_name, func_node, classes, tests):
    raise NotImplementedError("go not yet implemented")

def build_java(solve_name, func_node, classes, tests):
    raise NotImplementedError("java not yet implemented")

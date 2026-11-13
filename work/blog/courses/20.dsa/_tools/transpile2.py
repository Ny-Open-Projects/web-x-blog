#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python -> Go/Java/TS transpiler (focused subset) for DSA remediation.
Supports: single solve fn, int/number/list/str/dict/set IO, recursion,
if/elif/else, for..in (range/enumerate/list/dict.items/zip), while,
common builtins, list comp (simple), TreeNode/ListNode (attribute access + helpers).
Unsupported constructs raise TranspileError -> caller records fail.
"""
import ast, json, sys, os, subprocess, re

REPO = "/Users/Wang/Code/github/web-x-blog/work/blog/courses/20.dsa"
HELPERS = {"print","build_list","print_list","build_tree","to_list","list_to_arr",
           "demo","helper","main","TreeNode","ListNode","Solution","min","max","abs",
           "len","sorted","range","enumerate","zip","list","dict","set","sum","int",
           "str","float","bool","print_list_node","build_linked_list","get_node"}

class TranspileError(Exception):
    pass

def find_solve(src):
    tree = ast.parse(src)
    mb=None
    for n in tree.body:
        if isinstance(n, ast.If): mb=n.body; break
    for n in (mb or []):
        if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call):
            f=n.value.func
            if isinstance(f, ast.Name) and f.id not in HELPERS: return f.id
    for n in tree.body:
        if isinstance(n, ast.FunctionDef) and n.name not in HELPERS: return n.name
    return None

# ---------- type inference ----------
def is_tree_use(fn, pname):
    for n in ast.walk(fn):
        if isinstance(n, ast.Attribute):
            b=n.value
            if isinstance(b, ast.Name) and b.id==pname and n.attr in ('left','right','val'):
                return True
    return False
def is_list_use(fn, pname):
    for n in ast.walk(fn):
        if isinstance(n, ast.Subscript) and isinstance(n.value, ast.Name) and n.value.id==pname:
            return True
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id=='len' and n.args and isinstance(n.args[0], ast.Name) and n.args[0].id==pname:
            return True
    return False

def infer_params(fn):
    out=[]
    for a in fn.args.args:
        nm=a.arg
        if is_tree_use(fn, nm): out.append((nm,'tree'))
        elif is_list_use(fn, nm): out.append((nm,'list'))
        else: out.append((nm,'int'))
    return out

def infer_return(fn):
    # look at return statements
    types=set()
    for n in ast.walk(fn):
        if isinstance(n, ast.Return) and n.value is not None:
            t=rtype(n.value)
            if t: types.add(t)
    if 'tree' in types: return 'tree'
    if 'listnode' in types: return 'listnode'
    if 'bool' in types: return 'bool'
    if 'list' in types: return 'list'
    if 'str' in types: return 'str'
    if 'num' in types: return 'num'
    if types: return next(iter(types))
    return 'int'

def rtype(node):
    if isinstance(node, ast.Constant):
        if isinstance(node.value,bool): return 'bool'
        if isinstance(node.value,int): return 'int'
        if isinstance(node.value,float): return 'num'
        if isinstance(node.value,str): return 'str'
        if node.value is None: return 'nil'
    if isinstance(node, ast.List): return 'list'
    if isinstance(node, ast.Dict): return 'dict'
    if isinstance(node, ast.Set): return 'set'
    if isinstance(node, ast.BoolOp): return 'bool'
    if isinstance(node, ast.Compare): return 'bool'
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not): return 'bool'
    if isinstance(node, ast.Call):
        if isinstance(node.func, ast.Name):
            fn=node.func.id
            if fn in ('len',): return 'int'
            if fn in ('int',): return 'int'
            if fn in ('str',): return 'str'
            if fn in ('min','max','abs'): return 'int'
            if fn in ('sorted',): return 'list'
            return None
        if isinstance(node.func, ast.Attribute):
            m=node.func.attr
            if m=='append': return 'nil'
            return None
    if isinstance(node, ast.BinOp):
        return 'int'
    if isinstance(node, ast.Name):
        return None
    return None

# ---------- expression translator ----------
class T:
    def __init__(self, lang): self.lang=lang; self.locals=set(); self.used_tree=False; self.used_ln=False
    def E(self, node):
        return self.expr(node)[0]
    def expr(self, node):
        lang=self.lang
        if isinstance(node, ast.Constant):
            v=node.value
            if isinstance(v,bool): return (("true" if v else "false"),'bool')
            if v is None: return (("null" if lang!='go' else "nil"),'nil')
            if isinstance(v,int): return (str(v),'int')
            if isinstance(v,float): return (repr(v),'num')
            if isinstance(v,str):
                s=v.replace('\\','\\\\').replace('"','\\"').replace('\n','\\n').replace('\t','\\t')
                return ('"'+s+'"','str')
            return (repr(v),'any')
        if isinstance(node, ast.Name):
            n=node.id
            if n=='True': return ('true','bool')
            if n=='False': return ('false','bool')
            if n=='None': return (('null' if lang!='go' else 'nil'),'nil')
            if n in self.locals: return (n, None)
            return (n, None)
        if isinstance(node, ast.Attribute):
            base,h=self.expr(node.value)
            if h=='tree' or (isinstance(node.value, ast.Name) and node.value.id in TREEVARS): self.used_tree=True
            if base in TREEVARS and node.attr in ('left','right','val'): self.used_tree=True
            if base in LNVARS and node.attr in ('next','val'): self.used_ln=True
            return (base+"."+node.attr, None)
        if isinstance(node, ast.BinOp):
            l,h1=self.expr(node.left); r,h2=self.expr(node.right)
            op=type(node.op).__name__
            m={'Add':'+','Sub':'-','Mult':'*','Div':'/','FloorDiv':'/','Mod':'%','Pow':'**',
               'BitAnd':'&','BitOr':'|','BitXor':'^','LShift':'<<','RShift':'>>'}
            if op=='Pow':
                if lang=='go': return ("int(math.Pow(float64("+l+"), float64("+r+")))",'int')
                if lang=='java': return ("(int)Math.pow("+l+","+r+")",'int')
                return ("Math.pow("+l+","+r+")",'num')
            if op=='Div' and lang=='go':
                # integer division when both int
                if h1=='int' and h2=='int':
                    return ("("+l+" / "+r+")",'int')
                return ("("+l+" / "+r+")",'num')
            return ("("+l+" "+m.get(op,op)+" "+r+")",'int')
        if isinstance(node, ast.BoolOp):
            vals=[self.expr(v)[0] for v in node.values]
            op=" && " if isinstance(node.op, ast.And) else " || "
            return ("("+op.join(vals)+")",'bool')
        if isinstance(node, ast.UnaryOp):
            v,h=self.expr(node.operand)
            if isinstance(node.op, ast.Not): return ("(!"+v+")",'bool')
            if isinstance(node.op, ast.USub): return ("(-"+v+")",h)
            return ("(+"+v+")",h)
        if isinstance(node, ast.Compare):
            return self.compare(node)
        if isinstance(node, ast.Call):
            return self.call(node)
        if isinstance(node, ast.Subscript):
            return self.subscript(node)
        if isinstance(node, ast.List):
            els=[self.expr(e)[0] for e in node.elts]
            return (self.listlit(els),'list')
        if isinstance(node, ast.Tuple):
            els=[self.expr(e)[0] for e in node.elts]
            return ("("+", ".join(els)+")",'tuple')
        if isinstance(node, ast.Dict):
            items=[(self.expr(k)[0],self.expr(v)[0]) for k,v in zip(node.keys,node.values)]
            if lang=='go':
                return ("map[int]int{"+",".join(k+":"+v for k,v in items)+"}",'dict')
            return ("new Map(["+",".join("["+k+","+v+"]" for k,v in items)+"])","dict")
        if isinstance(node, ast.Set):
            els=[self.expr(e)[0] for e in node.elts]
            if lang=='go':
                return ("setFrom(["+",".join(els)+"])",'set')
            return ("new Set(["+",".join(els)+"])",'set')
        if isinstance(node, ast.IfExp):
            c_=self.expr(node.test)[0]; t_=self.expr(node.body)[0]; f_=self.expr(node.orelse)[0]
            if lang=='go':
                return ("func() interface{} { if "+c_+" { return "+t_+" }; return "+f_+" }()",'any')
            return ("("+c_+" ? "+t_+" : "+f_+")",'any')
        if isinstance(node, ast.ListComp):
            return self.listcomp(node)
        raise TranspileError("expr "+type(node).__name__)
    def listlit(self, els):
        lang=self.lang
        if lang=='go': return "[]int{"+", ".join(els)+"}"
        if lang=='java': return "new int[]{"+", ".join(els)+"}"
        return "["+", ".join(els)+"]"
    def compare(self, node):
        lang=self.lang
        l,h=self.expr(node.left)
        parts=[l]
        code=l
        for op,comp in zip(node.ops, node.comparators):
            r,_=self.expr(comp)
            on=type(op).__name__
            if on=='In':
                return ("contains("+r+","+l+")",'bool') if lang!='go' else ("contains("+r+", "+l+")",'bool')
            if on=='NotIn':
                return ("!contains("+r+","+l+")",'bool')
            sm={'Eq':'==','NotEq':'!=','Lt':'<','LtE':'<=','Gt':'>','GtE':'>=','Is':'==','IsNot':'!='}
            sym=sm.get(on,'==')
            code=code+" "+sym+" "+r
        return ("("+code+")",'bool')
    def call(self, node):
        lang=self.lang
        f=node.func
        if isinstance(f, ast.Name):
            fn=f.id
            args=[self.expr(a)[0] for a in node.args]
            if fn=='len': return ("len("+",".join(args)+")",'int') if lang=='go' else ("("+",".join(args)+").length",'int')
            if fn=='int': return ("int("+args[0]+")",'int')
            if fn=='float': return ("float64("+args[0]+")" if lang=='go' else "float("+args[0]+")",'num')
            if fn=='str': return ("String("+args[0]+")" if lang=='java' else "String("+args[0]+")",'str')
            if fn=='abs': return ("int(math.Abs(float64("+args[0]+")))" if lang=='go' else "Math.abs("+args[0]+")",'int')
            if fn in ('min','max'):
                if lang=='go': return ((fn+"("+",".join(args)+")"),'int')
                return ("Math."+fn.capitalize()+"("+",".join(args)+")",'int')
            if fn=='sorted':
                if lang=='go': return ("sortedCopy("+args[0]+")",'list')
                if lang=='java': return ("sortedArr("+args[0]+")",'list')
                return ("[... "+args[0]+"].sort((a,b)=>a-b)",'list')
            if fn in ('list','set','dict','tuple','range','print'):
                return ("("+",".join(args)+")",'any')
            # user fn
            return (fn+"("+",".join(args)+")",'any')
        if isinstance(f, ast.Attribute):
            base,h=self.expr(f.value)
            if base in TREEVARS: self.used_tree=True
            if base in LNVARS: self.used_ln=True
            method=f.attr
            args=[self.expr(a)[0] for a in node.args]
            if method=='append':
                if lang=='go': return (base+".append("+",".join(args)+")",'nil')
                if lang=='java': return (base+".add("+",".join(args)+")",'nil')
                return (base+".push("+",".join(args)+")",'nil')
            if method=='get':
                if lang=='go': return (base+"["+args[0]+"]",'any')
                return (base+".get("+args[0]+")",'any')
            if method=='pop':
                if lang=='go': return (base+".pop()",'any')
                return (base+".pop()",'any')
            if method=='add':
                return (base+".add("+",".join(args)+")",'nil')
            return (base+"."+method+"("+",".join(args)+")",'any')
        raise TranspileError("call")
    def subscript(self, node):
        lang=self.lang
        v,h=self.expr(node.value)
        if isinstance(node.slice, ast.Slice):
            lo=self.expr(node.slice.lower)[0] if node.slice.lower else "0"
            hi=self.expr(node.slice.upper)[0] if node.slice.upper else (v+".length")
            if lang=='go': return (v+"["+lo+":"+hi+"]",'list')
            if lang=='java': return (v+".subList("+lo+","+hi+")",'list')
            return (v+".slice("+lo+","+hi+")",'list')
        s,_=self.expr(node.slice)
        if lang=='go': return (v+"["+s+"]",'any')
        return (v+"["+s+"]",'any')
    def listcomp(self, node):
        lang=self.lang
        g=node.generators[0]
        iter_,h=self.expr(g.iter)
        var=self.expr(g.target)[0] if isinstance(g.target, ast.Name) else "x"
        body=self.expr(node.elt)[0]
        conds=[self.expr(i)[0] for i in g.ifs]
        cond=" && ".join(conds) if conds else "true"
        if lang=='go':
            return ("func() []int { out:=[]int{}; for _, "+var+" := range "+iter_+" { if "+cond+" { out=append(out,"+body+") } }; return out }()")
        if lang=='java':
            return ("listComp("+iter_+", "+var+" -> "+cond+", "+var+" -> "+body+")")
        return ("("+iter_+").filter(("+var+") => ("+cond+")).map(("+var+") => ("+body+"))")

# ---------- statement translator ----------
def stmt(c, node, ind):
    lang=c.lang; pad="    "*ind
    if isinstance(node, ast.Return):
        if node.value is None: return pad+("return" if lang!='java' else "return;")
        v,_=c.expr(node.value)
        return pad+"return "+v+(";" if lang=='java' else "")
    if isinstance(node, ast.Assign):
        val,h=c.expr(node.value)
        out=[]
        for tgt in node.targets:
            if isinstance(tgt, ast.Name):
                nm=tgt.id
                if nm not in c.locals:
                    c.locals.add(nm)
                    out.append(pad+("var "+nm+" = "+val) if lang=='go' else (("let "+nm+" = "+val+";") if lang=='ts' else (nm+" := "+val if False else "auto "+nm+" = "+val)))
                    if lang=='java': out[-1]=pad+"var "+nm+" = "+val+";"  # placeholder; refine
                else:
                    out.append(pad+nm+" = "+val+(";" if lang=='java' else ""))
            elif isinstance(tgt, ast.Subscript):
                b,_=c.expr(tgt.value); s,_=c.expr(tgt.slice)
                out.append(pad+b+"["+s+"] = "+val+(";" if lang=='java' else ""))
            elif isinstance(tgt, ast.Attribute):
                b,_=c.expr(tgt.value)
                out.append(pad+b+"."+tgt.attr+" = "+val+(";" if lang=='java' else ""))
            elif isinstance(tgt, ast.Tuple):
                names=[x.id for x in tgt.elts]
                for nm in names: c.locals.add(nm)
                if lang=='go': out.append(pad+"var "+", ".join(names)+" = "+val)
                elif lang=='java': out.append(pad+"// unpack "+val)
                else: out.append(pad+"let ["+", ".join(names)+"] = "+val+";")
        return "\n".join(out)
    if isinstance(node, ast.AugAssign):
        tgt=c.expr(node.target)[0]; r,_=c.expr(node.value)
        op=type(node.op).__name__
        m={'Add':'+=','Sub':'-=','Mult':'*=','Div':'/=','Mod':'%='}
        return pad+tgt+" "+m.get(op,op)+" "+r+(";" if lang=='java' else "")
    if isinstance(node, ast.If):
        return st_if(c,node,ind)
    if isinstance(node, ast.For):
        return st_for(c,node,ind)
    if isinstance(node, ast.While):
        test,_=c.expr(node.test)
        body="\n".join(stmt(c,s,ind+1) for s in node.body)
        return pad+"for ("+test+") {\n"+body+"\n"+pad+"}" if lang!='java' else pad+"while ("+test+") {\n"+body+"\n"+pad+"}"
    if isinstance(node, ast.Expr):
        v,_=c.expr(node.value)
        if v.strip().startswith("/*") or v.strip()=="0": return ""
        return pad+v+(";" if lang=='java' else "")
    if isinstance(node, ast.Pass): return pad+"// pass"
    if isinstance(node, ast.Break): return pad+"break"+((";" if lang=='java' else ""))
    if isinstance(node, ast.Continue): return pad+"continue"+((";" if lang=='java' else ""))
    if isinstance(node, ast.FunctionDef):
        return st_func(c,node,ind)
    raise TranspileError("stmt "+type(node).__name__)

def st_if(c,node,ind):
    lang=c.lang; pad="    "*ind
    test,_=c.expr(node.test)
    out=[pad+"if ("+test+") {"]
    for s in node.body: out.append(stmt(c,s,ind+1))
    out.append(pad+"}")
    if node.orelse:
        if len(node.orelse)==1 and isinstance(node.orelse[0], ast.If):
            elsep=stmt(c,node.orelse[0],ind)  # produces "if (...) {..." at same indent
            out.append(pad+"else "+elsep[len(pad):])
            return "\n".join(out)
        out.append(pad+"else {")
        for s in node.orelse: out.append(stmt(c,s,ind+1))
        out.append(pad+"}")
    return "\n".join(out)

def st_for(c,node,ind):
    lang=c.lang; pad="    "*ind
    it=node.iter; target=node.target
    if isinstance(it, ast.Call) and isinstance(it.func, ast.Name) and it.func.id=='range':
        args=[c.expr(a)[0] for a in it.args]
        var=c.expr(target)[0] if isinstance(target, ast.Name) else "i"
        c.locals.add(var)
        lo,hi,step=("0",args[0],"1") if len(args)==1 else (args[0],args[1],"1") if len(args)==2 else (args[0],args[1],args[2])
        if lang=='go': return pad+"for "+var+" := "+lo+"; "+var+" < "+hi+"; "+var+" += "+step+" {\n"+"\n".join(stmt(c,s,ind+1) for s in node.body)+"\n"+pad+"}"
        if lang=='java': return pad+"for (int "+var+" = "+lo+"; "+var+" < "+hi+"; "+var+" += "+step+") {\n"+"\n".join(stmt(c,s,ind+1) for s in node.body)+"\n"+pad+"}"
        return pad+"for (let "+var+" = "+lo+"; "+var+" < "+hi+"; "+var+" += "+step+") {\n"+"\n".join(stmt(c,s,ind+1) for s in node.body)+"\n"+pad+"}"
    iter_,h=c.expr(it)
    var=c.expr(target)[0] if isinstance(target, ast.Name) else "x"
    c.locals.add(var)
    if lang=='go':
        return pad+"for _, "+var+" := range "+iter_+" {\n"+"\n".join(stmt(c,s,ind+1) for s in node.body)+"\n"+pad+"}"
    if lang=='java':
        return pad+"for (var "+var+" : "+iter_+") {\n"+"\n".join(stmt(c,s,ind+1) for s in node.body)+"\n"+pad+"}"
    return pad+"for (const "+var+" of "+iter_+") {\n"+"\n".join(stmt(c,s,ind+1) for s in node.body)+"\n"+pad+"}"

def st_func(c,node,ind):
    lang=c.lang; pad="    "*ind
    name=node.name
    # nested helper: just translate body as statements
    c2=T(lang); 
    for a in node.args.args: c2.locals.add(a.arg)
    body="\n".join(stmt(c2,s,ind+1) for s in node.body)
    ret=infer_return(node)
    rt=GO_RET[ret] if lang=='go' else (JAVA_RET[ret] if lang=='java' else TS_RET[ret])
    params=", ".join(a.arg+" "+GO_ARG[ret] for a in node.args.args) if lang=='go' else \
           (", ".join("int "+a.arg for a in node.args.args) if lang=='java' else ", ".join(a.arg for a in node.args.args))
    return pad+"func "+name+"("+params+") "+rt+" {\n"+body+"\n"+pad+"}" if lang=='go' else \
           (pad+"int "+name+"("+params+") {\n"+body+"\n"+pad+"}" if lang=='java' else pad+"function "+name+"("+params+") {\n"+body+"\n"+pad+"}")

# type maps
GO_RET={'int':'int','num':'float64','str':'string','bool':'bool','list':'[]int','liststr':'[]string',
        'tree':'*TreeNode','listnode':'*ListNode','dict':'map[int]int','set':'set[int]','nil':'interface{}','any':'interface{}'}
JAVA_RET={'int':'int','num':'double','str':'String','bool':'boolean','list':'int[]','liststr':'String[]',
          'tree':'TreeNode','listnode':'ListNode','dict':'Map<Integer,Integer>','set':'Set<Integer>','nil':'Object','any':'Object'}
TS_RET={'int':'number','num':'number','str':'string','bool':'boolean','list':'number[]','liststr':'string[]',
        'tree':'TreeNode|null','listnode':'ListNode|null','dict':'Map<number,number>','set':'Set<number>','nil':'any','any':'any'}
GO_ARG={'int':'int','num':'float64','str':'string','bool':'bool','list':'[]int','liststr':'[]string',
        'tree':'*TreeNode','listnode':'*ListNode','dict':'map[int]int','set':'set[int]','nil':'interface{}','any':'interface{}'}

TREEVARS=set(); LNVARS=set()

# ---------- file emission ----------
def emit(lang, pyfile, src, fname, fn, mode, cases_in, cases_out):
    global TREEVARS, LNVARS
    params=infer_params(fn)
    ret=infer_return(fn)
    TREEVARS=set(p for p,t in params if t=='tree')
    LNVARS=set(p for p, t in params if t=='listnode')
    c=T(lang)
    for p,t in params: c.locals.add(p)
    body="\n".join(stmt(c,s,1) for s in fn.body)
    # fix java locals: we emitted "var x = ..." placeholder; for java use proper type inference is hard; do simple: replace with final guessed
    # We'll just emit go/java/ts here with best-effort.
    if lang=='go':
        return emit_go(params, ret, fname, body, mode, cases_in, cases_out, c.used_tree, c.used_ln)
    if lang=='java':
        return emit_java(params, ret, fname, body, mode, cases_in, cases_out, c.used_tree, c.used_ln)
    return emit_ts(params, ret, fname, body, mode, cases_in, cases_out, c.used_tree, c.used_ln)

# (emitters defined in separate module to keep size manageable)

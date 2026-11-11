#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Focused Python -> Go/Java/TS transpiler for DSA remediation.
Common subset: single solve fn, int/number/list/str IO, recursion, if/elif/else,
for..in(range/enumerate/list), while, common builtins, list comp (simple),
TreeNode/ListNode attribute access (with helpers). Unsupported -> TranspileError.
"""
import ast, json, sys, os

REPO = "/Users/Wang/Code/webfault-ai/dsa"
HELPERS = {"print","build_list","print_list","build_tree","to_list","list_to_arr",
           "demo","helper","main","TreeNode","ListNode","Solution","min","max","abs",
           "len","sorted","range","enumerate","zip","list","dict","set","sum","int",
           "str","float","bool","print_list_node","build_linked_list","get_node"}

class TP(Exception): pass

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

TREEVARS=set(); LNVARS=set()

def is_tree_use(fn, p):
    for n in ast.walk(fn):
        if isinstance(n, ast.Attribute) and isinstance(n.value, ast.Name) and n.value.id==p and n.attr in ('left','right','val'):
            return True
    return False
def is_list_use(fn, p):
    for n in ast.walk(fn):
        if isinstance(n, ast.Subscript) and isinstance(n.value, ast.Name) and n.value.id==p: return True
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id=='len' and n.args and isinstance(n.args[0], ast.Name) and n.args[0].id==p: return True
    return False

def infer_params(fn):
    out=[]
    for a in fn.args.args:
        if is_tree_use(fn,a.arg): out.append((a.arg,'tree'))
        elif is_list_use(fn,a.arg): out.append((a.arg,'list'))
        else: out.append((a.arg,'int'))
    return out

def infer_return(fn):
    ptypes={a:t for a,t in infer_params(fn)}
    types=set()
    for n in ast.walk(fn):
        if isinstance(n, ast.Return) and n.value is not None:
            t=rtype(n.value, ptypes)
            if t: types.add(t)
    for order in ('tree','listnode','bool','list','str','num','int'):
        if order in types: return order
    return 'int'

def rtype(node, ptypes=None):
    if ptypes is None: ptypes={}
    if isinstance(node, ast.Constant):
        if isinstance(node.value,bool): return 'bool'
        if isinstance(node.value,int): return 'int'
        if isinstance(node.value,float): return 'num'
        if isinstance(node.value,str): return 'str'
        return 'nil'
    if isinstance(node, ast.List): return 'list'
    if isinstance(node, ast.Dict): return 'dict'
    if isinstance(node, ast.Set): return 'set'
    if isinstance(node, ast.BoolOp): return 'bool'
    if isinstance(node, ast.Compare): return 'bool'
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not): return 'bool'
    if isinstance(node, ast.Name):
        nm=node.id
        if nm in ptypes: return ptypes[nm]
        return None
    if isinstance(node, ast.Attribute):
        if node.attr in ('val',): return 'int'
        if node.attr in ('left','right'): return 'tree'
        if node.attr=='next': return 'listnode'
        return None
    if isinstance(node, ast.Call):
        if isinstance(node.func, ast.Name):
            fn=node.func.id
            if fn in ('len','int','min','max','abs'): return 'int'
            if fn=='str': return 'str'
            if fn=='sorted': return 'list'
            if fn in ptypes: return ptypes[fn]
            return None
        if isinstance(node.func, ast.Attribute) and node.func.attr=='append': return 'nil'
        return None
    if isinstance(node, ast.BinOp): return 'int'
    return None

class C:
    def __init__(self, lang): self.lang=lang; self.locals=set(); self.ut=False; self.ul=False; self.mapvars=set()
    def ex(self, n): return self.expr(n)[0]
    def expr(self, n):
        L=self.lang
        if isinstance(n, ast.Constant):
            v=n.value
            if isinstance(v,bool): return (('true' if v else 'false'),'bool')
            if v is None: return (('null' if L!='go' else 'nil'),'nil')
            if isinstance(v,int): return (str(v),'int')
            if isinstance(v,float): return (repr(v),'num')
            if isinstance(v,str):
                s=v.replace('\\','\\\\').replace('"','\\"').replace('\n','\\n').replace('\t','\\t')
                return ('"'+s+'"','str')
            return (repr(v),'any')
        if isinstance(n, ast.Name):
            i=n.id
            if i=='True': return ('true','bool')
            if i=='False': return ('false','bool')
            if i=='None': return (('null' if L!='go' else 'nil'),'nil')
            return (i, None)
        if isinstance(n, ast.Attribute):
            b,h=self.expr(n.value)
            if b in TREEVARS and n.attr in ('left','right','val'): self.ut=True
            if b in LNVARS and n.attr in ('next','val'): self.ul=True
            return (b+"."+n.attr, None)
        if isinstance(n, ast.BinOp):
            l,h1=self.expr(n.left); r,h2=self.expr(n.right)
            op=type(n.op).__name__
            m={'Add':'+','Sub':'-','Mult':'*','Div':'/','FloorDiv':'/','Mod':'%','Pow':'**',
               'BitAnd':'&','BitOr':'|','BitXor':'^','LShift':'<<','RShift':'>>'}
            if op=='Pow':
                if L=='go': return ("int(math.Pow(float64("+l+"), float64("+r+")))",'int')
                if L=='java': return ("(int)Math.pow("+l+","+r+")",'int')
                return ("Math.pow("+l+","+r+")",'num')
            if op=='Div' and L=='go' and h1=='int' and h2=='int':
                return ("("+l+" / "+r+")",'int')
            return ("("+l+" "+m.get(op,op)+" "+r+")",'int')
        if isinstance(n, ast.BoolOp):
            return ("("+(" && " if isinstance(n.op,ast.And) else " || ").join(self.expr(v)[0] for v in n.values)+")",'bool')
        if isinstance(n, ast.UnaryOp):
            v,h=self.expr(n.operand)
            if isinstance(n.op, ast.Not): return ("(!"+v+")",'bool')
            if isinstance(n.op, ast.USub): return ("(-"+v+")",h)
            return ("(+"+v+")",h)
        if isinstance(n, ast.Compare): return self._cmp(n)
        if isinstance(n, ast.Call): return self._call(n)
        if isinstance(n, ast.Subscript): return self._sub(n)
        if isinstance(n, ast.List):
            els=[self.expr(e)[0] for e in n.elts]
            return (self._list(els),'list')
        if isinstance(n, ast.Tuple):
            return ("("+", ".join(self.expr(e)[0] for e in n.elts)+")",'tuple')
        if isinstance(n, ast.Dict):
            items=[(self.expr(k)[0],self.expr(v)[0]) for k,v in zip(n.keys,n.values)]
            if L=='go': return ("map[int]int{"+",".join(k+":"+v for k,v in items)+"}",'dict')
            return ("new Map(["+",".join("["+k+","+v+"]" for k,v in items)+"])","dict")
        if isinstance(n, ast.Set):
            els=[self.expr(e)[0] for e in n.elts]
            if L=='go': return ("setFrom([]int{"+",".join(els)+"})",'set')
            return ("new Set(["+",".join(els)+"])","set")
        if isinstance(n, ast.IfExp):
            c_=self.expr(n.test)[0]; t_=self.expr(n.body)[0]; f_=self.expr(n.orelse)[0]
            if L=='go': return ("func() interface{} { if "+c_+" { return "+t_+"}; return "+f_+" }()",'any')
            return ("("+c_+" ? "+t_+" : "+f_+")",'any')
        if isinstance(n, ast.ListComp): return self._lc(n)
        raise TP("expr "+type(n).__name__)
    def _list(self, els):
        L=self.lang
        if L=='go': return "[]int{"+", ".join(els)+"}"
        if L=='java': return "new int[]{"+", ".join(els)+"}"
        return "["+", ".join(els)+"]"
    def _cmp(self, n):
        L=self.lang
        l,_=self.expr(n.left); code=l
        for op,comp in zip(n.ops,n.comparators):
            r,_=self.expr(comp); on=type(op).__name__
            # container for 'in': the right operand (comp)
            if on=='In':
                if L=='go' and (r.strip() in self.mapvars or r.strip().startswith('memo')):
                    return ("func() bool { _, _ok := "+r+"["+l+"]; return _ok }()",'bool')
                if L=='ts' and r.strip() in self.mapvars:
                    return (r+".has("+l+")",'bool')
                if L=='java' and r.strip() in self.mapvars:
                    return (r+".containsKey("+l+")",'bool')
                return ("contains("+r+", "+l+")",'bool')
            if on=='NotIn':
                if L=='go' and (r.strip() in self.mapvars or r.strip().startswith('memo')):
                    return ("func() bool { _, _ok := "+r+"["+l+"]; return !_ok }()",'bool')
                if L=='ts' and r.strip() in self.mapvars:
                    return ("!"+r+".has("+l+")",'bool')
                if L=='java' and r.strip() in self.mapvars:
                    return ("!"+r+".containsKey("+l+")",'bool')
                return ("!contains("+r+", "+l+")",'bool')
            sm={'Eq':'==','NotEq':'!=','Lt':'<','LtE':'<=','Gt':'>','GtE':'>=','Is':'==','IsNot':'!='}
            code+=" "+sm.get(on,'==')+" "+r
        return ("("+code+")",'bool')
    def _call(self, n):
        L=self.lang; f=n.func
        if isinstance(f, ast.Name):
            fn=f.id; args=[self.expr(a)[0] for a in n.args]
            if fn=='len': return (("len("+",".join(args)+")") if L=='go' else ("("+",".join(args)+").length"),'int')
            if fn=='int': return ("int("+args[0]+")",'int')
            if fn=='float': return (("float64("+args[0]+")") if L=='go' else "float("+args[0]+")",'num')
            if fn=='str': return ("String("+args[0]+")",'str')
            if fn=='abs': return (("int(math.Abs(float64("+args[0]+")))") if L=='go' else "Math.abs("+args[0]+")",'int')
            if fn in ('min','max'):
                if L=='go': return (fn+"("+",".join(args)+")",'int')
                return ("Math."+fn.capitalize()+"("+",".join(args)+")",'int')
            if fn=='sorted':
                if L=='go': return ("sortedCopy("+args[0]+")",'list')
                if L=='java': return ("sortedArr("+args[0]+")",'list')
                return ("[..."+args[0]+"].sort((a,b)=>a-b)",'list')
            if fn in ('list','set','dict','tuple','range','print'): return ("("+",".join(args)+")",'any')
            return (fn+"("+",".join(args)+")",'any')
        if isinstance(f, ast.Attribute):
            b,h=self.expr(f.value)
            if b in TREEVARS: self.ut=True
            if b in LNVARS: self.ul=True
            m=f.attr; args=[self.expr(a)[0] for a in n.args]
            if m=='append':
                if L=='go': return (b+".append("+",".join(args)+")",'nil')
                if L=='java': return (b+".add("+",".join(args)+")",'nil')
                return (b+".push("+",".join(args)+")",'nil')
            if m=='get': return (b+"["+args[0]+"]" if L=='go' else b+".get("+args[0]+")",'any')
            if m=='pop': return (b+".pop()" if L!='go' else b+".pop()",'any')
            if m=='add': return (b+".add("+",".join(args)+")",'nil')
            return (b+"."+m+"("+",".join(args)+")",'any')
        raise TP("call")
    def _sub(self, n):
        L=self.lang; v,_=self.expr(n.value)
        if isinstance(n.slice, ast.Slice):
            lo=self.expr(n.slice.lower)[0] if n.slice.lower else "0"
            hi=self.expr(n.slice.upper)[0] if n.slice.upper else (v+".length")
            if L=='go': return (v+"["+lo+":"+hi+"]",'list')
            if L=='java': return (v+".subList("+lo+","+hi+")",'list')
            return (v+".slice("+lo+","+hi+")",'list')
        s,_=self.expr(n.slice)
        return (v+"["+s+"]",'any')
    def _lc(self, n):
        L=self.lang; g=n.generators[0]
        it,h=self.expr(g.iter); var=self.expr(g.target)[0] if isinstance(g.target,ast.Name) else "x"
        body=self.expr(n.elt)[0]; conds=[self.expr(i)[0] for i in g.ifs]
        cond=" && ".join(conds) if conds else "true"
        if L=='go': return ("func() []int { o:=[]int{}; for _, "+var+" := range "+it+" { if "+cond+" { o=append(o,"+body+") } }; return o }()")
        if L=='java': return ("listComp("+it+", "+var+" -> "+cond+", "+var+" -> "+body+")")
        return ("("+it+").filter(("+var+") => ("+cond+")).map(("+var+") => ("+body+"))")

RET={'int':'int','num':'float64','str':'string','bool':'bool','list':'[]int','liststr':'[]string',
     'tree':'*TreeNode','listnode':'*ListNode','dict':'map[int]int','set':'set[int]','nil':'interface{}','any':'interface{}'}
RETJ={'int':'int','num':'double','str':'String','bool':'boolean','list':'int[]','liststr':'String[]',
      'tree':'TreeNode','listnode':'ListNode','dict':'Map<Integer,Integer>','set':'Set<Integer>','nil':'Object','any':'Object'}
RETT={'int':'number','num':'number','str':'string','bool':'boolean','list':'number[]','liststr':'string[]',
      'tree':'TreeNode|null','listnode':'ListNode|null','dict':'Map<number,number>','set':'Set<number>','nil':'any','any':'any'}

def stmt(c, n, ind):
    L=c.lang; pad="    "*ind
    if isinstance(n, ast.Return):
        if n.value is None: return pad+("return" if L!='java' else "return;")
        v,_=c.expr(n.value); return pad+"return "+v+(";" if L=='java' else "")
    if isinstance(n, ast.Assign):
        out=[]
        for t in n.targets:
            if isinstance(t, ast.Tuple):
                rhss=[c.expr(e)[0] for e in n.value.elts]
                temps=[]
                for i,r in enumerate(rhss):
                    tn="_t%d"%(id(n)*100+i)
                    c.locals.add(tn)
                    if L=='go': out.append(pad+tn+" := "+r)
                    elif L=='java': out.append(pad+"var "+tn+" = "+r+";")
                    else: out.append(pad+"let "+tn+" = "+r+";")
                    temps.append(tn)
                for lhs,tn in zip(t.elts, temps):
                    if isinstance(lhs, ast.Name):
                        if lhs.id not in c.locals:
                            c.locals.add(lhs.id)
                            if L=='go': out.append(pad+lhs.id+" := "+tn)
                            elif L=='java': out.append(pad+"var "+lhs.id+" = "+tn+";")
                            else: out.append(pad+"let "+lhs.id+" = "+tn+";")
                        else: out.append(pad+lhs.id+" = "+tn+(";" if L=='java' else ""))
                    elif isinstance(lhs, ast.Subscript):
                        b,_=c.expr(lhs.value); s,_=c.expr(lhs.slice)
                        out.append(pad+b+"["+s+"] = "+tn+(";" if L=='java' else ""))
                    elif isinstance(lhs, ast.Attribute):
                        b,_=c.expr(lhs.value); out.append(pad+b+"."+lhs.attr+" = "+tn+(";" if L=='java' else ""))
                return "\n".join(out)
            val,h=c.expr(n.value)
            if isinstance(t, ast.Name):
                nm=t.id
                if nm not in c.locals:
                    c.locals.add(nm)
                    if L=='go': out.append(pad+nm+" := "+val)
                    elif L=='java': out.append(pad+"var "+nm+" = "+val+";")
                    else: out.append(pad+"let "+nm+" = "+val+";")
                else: out.append(pad+nm+" = "+val+(";" if L=='java' else ""))
            elif isinstance(t, ast.Subscript):
                b,_=c.expr(t.value); s,_=c.expr(t.slice)
                out.append(pad+b+"["+s+"] = "+val+(";" if L=='java' else ""))
            elif isinstance(t, ast.Attribute):
                b,_=c.expr(t.value); out.append(pad+b+"."+t.attr+" = "+val+(";" if L=='java' else ""))
        return "\n".join(out)
    if isinstance(n, ast.AugAssign):
        t=c.expr(n.target)[0]; r,_=c.expr(n.value); op=type(n.op).__name__
        m={'Add':'+=','Sub':'-=','Mult':'*=','Div':'/=','Mod':'%='}
        return pad+t+" "+m.get(op,op)+" "+r+(";" if L=='java' else "")
    if isinstance(n, ast.If): return s_if(c,n,ind)
    if isinstance(n, ast.For): return s_for(c,n,ind)
    if isinstance(n, ast.While):
        t,_=c.expr(n.test); body="\n".join(stmt(c,s,ind+1) for s in n.body)
        return pad+("for ("+t+") {\n"+body+"\n"+pad+"}" if L!='java' else "while ("+t+") {\n"+body+"\n"+pad+"}")
    if isinstance(n, ast.Expr):
        v,_=c.expr(n.value)
        if v.strip().startswith("/*") or v.strip()=="0": return ""
        return pad+v+(";" if L=='java' else "")
    if isinstance(n, ast.Pass): return pad+"// pass"
    if isinstance(n, ast.Break): return pad+"break"+((";" if L=='java' else ""))
    if isinstance(n, ast.Continue): return pad+"continue"+((";" if L=='java' else ""))
    if isinstance(n, ast.FunctionDef): return s_func(c,n,ind)
    raise TP("stmt "+type(n).__name__)

def s_if(c,n,ind):
    L=c.lang; pad="    "*ind; t,_=c.expr(n.test)
    out=[pad+"if ("+t+") {"]
    for s in n.body: out.append(stmt(c,s,ind+1))
    out.append(pad+"}")
    if n.orelse:
        if len(n.orelse)==1 and isinstance(n.orelse[0], ast.If):
            e=stmt(c,n.orelse[0],ind); out.append(pad+"else "+e[len(pad):]); return "\n".join(out)
        out.append(pad+"else {")
        for s in n.orelse: out.append(stmt(c,s,ind+1))
        out.append(pad+"}")
    return "\n".join(out)

def s_for(c,n,ind):
    L=c.lang; pad="    "*ind; it=n.iter; tg=n.target
    if isinstance(it, ast.Call) and isinstance(it.func, ast.Name) and it.func.id=='range':
        a=[c.expr(x)[0] for x in it.args]
        var=c.expr(tg)[0] if isinstance(tg,ast.Name) else "i"; c.locals.add(var)
        lo,hi,st=("0",a[0],"1") if len(a)==1 else (a[0],a[1],"1") if len(a)==2 else (a[0],a[1],a[2])
        if L=='go': return pad+"for "+var+" := "+lo+"; "+var+" < "+hi+"; "+var+" += "+st+" {\n"+"\n".join(stmt(c,s,ind+1) for s in n.body)+"\n"+pad+"}"
        if L=='java': return pad+"for (int "+var+" = "+lo+"; "+var+" < "+hi+"; "+var+" += "+st+") {\n"+"\n".join(stmt(c,s,ind+1) for s in n.body)+"\n"+pad+"}"
        return pad+"for (let "+var+" = "+lo+"; "+var+" < "+hi+"; "+var+" += "+st+") {\n"+"\n".join(stmt(c,s,ind+1) for s in n.body)+"\n"+pad+"}"
    ite,h=c.expr(it); var=c.expr(tg)[0] if isinstance(tg,ast.Name) else "x"; c.locals.add(var)
    if L=='go': return pad+"for _, "+var+" := range "+ite+" {\n"+"\n".join(stmt(c,s,ind+1) for s in n.body)+"\n"+pad+"}"
    if L=='java': return pad+"for (var "+var+" : "+ite+") {\n"+"\n".join(stmt(c,s,ind+1) for s in n.body)+"\n"+pad+"}"
    return pad+"for (const "+var+" of "+ite+") {\n"+"\n".join(stmt(c,s,ind+1) for s in n.body)+"\n"+pad+"}"

def s_func(c,n,ind):
    L=c.lang; pad="    "*ind; name=n.name
    c2=C(L)
    for a in n.args.args: c2.locals.add(a.arg)
    body="\n".join(stmt(c2,s,ind+1) for s in n.body)
    rt=infer_return(n)
    rtype=RET[rt] if L=='go' else (RETJ[rt] if L=='java' else RETT[rt])
    # param types: infer from usage
    pt=[]
    for a in n.args.args:
        if a.arg in TREEVARS: pt.append(('*TreeNode' if L=='go' else ('TreeNode' if L=='java' else 'TreeNode|null')))
        elif a.arg in LNVARS: pt.append(('*ListNode' if L=='go' else ('ListNode' if L=='java' else 'ListNode|null')))
        else: pt.append('int')
    params=", ".join(a.arg+" "+t for a,t in zip([a.arg for a in n.args.args],pt)) if L=='go' else \
           (", ".join("int "+a.arg for a in n.args.args) if L=='java' else ", ".join(a.arg for a in n.args.args))
    if L=='go': return pad+"func "+name+"("+params+") "+rtype+" {\n"+body+"\n"+pad+"}"
    if L=='java': return pad+"int "+name+"("+params+") {\n"+body+"\n"+pad+"}"
    return pad+"function "+name+"("+params+") {\n"+body+"\n"+pad+"}"

# ---------- top-level emit ----------
def build(lang, src, fname, fn, mode, cases_in, cases_out):
    global TREEVARS, LNVARS
    all_params=infer_params(fn); ret=infer_return(fn)
    ndef=len(fn.args.defaults) if hasattr(fn.args,'defaults') else 0
    req=all_params[:len(all_params)-ndef]
    defl=all_params[len(all_params)-ndef:]
    # memoization (defaulted params) only supported in go
    if defl and lang!='go':
        raise TP("defaulted/memoized params not supported in "+lang)
    TREEVARS={p for p,t in req if t=='tree'}; LNVARS={p for p,t in req if t=='listnode'}
    c=C(lang)
    for p,t in all_params: c.locals.add(p)
    c.mapvars=set(p for p,t in defl)  # defaulted params treated as map[int]int (go)
    # also any req param used as dict
    for p,t in req:
        if t=='dict': c.mapvars.add(p)
    try:
        body="\n".join(stmt(c,s,1) for s in fn.body)
    except TP as e:
        raise TP(str(e)+" in "+fname)
    if defl and lang=='go':
        prefix="\n".join("    var %s map[int]int"%p for p,t in defl)
        body=prefix+"\n"+body
    params=req  # signature uses only required params
    if lang=='go': return go_file(params,ret,fname,body,mode,cases_in,cases_out,c.ut,c.ul)
    if lang=='java': return java_file(params,ret,fname,body,mode,cases_in,cases_out,c.ut,c.ul)
    return ts_file(params,ret,fname,body,mode,cases_in,cases_out,c.ut,c.ul)

# ============ EMITTERS ============
def lit(lang, val, ptype):
    """python value -> target literal for a param of given type."""
    if ptype in ('tree','listnode'):
        # val is a level-order array (list); emit as build call
        s=",".join(("null" if x is None else str(x)) for x in val)
        if lang=='go': return ('buildTree("'+s+'")') if ptype=='tree' else ('buildList("'+s+'")')
        if lang=='java': return ('buildTree("'+s+'")') if ptype=='tree' else ('buildList("'+s+'")')
        return ('buildTree("'+s+'")') if ptype=='tree' else ('buildList("'+s+'")')
    if ptype=='list':
        if lang=='go': return "[]int{"+",".join(str(x) for x in val)+"}"
        if lang=='java': return "new int[]{"+",".join(str(x) for x in val)+"}"
        return "["+",".join(str(x) for x in val)+"]"
    if ptype=='int':
        return str(val)
    if ptype=='str':
        return '"'+str(val).replace('"','\\"')+'"'
    # fallback
    if isinstance(val,list):
        if lang=='go': return "[]int{"+",".join(str(x) for x in val)+"}"
        return "["+",".join(str(x) for x in val)+"]"
    return str(val)

def go_file(params,ret,fname,body,mode,cases_in,cases_out,ut,ul):
    need_math='math.Pow' in body
    need_sort='sortedCopy' in body
    need_strings = ut or ul
    imps=['"fmt"','"os"']
    if need_math: imps.append('"math"')
    if need_sort: imps.append('"sort"')
    if need_strings: imps.append('"strings"')
    hdr="package main\nimport (\n"+("\n".join("    "+i for i in imps))+"\n)\n"
    helpers=[]
    if ret=='list' or any(t=='list' for _,t in params):
        helpers.append("func eqIntSlice(a,b []int) bool { if len(a)!=len(b) {return false}; for i:=range a { if a[i]!=b[i] {return false} }; return true }")
    if ut:
        helpers.append("""type TreeNode struct { val int; left *TreeNode; right *TreeNode }
func buildTree(s string) *TreeNode {
    if s=="" { return nil }
    parts:=strings.Split(s,",")
    if parts[0]=="null" { return nil }
    root:=&TreeNode{val:atoi(parts[0])}; q:=[]*TreeNode{root}; i:=1
    for i<len(parts) {
        cur:=q[0]; q=q[1:]
        if i<len(parts) && parts[i]!="null" { cur.left=&TreeNode{val:atoi(parts[i])}; q=append(q,cur.left) }; i++
        if i<len(parts) && parts[i]!="null" { cur.right=&TreeNode{val:atoi(parts[i])}; q=append(q,cur.right) }; i++
    }
    return root
}
func atoi(s string) int { v:=0; for _,c:=range s { if c>='0'&&c<='9' { v=v*10+int(c-'0') } }; return v }
func serializeTree(n *TreeNode) []int {
    if n==nil { return []int{} }
    out:=[]int{}; q:=[]*TreeNode{n}
    for len(q)>0 { x:=q[0]; q=q[1:]; if x==nil { out=append(out,-1); continue }; out=append(out,x.val); q=append(q,x.left); q=append(q,x.right) }
    for len(out)>0 && out[len(out)-1]==-1 { out=out[:len(out)-1] }
    return out
}""")
    if ul:
        helpers.append("""type ListNode struct { val int; next *ListNode }
func buildList(s string) *ListNode {
    if s=="" { return nil }
    parts:=strings.Split(s,",")
    head:=&ListNode{val:atoi(parts[0])}; p:=head
    for i:=1;i<len(parts);i++ { p.next=&ListNode{val:atoi(parts[i])}; p=p.next }
    return head
}
func serializeList(n *ListNode) []int { out:=[]int{}; for n!=nil { out=append(out,n.val); n=n.next }; return out }""")
    if need_sort:
        helpers.append("func sortedCopy(a []int) []int { b:=make([]int,len(a)); copy(b,a); sort.Ints(b); return b }")
    if 'contains(' in body:
        helpers.append("func contains(arr []int, v int) bool { for _,x:=range arr { if x==v {return true} }; return false }")
    if 'setFrom(' in body:
        helpers.append("func setFrom(a []int) map[int]bool { m:=map[int]bool{}; for _,x:=range a { m[x]=true }; return m }")
    # harness
    nfields=len(params)
    struct_fields=""
    for i,(p,t) in enumerate(params):
        gtype = ('*TreeNode' if t=='tree' else ('*ListNode' if t=='listnode' else ('[]int' if t=='list' else ('string' if t=='str' else 'int'))))
        struct_fields+=("        in%d %s\n"%(i,gtype))
    want_type = ('[]int' if ret in ('list','tree','listnode') else ('string' if ret=='str' else ('float64' if ret=='num' else ('bool' if ret=='bool' else 'int'))))
    struct_fields+=("        want %s\n"%want_type)
    call_args=", ".join("c.in%d"%i for i in range(nfields))
    # compare
    if ret in ('tree','listnode'):
        cmp="if !eqIntSlice(serialize"+("Tree" if ret=='tree' else "List")+"(got), c.want) {"
    elif ret=='list':
        cmp="if !eqIntSlice(got, c.want) {"
    elif ret=='str':
        cmp="if got != c.want {"
    elif ret=='bool':
        cmp="if got != c.want {"
    else:
        cmp="if got != c.want {"
    case_entries=[]
    for ci,(cin,cout) in enumerate(zip(cases_in,cases_out)):
        ins=", ".join(lit('go',cin[i],params[i][1]) for i in range(nfields))
        case_entries.append("        {"+ins+", "+cout+"},")
    # function signature
    ptgo=[]
    for p,t in params:
        ptgo.append((p, '*TreeNode' if t=='tree' else ('*ListNode' if t=='listnode' else ('[]int' if t=='list' else ('string' if t=='str' else 'int')))))
    sig="func "+fname+"("+", ".join(a+" "+b for a,b in ptgo)+") "+RET[ret]+" {\n"+body+"\n}"
    harness=("func main() {\n    type tc struct {\n"+struct_fields+"    }\n    cases:=[]tc{\n"+("\n".join(case_entries))+"\n    }\n    ok:=true\n    for _,c:=range cases {\n        got:="+fname+"("+call_args+")\n        "+cmp+" ok=false; fmt.Printf(\"FAIL %v got %v want %v\\n\", c.in0, got, c.want) }\n    }\n    if !ok { os.Exit(1) }\n    fmt.Println(\"PASS\")\n}")
    return hdr+("\n".join(helpers)+"\n")+sig+"\n\n"+harness

def java_file(params,ret,fname,body,mode,cases_in,cases_out,ut,ul):
    cls="LcSol"
    hdr="package com.webfault.dsa;\nimport java.util.*;\n"
    helpers=[]
    if ret=='list' or any(t=='list' for _,t in params):
        helpers.append("static boolean eqInt(int[] a,int[] b){ if(a.length!=b.length) return false; for(int i=0;i<a.length;i++) if(a[i]!=b[i]) return false; return true; }")
    if ut:
        helpers.append("""static class TreeNode { int val; TreeNode left,right; TreeNode(int v){val=v;} }
static TreeNode buildTree(String s){ if(s.isEmpty()) return null; String[] p=s.split(","); if(p[0].equals("null")) return null; TreeNode root=new TreeNode(Integer.parseInt(p[0])); Queue<TreeNode> q=new LinkedList<>(); q.add(root); int i=1; while(i<p.length){ TreeNode cur=q.poll(); if(!p[i].equals("null")){ cur.left=new TreeNode(Integer.parseInt(p[i])); q.add(cur.left);} i++; if(i<p.length && !p[i].equals("null")){ cur.right=new TreeNode(Integer.parseInt(p[i])); q.add(cur.right);} i++; } return root; }
static List<Integer> serTree(TreeNode n){ List<Integer> out=new ArrayList<>(); if(n==null) return out; Queue<TreeNode> q=new LinkedList<>(); q.add(n); while(!q.isEmpty()){ TreeNode x=q.poll(); if(x==null){ out.add(-1); continue;} out.add(x.val); q.add(x.left); q.add(x.right);} while(out.size()>0 && out.get(out.size()-1)==-1) out.remove(out.size()-1); return out; }""")
    if ul:
        helpers.append("""static class ListNode { int val; ListNode next; ListNode(int v){val=v;} }
static ListNode buildList(String s){ String[] p=s.split(","); ListNode head=new ListNode(Integer.parseInt(p[0])); ListNode p2=head; for(int i=1;i<p.length;i++){ p2.next=new ListNode(Integer.parseInt(p[i])); p2=p2.next;} return head; }
static List<Integer> serList(ListNode n){ List<Integer> out=new ArrayList<>(); while(n!=null){ out.add(n.val); n=n.next;} return out; }""")
    if 'sortedArr' in body:
        helpers.append("static int[] sortedArr(int[] a){ int[] b=a.clone(); Arrays.sort(b); return b; }")
    if 'contains(' in body:
        helpers.append("static boolean contains(int[] a,int v){ for(int x:a) if(x==v) return true; return false; }")
    if 'listComp' in body:
        helpers.append("static List<Integer> listComp(int[] it, java.util.function.Predicate<Integer> p, java.util.function.Function<Integer,Integer> f){ List<Integer> o=new ArrayList<>(); for(int x:it) if(p.test(x)) o.add(f.apply(x)); return o; }")
    # method signature
    pt=[]
    for p,t in params:
        pt.append(('TreeNode' if t=='tree' else ('ListNode' if t=='listnode' else ('int[]' if t=='list' else ('String' if t=='str' else 'int')))))
    rt=('int[]' if ret in ('list','tree','listnode') else ('String' if ret=='str' else ('double' if ret=='num' else ('boolean' if ret=='bool' else 'int'))))
    # fix body to use var for locals (already emitted 'var x = ...') ok in java12
    nfields=len(params)
    entries=[]
    for cin,cout in zip(cases_in,cases_out):
        ins=", ".join(lit('java',cin[i],params[i][1]) for i in range(nfields))
        entries.append("new TC("+ins+", "+cout+")")
    if ret=='tree':
        cmp="if(!eqInt(serTree(got), (int[])c.want)){"
    elif ret=='listnode':
        cmp="if(!eqInt(serList(got), (int[])c.want)){"
    elif ret=='list':
        cmp="if(!eqInt(got, (int[])c.want)){"
    else:
        cmp="if(!got.equals(c.want)){"
    harness=("    public static void main(String[] args) {\n        class TC { "+("; ".join("Object in%d; "%i for i in range(nfields)))+"Object want; TC("+",".join("Object i%d"%i for i in range(nfields))+", Object w){ "+"; ".join("in%d=i%d"%(i,i) for i in range(nfields))+"; want=w; } }\n        TC[] cases={ "+", ".join(entries)+" };\n        boolean ok=true;\n        for(TC c: cases){ "+rt+" got="+fname+"("+", ".join("(("+pt[i]+")c.in%d)"%i for i in range(nfields))+"); "+cmp+" ok=false; System.out.println(\"FAIL \"+c.in0); } }\n        if(!ok) throw new RuntimeException(\"FAILED\");\n        System.out.println(\"PASS\");\n    }")
    return hdr+"class "+cls+" {\n"+("\n".join(helpers)+"\n")+("    static "+rt+" "+fname+"("+", ".join(pt[i]+" "+params[i][0] for i in range(nfields))+") {\n"+body+"\n    }\n")+harness+"\n}\n"

def ts_file(params,ret,fname,body,mode,cases_in,cases_out,ut,ul):
    hdr=""
    helpers=[]
    if ret=='list' or any(t=='list' for _,t in params):
        helpers.append("function eqInt(a:number[],b:number[]):boolean{ if(a.length!=b.length) return false; for(let i=0;i<a.length;i++) if(a[i]!=b[i]) return false; return true; }")
    if ut:
        helpers.append("""class TreeNode { val:number; left:TreeNode|null; right:TreeNode|null; constructor(v:number){this.val=v;this.left=null;this.right=null;} }
function buildTree(s:string):TreeNode|null{ if(!s) return null; const p=s.split(','); if(p[0]=='null') return null; const root=new TreeNode(+p[0]); const q:TreeNode[]=[root]; let i=1; while(i<p.length){ const cur=q.shift()!; if(p[i]!='null'){ cur.left=new TreeNode(+p[i]); q.push(cur.left);} i++; if(i<p.length && p[i]!='null'){ cur.right=new TreeNode(+p[i]); q.push(cur.right);} i++; } return root; }
function serTree(n:TreeNode|null):number[]{ const out:number[]=[]; if(!n) return out; const q:any[]=[n]; while(q.length){ const x=q.shift(); if(x==null){ out.push(-1); continue;} out.push(x.val); q.push(x.left); q.push(x.right);} while(out.length && out[out.length-1]==-1) out.pop(); return out; }""")
    if ul:
        helpers.append("""class ListNode { val:number; next:ListNode|null; constructor(v:number){this.val=v;this.next=null;} }
function buildList(s:string):ListNode|null{ const p=s.split(','); const head=new ListNode(+p[0]); let cur=head; for(let i=1;i<p.length;i++){ cur.next=new ListNode(+p[i]); cur=cur.next;} return head; }
function serList(n:ListNode|null):number[]{ const out:number[]=[]; while(n){ out.push(n.val); n=n.next;} return out; }""")
    if 'sortedArr' in body or 'Math.' in body: pass
    if 'contains(' in body:
        helpers.append("function contains(a:number[],v:number):boolean{ return a.indexOf(v)>=0; }")
    # function
    pt=[('TreeNode|null' if t=='tree' else ('ListNode|null' if t=='listnode' else ('number[]' if t=='list' else ('string' if t=='str' else 'number')))) for _,t in params]
    rt=('number[]' if ret in ('list','tree','listnode') else ('string' if ret=='str' else ('number' if ret in ('int','num') else ('boolean' if ret=='bool' else 'any'))))
    nfields=len(params)
    entries=[]
    for cin,cout in zip(cases_in,cases_out):
        ins=", ".join(lit('ts',cin[i],params[i][1]) for i in range(nfields))
        entries.append("        { in: ["+ins+"], want: "+cout+" },")
    if ret in ('tree','listnode'):
        cmp="if(!eqInt(ser"+( "Tree" if ret=='tree' else "List")+"(got as any), c.want)){"
    elif ret=='list':
        cmp="if(!eqInt(got, c.want)){"
    else:
        cmp="if(got !== c.want){"
    call=", ".join("c.in["+str(i)+"]" for i in range(nfields))
    harness=("export function demo():void{\n"+("\n".join(helpers)+"\n")+("    function "+fname+"("+", ".join(params[i][0]+":"+pt[i] for i in range(nfields))+"):"+rt+"{\n"+body+"\n    }\n")+
        "    const cases=[ "+("\n".join(entries))+" ];\n    let fail=false;\n    for(const c of cases){ const got="+fname+"("+call+"); "+cmp+" fail=true; console.log('FAIL',c.in,c.want,got); } }\n    if(fail) throw new Error('FAILED');\n    console.log('PASS');\n}\ndemo();")
    return hdr+harness

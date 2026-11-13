-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/105893757
-- 栈排序分析 — Lua 版（方案3）
local function stack_sort(input) -- local function stack_sort(input)
	local st = {} -- 把 {} 写入 local st
	for _, v in ipairs(input) do
		st[#st + 1] = v
	end -- 遍历取 值
	local out = {} -- 把 {} 写入 local out
	while #st > 0 do
		out[#out + 1] = table.remove(st)
	end -- 把 table 弹出 st) 终点 写入 while #st > 0 do out[#out + 1]
	return out -- 返回 out
end -- 终点
assert(table.concat(stack_sort({ 3, 1, 5, 2, 4 }), ",") == "4,2,5,1,3") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS

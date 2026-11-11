-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130726302
-- LeetCode 150. 逆波兰表达式求值 — Lua 版（方案1）
local function eval_rpn(tokens) -- local function eval_rpn(tokens)
	local st = {} -- 把 {} 写入 local st
	for _, t in ipairs(tokens) do -- 遍历取 另一字符串
		if t == "+" then -- 若 另一字符串 等于 「 加 」 then
			local b = table.remove(st)
			local a = table.remove(st) -- 把 table 弹出 st); local 数组 赋值为 table 弹出 st) 写入 local b
			st[#st + 1] = a + b -- 把 数组 加 b 写入 st[#st + 1]
		elseif t == "-" then -- 把 赋值为 「 减 」 then 写入 elseif t
			local b = table.remove(st)
			local a = table.remove(st) -- 把 table 弹出 st); local 数组 赋值为 table 弹出 st) 写入 local b
			st[#st + 1] = a - b -- 把 数组 减 b 写入 st[#st + 1]
		elseif t == "*" then -- 把 赋值为 「 乘 」 then 写入 elseif t
			local b = table.remove(st)
			local a = table.remove(st) -- 把 table 弹出 st); local 数组 赋值为 table 弹出 st) 写入 local b
			st[#st + 1] = a * b -- 把 数组 乘 b 写入 st[#st + 1]
		elseif t == "/" then -- 把 赋值为 「 除以 」 then 写入 elseif t
			local b = table.remove(st)
			local a = table.remove(st) -- 把 table 弹出 st); local 数组 赋值为 table 弹出 st) 写入 local b
			st[#st + 1] = math.floor(a / b + 0.5) * ((a * b < 0) and -1 or 1) * -1 -- 截断除法
			-- 简化：C 风格截断
			local q = a / b -- 把 数组 除以 b 写入 local q
			st[#st] = (q >= 0) and math.floor(q) or math.ceil(q) -- 把 (节点 不低于 0) and math.floor(节点) or math.ceil(节点) 写入 st[#st]
		else -- 否则
			st[#st + 1] = tonumber(t) -- 把 tonumber(另一字符串) 写入 st[#st + 1]
		end -- 终点
	end -- 终点
	return st[1] -- 返回 st[1]
end -- 终点
assert(eval_rpn({ "2", "1", "+", "3", "*" }) == 9) -- 断言校验
assert(eval_rpn({ "4", "13", "5", "/", "+" }) == 6) -- 断言校验
assert(eval_rpn({ "10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+" }) == 22) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS

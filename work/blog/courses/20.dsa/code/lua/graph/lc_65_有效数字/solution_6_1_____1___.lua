-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133920771
-- LeetCode 65. 有效数字 — Lua 版

-- 方案6（确定有限状态自动机 DFA，其余字符 lowercase）
local function is_number(s) -- local function is_number(字符串)
	local t = s:match("^%s*(.-)%s*$") -- 等价于 TS 的 trim()
	local graph = { -- 把 { 写入 local graph
		[0] = { blank = 0, sign = 1, ["."] = 2, digit = 6 },
		[1] = { digit = 6, ["."] = 2 },
		[2] = { digit = 3 },
		[3] = { digit = 3, e = 4 },
		[4] = { digit = 5, sign = 7 },
		[5] = { digit = 5 },
		[6] = { digit = 6, ["."] = 3, e = 4 },
		[7] = { digit = 5 },
	}
	local state = 0 -- 把 0 写入 local state
	for i = 1, #t do -- 把 1, #另一字符串 do 写入 for i
		local ch = t:sub(i, i) -- 把 另一字符串:sub(下标 i, 下标 i) 写入 local ch
		local c -- local 字符
		if ch:match("%d") then -- 若 字符:match(「 对…取模 d」) then
			c = "digit" -- 把 「digit」 存入 字符
		elseif ch == " " then -- 把 赋值为 「 」 then 写入 elseif ch
			c = "blank" -- 把 「blank」 存入 字符
		elseif ch == "+" or ch == "-" then -- 把 赋值为 「 加 」 or 字符 等于 「 加 」 then 写入 elseif ch
			c = "sign" -- 把 「sign」 存入 字符
		else -- 否则
			c = ch:lower() -- 把 字符:lower() 存入 字符
		end -- 终点
		local row = graph[state] -- 把 graph[state] 写入 local row
		if row[c] == nil then
			return false
		end -- 若 row[字符] 等于 nil then return false 终点
		state = row[c] -- 把 row[字符] 存入 state
	end -- 终点
	return state == 3 or state == 5 or state == 6 -- 返回 state 等于 3 or state 等于 5 or state 等于 6
end -- 终点

assert(is_number("0") == true, "isNumber('0') should be true") -- 断言校验
assert(is_number("abc") == false, "isNumber('abc') should be false") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS

-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133598918
-- LeetCode 2. 两数相加 — Lua 版（方案1）
local function add_two_numbers(a, b) -- local function add_two_numbers(数组, b)
	local i, j, carry = 1, 1, 0 -- 把 1, 1, 0 写入 local i, j, carry
	local out = {} -- 把 {} 写入 local out
	while i <= #a or j <= #b or carry > 0 do -- 把 #数组 or 下标 j 不超过 #b or carry 超过 0 do 写入 while i <
		local total = carry -- 把 carry 写入 local total
		if i <= #a then
			total = total + a[i]
			i = i + 1
		end
		if j <= #b then
			total = total + b[j]
			j = j + 1
		end -- 若 下标 j 不超过 #b then 总和 赋值为 总和 加 b[下标 j]; 下标 j 赋值为 下标 j 加 1 终点
		out[#out + 1] = total % 10 -- 把 总和 对…取模 10 写入 out[#out + 1]
		carry = math.floor(total / 10) -- 把 math.floor(总和 除以 10) 存入 carry
	end -- 终点
	if #out == 0 then
		out[1] = 0
	end -- 若 #out 等于 0 then out[1] 赋值为 0 终点
	return out -- 返回 out
end -- 终点
assert(table.concat(add_two_numbers({ 2, 4, 3 }, { 5, 6, 4 }), ",") == "7,0,8") -- 打印输出
assert(table.concat(add_two_numbers({ 0 }, { 0 }), ",") == "0") -- 打印输出
assert(table.concat(add_two_numbers({ 9, 9, 9, 9, 9, 9, 9 }, { 9, 9, 9, 9 }), ",") == "8,9,9,9,0,0,0,1") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS

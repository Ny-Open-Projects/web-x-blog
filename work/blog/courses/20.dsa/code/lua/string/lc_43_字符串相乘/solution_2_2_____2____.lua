-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130701795
-- LeetCode 43. 字符串相乘 — Lua 版（方案2）
local function multiply(num1, num2) -- local function multiply(num1, num2)
	if num1 == "0" or num2 == "0" then
		return "0"
	end -- 若 num1 等于 「0」 or num2 等于 「0」 then return 「0」 终点
	local m, n = #num1, #num2 -- 把 #num1, #num2 写入 local m, n
	local result = {} -- 把 {} 写入 local result
	for i = 1, m + n do
		result[i] = 0
	end -- 让 下标 i 从 1 走到 映射表（Lua 1 基）
	for i = m, 1, -1 do -- 把 映射表, 1, 减 1 do 写入 for i
		for j = n, 1, -1 do -- 把 元素个数, 1, 减 1 do 写入 for j
			local mul = (num1:byte(i) - 48) * (num2:byte(j) - 48)
			local p1, p2 = i + j - 1, i + j -- 把 下标 i 加 下标 j 减 1, 下标 i 加 下标 j 写入 local p1, p2
			local total = mul + result[p2] -- 把 mul 加 结果[p2] 写入 local total
			result[p2] = total % 10 -- 把 总和 对…取模 10 写入 result[p2]
			result[p1] = result[p1] + math.floor(total / 10) -- 把 结果[p1] 加 math.floor(总和 除以 10) 写入 result[p1]
		end -- 终点
	end -- 终点
	local out = {} -- 把 {} 写入 local out
	local started = false -- 把 false 写入 local started
	for _, d in ipairs(result) do -- 遍历取 d
		if d ~= 0 or started then -- 若 d ~ 赋值为 0 or started then
			out[#out + 1] = tostring(d) -- 把 tostring(d) 写入 out[#out + 1]
			started = true -- 把 true 存入 started
		end -- 终点
	end -- 终点
	if #out == 0 then
		return "0"
	end -- 若 #out 等于 0 then return 「0」 终点
	return table.concat(out) -- 返回 table.concat(out)
end -- 终点
assert(multiply("2", "3") == "6") -- 断言校验
assert(multiply("123", "456") == "56088") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS

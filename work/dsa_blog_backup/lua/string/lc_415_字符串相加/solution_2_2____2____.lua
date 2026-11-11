-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130736023
-- LeetCode 415. 字符串相加 — Lua 版（方案2）
local function add_strings(num1, num2) -- local function add_strings(num1, num2)
	local i, j = #num1, #num2 -- 把 #num1, #num2 写入 local i, j
	local carry = 0 -- 把 0 写入 local carry
	local out = {} -- 把 {} 写入 local out
	while i >= 1 or j >= 1 or carry > 0 do -- 把 1 or 下标 j 不低于 1 or carry 超过 0 do 写入 while i >
		local total = carry -- 把 carry 写入 local total
		if i >= 1 then
			total = total + (num1:byte(i) - 48)
			i = i - 1
		end
		if j >= 1 then
			total = total + (num2:byte(j) - 48)
			j = j - 1
		end
		out[#out + 1] = tostring(total % 10) -- 把 tostring(总和 对…取模 10) 写入 out[#out + 1]
		carry = math.floor(total / 10) -- 把 math.floor(总和 除以 10) 存入 carry
	end -- 终点
	if #out == 0 then
		return "0"
	end -- 若 #out 等于 0 then return 「0」 终点
	return table.concat(out):reverse() -- 返回 table.concat(out):reverse()
end -- 终点
assert(add_strings("11", "123") == "134") -- 断言校验
assert(add_strings("456", "77") == "533") -- 断言校验
assert(add_strings("0", "0") == "0") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS

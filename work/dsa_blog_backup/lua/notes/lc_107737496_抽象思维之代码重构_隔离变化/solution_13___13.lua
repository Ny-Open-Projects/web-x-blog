-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
-- LeetCode 107737496. 代码重构_隔离变化 — Lua 版（方案13：微型正则匹配 match/matchhere/matchstar）
local function matchstar(c, re, text) -- local function matchstar(字符, re, text)
	local i = 0 -- 把 0 写入 local i
	while true do -- while true do
		if matchhere(re, text:sub(i + 1)) then
			return true
		end -- 若 matchhere(re, text:sub(下标 i 加 1)) then return true 终点
		if i >= #text then
			break
		end -- 若 下标 i 不低于 #text then break 终点
		if text:sub(i + 1, i + 1) ~= c and c ~= "." then
			break
		end
		i = i + 1 -- 把 下标 i 加 1 存入 下标 i
	end -- 终点
	return false -- 返回 false
end -- 终点

function matchhere(re, text) -- function matchhere(re, text)
	if re == "" then
		return true
	end -- 若 re 等于 「」 then return true 终点
	if #re >= 2 and re:sub(2, 2) == "*" then -- 若 #re 不低于 2 and re:sub(2, 2) 等于 「 乘 」 then
		return matchstar(re:sub(1, 1), re:sub(3), text) -- 返回 matchstar(re:sub(1, 1), re:sub(3), text)
	end -- 终点
	if re:sub(1, 1) == "$" and #re == 1 then
		return text == ""
	end
	if #text > 0 and (re:sub(1, 1) == "." or re:sub(1, 1) == text:sub(1, 1)) then
		return matchhere(re:sub(2), text:sub(2)) -- 返回 matchhere(re:sub(2), text:sub(2))
	end -- 终点
	return false -- 返回 false
end -- 终点

local function match(re, text) -- local function match(re, text)
	if #re > 0 and re:sub(1, 1) == "^" then -- 若 #re 超过 0 and re:sub(1, 1) 等于 「 按位异或 」 then
		return matchhere(re:sub(2), text) -- 返回 matchhere(re:sub(2), text)
	end -- 终点
	local i = 0 -- 把 0 写入 local i
	while true do -- while true do
		if matchhere(re, text:sub(i + 1)) then
			return true
		end -- 若 matchhere(re, text:sub(下标 i 加 1)) then return true 终点
		if i >= #text then
			break
		end -- 若 下标 i 不低于 #text then break 终点
		i = i + 1 -- 把 下标 i 加 1 存入 下标 i
	end -- 终点
	return false -- 返回 false
end -- 终点

assert(match("abc", "xxabcxx") == true, "m1") -- 断言校验
assert(match("a.c", "axc") == true, "m2") -- 断言校验
assert(match("a*", "aaaa") == true, "m3") -- 断言校验
assert(match("^a", "ba") == false, "m4") -- 断言校验
assert(match("c$", "abc") == true, "m5") -- 断言校验
assert(match("a.*c", "aXYZc") == true, "m6") -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS

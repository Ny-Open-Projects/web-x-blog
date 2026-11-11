-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133759617
-- LeetCode 20. 有效的括号 — Lua 版（方案11）
local function is_valid(s) -- local function is_valid(字符串)
	local stack = {} -- 把 {} 写入 local stack
	local pairs = { [")"] = "(", ["]"] = "[", ["}"] = "{" }
	for i = 1, #s do -- 把 1, #字符串 do 写入 for i
		local ch = s:sub(i, i) -- 把 字符串:sub(下标 i, 下标 i) 写入 local ch
		if pairs[ch] then -- 若 pairs[字符] then
			local top = #stack > 0 and table.remove(stack) or "#" -- 把 #栈 超过 0 and table 弹出 栈) or 「#」 写入 local top
			if top ~= pairs[ch] then
				return false
			end -- 若 top ~ 赋值为 pairs[字符] then return false 终点
		else -- 否则
			stack[#stack + 1] = ch -- 把 字符 写入 stack[#stack + 1]
		end -- 终点
	end -- 终点
	return #stack == 0 -- 返回 #栈 等于 0
end -- 终点
local tests = { "(", "()", "()[]{}", "(]", "([)]", "abc" } -- 把 {「(」, 「(」, 「(」, 「(」, 「(」, 「(」} 写入 local tests
local want = { false, true, true, false, false, false } -- 把 {false, true, true, false, false, false} 写入 local want
for i, t in ipairs(tests) do -- 遍历取 另一字符串
	assert(is_valid(t) == want[i], "case " .. i) -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS

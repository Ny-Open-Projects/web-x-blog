-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134255301
-- LeetCode 380. O(1)时间插入删除和获取随机元素 — Lua 版（方案1）
local RandomizedSet = {} -- 把 {} 写入 local RandomizedSet
RandomizedSet.__index = RandomizedSet -- 把 RandomizedSet 写入 RandomizedSet.__index
function RandomizedSet.new()
	return setmetatable({ vals = {}, pos = {} }, RandomizedSet)
end
function RandomizedSet:insert(val) -- function RandomizedSet:insert(值)
	if self.pos[val] then
		return false
	end -- 若 self.pos[值] then return false 终点
	self.pos[val] = #self.vals + 1 -- 把 #self.vals 加 1 写入 self.pos[val]
	self.vals[#self.vals + 1] = val -- 把 值 写入 self.vals[#self.vals + 1]
	return true -- 返回 true
end -- 终点
function RandomizedSet:remove(val) -- function RandomizedSet:remove(值)
	local idx = self.pos[val] -- 把 self.pos[值] 写入 local idx
	if not idx then
		return false
	end -- 若 not idx then return false 终点
	local last = self.vals[#self.vals] -- 把 self.vals[#self.vals] 写入 local last
	self.vals[idx] = last -- 把 last 写入 self.vals[idx]
	self.pos[last] = idx -- 把 idx 写入 self.pos[last]
	self.vals[#self.vals] = nil -- 把 nil 写入 self.vals[#self.vals]
	self.pos[val] = nil -- 把 nil 写入 self.pos[val]
	return true -- 返回 true
end -- 终点
function RandomizedSet:get_random() -- function RandomizedSet:get_random()
	return self.vals[math.random(#self.vals)] -- 返回 self.vals[math.random(#self.vals)]
end -- 终点
math.randomseed(42) -- math.randomseed(42)
local s = RandomizedSet.new() -- 把 RandomizedSet.new() 写入 local s
assert(s:insert(1) == true) -- 断言校验
assert(s:remove(2) == false) -- 断言校验
assert(s:insert(2) == true) -- 断言校验
local r = s:get_random() -- 把 字符串:get_random() 写入 local r
assert(r == 1 or r == 2) -- 断言校验
assert(s:remove(1) == true) -- 断言校验
assert(s:insert(2) == false) -- 断言校验
assert(s:get_random() == 2) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS

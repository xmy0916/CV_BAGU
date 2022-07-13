⚠️注意：本README用于迅速回忆hot100的解法，可以理解为背答案，答案写的是我自己的口语理解不一定适合他人理解。

> 1、两数之和
<details>
  <summary><a href="./code/1.py">答案</a></summary>
  set一下数组得到存在的值，遍历找target-now是否在set中。O(n)
</details>

> 2、两数相加
<details>
  <summary><a href="./code/2.py">答案</a></summary>
  用一个进位标志记录是否进位，然后就两个指针指向两个加数的链表相加就好了。<br>
  ⚠️注意，遍历完两个加数的链表其中之一可能非空，另外遍历完进位为1的话还得增加一个最高位1 O(m+n)
</details>

> 3、无重复最长子串
<details>
  <summary><a href="./code/3.py">答案</a></summary>
  字典记录字符的位置，key是字符，value是index<br>
  如果新遍历的字符不在字典，字典更新并更新最大长度<br>
  如果在字典，⚠️注意：更新窗口start的位置，为max(start, 字典中当前字符的位置+1)，就是start不可后退！O(n)
</details>

> 4、两个正序数组的中位数⚠️
<details>
  <summary><a href="./code/4.py">答案</a></summary>
  暴力：归并排序合并两个数组，然后返回mid即可。面试写不来最优解，可以用此解法。 O(m+n)
  待更新最优解
</details>

> 5、最长回文子串️
<details>
  <summary><a href="./code/5.py">答案</a></summary>
  中心扩展法，遍历字符串，分别考虑以单个字符为中心时候和以N个一样的字符为中心的情况。向左右扩展更新答案。
</details>

> 10、正则表达式匹配️
<details>
  <summary><a href="./code/10.py">答案</a></summary>
  动态规划，dp[i][j]表示前j个P是否可以匹配前i个S。<br>
  <li>1、当前p是'.'，直接取dp[i-1][j-1]</li>
  <li>2、当前p是字符，如果p[j-1]==s[i-1]，也是直接取dp[i-1][j-1]</li>
  <li>3、当前p是'*'，第一种可以不要p的前一个字符，就取case1 = dp[i][j-2]，第二种前一个字符必须要就取dp[i-1][j] if s[i-1] == p[j-2] or p[j-2] == '.' else False， 两种情况或一下即可</li>
</details>

> 11、盛最多水的容器
<details>
  <summary><a href="./code/11.py">答案</a></summary>
  左右两头的双指针，短板移动即可。
</details>

> 15、三数之和
<details>
  <summary><a href="./code/15.py">答案</a></summary>
  sort完，双指针，注意去重。
</details>

> 17、电话号码组合
<details>
  <summary><a href="./code/17.py">答案</a></summary>
  dfs
</details>

> 19、删除链表的倒数第 N 个结点
<details>
  <summary><a href="./code/19.py">答案</a></summary>
  快慢指针
</details>

> 20、有效的括号
<details>
  <summary><a href="./code/20.py">答案</a></summary>
  括号问题，一般考虑栈来解，栈不行考虑可否dp，这个直接判断是右括号时栈顶和当前即可，左括号压栈。最后要栈空
</details>

> 21、合并两个有序链表
<details>
  <summary><a href="./code/21.py">答案</a></summary>
  双指针即可，注意两个链表可能不等长，如果两个指针一个为空另一个不空得接着插入。
</details>

> 22、括号生成
<details>
  <summary><a href="./code/22.py">答案</a></summary>
  dp的思想，计算i组括号时的括号组合时，开始遍历 p q ，其中p+q=i-1，那么dp[i] +=  "(" + p的每一个情况 + ")" + q的每一个情况
</details>

> 23、合并K个升序链表
<details>
  <summary><a href="./code/23.py">答案</a></summary>
  K指针比较好写，等价合并两个有序链表。
</details>

> 31、下一个排列⚠️
<details>
  <summary><a href="./code/31.py">答案</a></summary>
  <li>1、从后向前查找第一个相邻升序的元素对 (i,j)，满足 A[i] < A[j]。此时 [j,end) 必然是降序
  <li>2、在 [j,end) 从后向前查找第一个满足 A[i] < A[k] 的 k。A[i]、A[k] 分别就是上文所说的「小数」、「大数」
  <li>3、将 A[i] 与 A[k] 交换
  <li>4、可以断定这时 [j,end) 必然是降序，逆置 [j,end)，使其升序
  <li>5、如果在步骤 1 找不到符合的相邻元素对，说明当前 [begin,end) 为一个降序顺序，则直接跳到步骤 4
  <li>⚠️感觉这题很难啊，要是考上一个排列还是不会做...
</details>

> 32、最长有效括号
<details>
  <summary><a href="./code/32.py">答案</a></summary>
  动态规划，i-dp[i-1]-1是与当前)对称的位置<br>
  if s[i]==')' and i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=='(':<br>
    dp[i]=dp[i-1]+dp[i-dp[i-1]-2]+2
</details>

> 33、搜索旋转排序数组⚠️
<details>
  <summary><a href="./code/33.py">答案</a></summary>
  二分，判断目标在有序侧还是无序侧，有序无序侧判断可以直接根据头尾的大小关系分析。
</details>

> 34、在排序数组中查找元素的第一个和最后一个位置
<details>
  <summary><a href="./code/34.py">答案</a></summary>
  第一次二分找左，第二次二分找右
</details>

> 39、组合总和
<details>
  <summary><a href="./code/39.py">答案</a></summary>
  要注意某个数可以多次利用，所以dfs给下一层的剩余候选要保留这一次用的那个值。可以提前sort剪枝。
</details>

> 42、接雨水
<details>
  <summary><a href="./code/42.py">答案</a></summary>
  从左往右遍历找到比当前index的高度最远的index， 从右往左遍历找到比当前index的高度最远的index， 然后再遍历一遍height即可，可以直接拿到左右最远的高的最小的那个就可以算出当前柱子能存多少水。
</details>

> 46、全排列
<details>
  <summary><a href="./code/46.py">答案</a></summary>
  dfs即可。
</details>

> 48、旋转图像
<details>
  <summary><a href="./code/48.py">答案</a></summary>
  先上下翻转，然后左右翻转即可。
</details>

> 49、字母异位词分组
<details>
  <summary><a href="./code/49.py">答案</a></summary>
  可以用桶排序的思想，统计下出现的所有字符假设n个，构建一个长度为n的数组，某个字符出现了就对应位置+1，然后字典的键是这个数组，值是所有的结果，最后返回values即可
</details>

> 53、最大子数组和
<details>
  <summary><a href="./code/53.py">答案</a></summary>
  动态规划，dp[i] = max(dp[i-1]+arr[i], arr[i])
</details>

> 55、跳跃游戏
<details>
  <summary><a href="./code/55.py">答案</a></summary>
  从左到右遍历，维护一个可以跳到最远的遍历，如果当前遍历的索引大于可跳到最远就直接退出了，否则就看看是否需要更新跳到最远。
</details>

> 56、合并区间
<details>
  <summary><a href="./code/56.py">答案</a></summary>
  先按区间左边从小到大排序，然后遍历一遍分相交、不相交、覆盖三种情况讨论就好了。
</details>

> 62、不同路径
<details>
  <summary><a href="./code/62.py">答案</a></summary>
  二维动态规划
</details>

> 64、最小路径和
<details>
  <summary><a href="./code/64.py">答案</a></summary>
  二维动态规划
</details>

> 70、爬楼梯
<details>
  <summary><a href="./code/70.py">答案</a></summary>
  动态规划，或者递归，还有通解O(1)(字节面试问到了，可以搜斐波那契数列通解)
</details>

> 72、编辑距离
<details>
  <summary><a href="./code/72.py">答案</a></summary>
  动态规划
</details>

> 75、 颜色分类
<details>
  <summary><a href="./code/75.py">答案</a></summary>
  第一遍把0弄到前面，记录最后一个0的位置，第二遍把所有的1弄到最后一个0的后面即可。
</details>

> 76、最小覆盖子串⚠️
<details>
  <summary><a href="./code/76.py">答案</a></summary>
  
</details>

> 78、子集
<details>
  <summary><a href="./code/78.py">答案</a></summary>
  dfs即可
</details>

> 79、单词搜索
<details>
  <summary><a href="./code/79.py">答案</a></summary>
  遍历一二维字符，从遍历位置开始dfs，在dfs的时候需要把当前位置用已使用的符号取代比如'-'，在回溯的时候需要还原。
</details>

> 84、柱状图中最大的矩形
<details>
  <summary><a href="./code/84.py">答案</a></summary>
  单调队列
</details>

> 85、最大矩形
<details>
  <summary><a href="./code/85.py">答案</a></summary>
  在纵轴上把1相加就可以把二维降为一维，然后用上一题的单调队列即可。
</details>

> 94、二叉树的中序遍历
<details>
  <summary><a href="./code/94.py">答案</a></summary>
  非递归：root不空的话，root压栈，遍历left（root=root.left），空的话弹栈给root，记录root的值，遍历right(root=root.right)
</details>

> 96、不同的二叉搜索树
<details>
  <summary><a href="./code/.py">答案</a></summary>
  就是n个节点假设左子树由i个节点右子树就有n-1-i个节点，此时不同的二叉树就是dp[i]*dp[n-1-i]了，然后把i从0到n-1的所有结果加起来即可。
</details>

> 98、验证二叉搜索树
<details>
  <summary><a href="./code/.py">答案</a></summary>
  中序遍历的结果是递增的，用非递归的方法遍历二叉树，然后在记录节点的时候和之前的一个结果比较大小即可。
</details>

> 101、对称二叉树
<details>
  <summary><a href="./code/.py">答案</a></summary>
  同时递归左右即可
</details>

> 102、二叉树的层序遍历
<details>
  <summary><a href="./code/.py">答案</a></summary>
  一个队列即可，初始化队的长度1，左子树先入队然后右子树入队，算下队的长度开始下一层
</details>

> 104、 二叉树的最大深度
<details>
  <summary><a href="./code/.py">答案</a></summary>
  递归
</details>

> 105、从前序与中序遍历序列构造二叉树
<details>
  <summary><a href="./code/.py">答案</a></summary>
  前序的第一个是根节点，去中序找根的index，index的左边就是左子树的中序遍历，右边是右子树的中序遍历，递归即可
</details>

> 114、二叉树展开为链表
<details>
  <summary><a href="./code/.py">答案</a></summary>
  非递归前序遍历即可
</details>

> 121、买卖股票的最佳时机
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 124、二叉树中的最大路径和
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 128、最长连续序列
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 136、只出现一次的数字
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 139、单词拆分
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 141、环形链表
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>

> 
<details>
  <summary><a href="./code/.py">答案</a></summary>
  
</details>



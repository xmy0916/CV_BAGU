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



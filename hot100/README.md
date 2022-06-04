⚠️注意：本README用于迅速回忆hot100的解法，可以理解为背答案，答案写的是我自己的口语理解不一定适合他人理解。

> 1、两数之和
<details>
  <summary><a href="./code/1.py">答案</a></summary>
  set一下数组得到存在的值，遍历找target-now是否在set中。O(n)
</details>

> 2、两数相加
<details>
  <summary>答案</summary>
  用一个进位标志记录是否进位，然后就两个指针指向两个加数的链表相加就好了。<br>
  ⚠️注意，遍历完两个加数的链表其中之一可能非空，另外遍历完进位为1的话还得增加一个最高位1 O(m+n)
</details>

> 3、无重复最长子串
<details>
  <summary>答案</summary>
  字典记录字符的位置，key是字符，value是index<br>
  如果新遍历的字符不在字典，字典更新并更新最大长度<br>
  如果在字典，⚠️注意：更新窗口start的位置，为max(start, 字典中当前字符的位置+1) O(n)
</details>

> 4、两个正序数组的中位数⚠️
<details>
  <summary>答案</summary>
  暴力：归并排序合并两个数组，然后返回mid即可。面试写不来最优解，可以用此解法。 O(m+n)
  待更新最优解
</details>

> 5、最长回文子串️
<details>
  <summary>答案</summary>
  中心扩展法，遍历字符串，分别考虑以单个字符为中心时候和以N个一样的字符为中心的情况。向左右扩展更新答案。
</details>
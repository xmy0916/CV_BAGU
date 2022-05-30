> 1、Transformer为什么除以根号d_k
<details>
  <summary>答案</summary>
  这个问题从attention的公式说起，softmax(q*k/(dk)^0.5)，因为外面包了层softmax，如果softmax的输入数值比较大就会出现输出的结果接近于One hot的情况，然后根据softmax的导数他是y*(1-y)，因此某个输出接近1的话他的梯度就趋于0了，因此这样会影响参数的更新。
  因此为了将softmax的输入稳定在比较小的范围，作者论文说的是首先q和k是满足均值为0方差为1的分布，因此q*k就满足均值为0方差为dk，因此除以根号dk就可以保证qk/dk^0.5的方差就为1了，然后一组数满足均值为0方差为1的时候就不可能出现特别大的值而是稳定在0附近
  计算详情参考：https://xmy0916.blog.csdn.net/article/details/123495872?spm=1001.2014.3001.5502
</details>

> 2、Transformer self attn的机制
<details>
  <summary>答案</summary>
  首先对于输入形状为（batchsize， n， dim）的序列用矩阵Wq（dim, dim）与之相乘得到Q（batchsize， n， dim），同理K,V得到Wk，Wv，然后计算Q和K的转置矩阵乘除以根号dk之后过softmax得到attn的权重加权到V上得到输出。
</details>

> 3、Transformer 为什么要映射到QKV？
<details>
  <summary>答案</summary>
  首先我们知道Q和K的转置点乘是为了得到一个attn score的矩阵拿来对V加权，K和Q用不同的矩阵得到可以理解为把QK映射到不同的特征空间，有了这种不同特征空间的投影增加了表达能力，这样计算出来的attn score的泛化能力更强，
  而如果用同样的Q和K相乘，得到的attn score矩阵是个对称矩阵相当于投影到了同一个空间，泛化能力差，这样的attn分数对V加权效果不好。
  </details>

> 4、Python 列表和元组的区别？
<details>
  <summary>答案</summary>
  列表的值可以修改，元组的值一经定义则不可修改，元组可以作为字典的健，列表不可以。
  </details>

> 5、Python空列表和空元组谁在内存占用的空间大？
<details>
  <summary>答案</summary>
  列表大，首先元组的内容不可修改，列表的内容可以修改，因此可以猜到列表的底层设计肯定比元组复杂，占用空间大情理之中。
  具体的，列表的大小是可变的，元组是固定大小的，因此列表底层需要一个间接层（指向存储元素的指针），此外在列表执行append的时候还需要一个指针来跟踪需要分配空间的大小。因此列表占用的内存大于元组。
  </details>

> 6、Python迭代器的定义？
<details>
  <summary>答案</summary>
  1、迭代器从第一个元素访问，直到所有元素访问完结束
  2、迭代器只能前进不能后退
  3、iter可以得到一个可以迭代对象的迭代器，next可以取得下一个元素
  </details>

> 7、Python迭代器和生成器的区别？
<details>
  <summary>答案</summary>
  相同：
  1、生成器是一种特殊的迭代器
  不同：
　1、迭代器可以通过 iter（） 内置函数创建
　2、生成器是通过函数的形式中调用 yield 或（）的形式创建的
　3、迭代器在调用next（）函数或for循环中，所有值被返回，没有其他过程或说动作
　4、生成器在调用next（）函数或for循环中，所有过程被执行，且返回值
  </details>

> 8、Python迭代器实现的方法？
<details>
  <summary>答案</summary>
  相同：
  1、用iter()函数得到迭代器对象
  2、用yiled函数得到生成器，也是中特殊的迭代器
  3、自己定义iter的对象，实现__iter__和__next__函数
  </details>

> 9、Python垃圾回收机制？
<details>
  <summary>答案</summary>
  python里每一个东西都是对象，它们的核心就是一个结构体：PyObject
  PyObject是每个对象必有的内容，其中ob_refcnt就是做为引用计数。当一个对象有新的引用时，它的ob_refcnt就会增加，当引用它的对象被删除，它的ob_refcnt就会减少
  当引用计数为0时，该对象生命就结束了。
  引用计数机制的优点：
    1、简单
    2、实时性：一旦没有引用，内存就直接释放了。不用像其他机制等到特定时机。实时性还带来一个好处：处理回收内存的时间分摊到了平时。
  引用计数机制的缺点：
    3、维护引用计数消耗资源
    4、循环引用
  </details>

> 10、什么是线性回归？
<details>
  <summary>答案</summary>
  线性回归就是要找一条直线，并且让这条直线尽可能地拟合图中的数据点。
  </details>

> 11、逻辑回归是线性的吗？
<details>
  <summary>答案</summary>
  逻辑回归的模型引入了sigmoid函数映射，是非线性模型，但本质上又是一个线性回归模型，因为除去sigmoid映射函数关系，其他的步骤，算法都是线性回归的。可以说，逻辑回归，都是以线性回归为理论支持的。
  </details>

> 12、dropout的原理？
<details>
  <summary>答案</summary>
  某个神经元以p的概率保留，1-p的概率输出0
  </details>

> 13、dropout训练和测试的差别？
<details>
  <summary>答案</summary>
  在Alexnet中实现的dropout，训练阶段以p保留，1-p输出0，测试阶段为了满足均值一致，会把测试的输出乘p
  现在，为了节约测试的计算资源，训练阶段仍然以p保留，1-p输出0，但是训练阶输出的值除以p，这样就保证测试阶段的均值和训阶段一致，且测试阶段不用任何操作。
  </details>

> 14、神经网络为什么要激活函数？
<details>
  <summary>答案</summary>
  引入激活函数是为了增加神经网络模型的非线性。没有激活函数的每层都相当于矩阵相乘。就算你叠加了若干层之后，无非还是个矩阵相乘罢了
  </details>

> 15、分类任务最后一层的softmax的作用是什么？
<details>
  <summary>答案</summary>
  它将多个神经元的输出，映射到（0,1）区间内，可以看成概率来理解，从而来进行多分类。
  </details>

> 16、SGD，ADAM相关问题
<details>
  <summary>答案</summary>
  首先明确一点，所有基于SGD的优化方法就是基于不同学习率变化策略的优化方法罢了。
  朴素的SGD算法存在着一直左右震荡的情况，大大减慢了我们网络的收敛速度。现在使用的基本是基于momentum的SGD算法，他的优化在于结合了历史梯度的信息，通过矢量加和约掉震荡方向上的梯度分量和而加速模型的收敛。
  ADAM算法结合了SGD+momentum的思想，以及RMSProp的思想（RMSProp通过动态地调整学习率来避免震荡）
  </details>
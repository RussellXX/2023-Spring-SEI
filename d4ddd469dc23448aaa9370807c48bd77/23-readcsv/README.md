### Python: CSV

本次作业，我们基于CSV实现一个简(jian)易(lou)的数据库。

CSV文件即逗号分隔值文件，示例：
```
    SiyuanCen,ceo,85900
    JingLan,staff,51500
    JinboHu,manager,66500
```
三列的属性分别为Name,Title,Salary. 约定本题中所有的csv文件都由这三列构成。

您需实现以下操作：
- `INSERT Name,Title,Salary`:向csv文件末尾追加写入一行 Name,Title,Salary.
- `SHOWALL`:读取内容后，您需按Salary升序排序，并计算Salary的平均值AVG。输出格式为表格形式，各列左对齐，两列间隔一个空格（以列中最长字符串为基准）。最后需打印Salary平均值。示例：
    ```
        Name      Title   Salary
        JingLan   staff   51500.00
        JinboHu   manager 66500.00
        SiyuanCen ceo     85900.00
        AVG:67966.66
    ```

输入：
```
第一行输入一个整数n，为需执行的指令的行数

接下来n行，为指令
```
注意：

1. 要读取的**文件名**将以参数的形式传递到待编写的函数中

2. Salary和平均值输出到**小数点后两位**

3. rawdata开头的文件**请勿修改**，它们保证在测试结束后将resource-x.csv文件恢复原状。自我测试的过程中请留意resource-x.csv的变化。

4. 本地使用Pycharm测试时，若发生找不到文件的错误，请修改test_read_csv.py:

   ```pyt
   resource1 = 'test/resource-1.csv'
   resource2 = 'test/resource-2.csv'
   raw1 = 'test/rawdata1-ReadOnly.csv'
   raw2 = 'test/rawdata2-ReadOnly.csv'
   ```

   改为：

   ```python
   resource1 = '../test/resource-1.csv'
   resource2 = '../test/resource-2.csv'
   raw1 = 'rawdata1-ReadOnly.csv'
   raw2 = 'rawdata2-ReadOnly.csv'
   ```

   
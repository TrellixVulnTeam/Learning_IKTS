#返回在元组（2,5,3,7）索引号为 2 的位置插入元素 9 之后的新元组。
tuple = (*(2,5,3,7)[:2],9,*(2,5,3,7)[2:])
print(tuple)
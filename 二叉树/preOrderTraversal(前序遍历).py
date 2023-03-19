# _*_ coding : utf-8 _*_
# @Time : 2023/3/19 14:29
# @Author : HackWu
# @File : preOrderTraversal(前序遍历)
# @Project : DS-Code

class TreeNode():   #定义树节点
    def __init__(self,data,left=None,right=None):
        self.data=data          #data为树节点存储的数据，left为左子树，right为右子树
        self.left=left
        self.right=right


class BinTree():    #定义二叉树
    def __init__(self):
        self.root=None
        self.ls=[]

    def add(self,data):                     #定义add方法，向树结构中添加元素
        node=TreeNode(data)                 #实例化节点为node,并添加跟节点，并将根节点的地址添加到self.ls中
        if self.root==None:
            self.root=node
            self.ls.append(self.root)
        else:
            rootNode=self.ls[0]             #将第一个元素设为根节点
            if rootNode.left==None:         #若根节点的左子树为None,添加左节点，并将其地址添加到self.sl中
                rootNode.left=node
                self.ls.append(rootNode.left)
            elif rootNode.right==None:      #若根节点的右子树为None，添加右节点，并将其地址添加到self.ls中
                rootNode.right=node
                self.ls.append(rootNode.right)
                self.ls.pop(0)                 #弹出self.ls的第一个元素，因为刚才已经被使用过了。

    def preOrderTraversal(self,root):       #前序遍历(根左右)： 递归实现
        if root==None:                      #若根节点为None，直接返回
            return
        print(root.data)
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)

    def preOrderStack(self,root):       #前序遍历(根左右)，使用堆栈实现 ，其实这就相当于是递归的原理
        if root==None:
            return
        stack=[]            #堆栈，用于暂时保存上一次运行的状态，类似于递归的原理
        result=[]           #存储已经处理完成的结果
        node=root           #获取到跟节点
        while node or stack:    #当node不为空，且stack堆栈中还有未完全处理好的程序或者数据时，运行
            while node:     #先处理node
                result.append(node.data)
                stack.append(node)      #还没有完全处理完成，但是先暂存在堆栈中，后续会再次处理
                node=node.left          #更新node的值，为node的左节点，然后继续处理。
            node=stack.pop()            #运行此操作时，证明此路径上的所有左节点，均被处理过了。但是还有右节点未被处理，所以再取出来.pop() 默认取出最后一个元素。
            node=node.right
        print(result)

if __name__ == '__main__':
    #如果想向树中添加数据data = [1,2,3,4,5,6,7,8,9,10]，那么可使用如下代码：
    tree=BinTree()      #实例化一个数对象，创建一个空树
    for i in range(1,11):       #创建一个非空二叉树
        tree.add(i)

    tree.preOrderTraversal(tree.root)   #使用递归
    tree.preOrderStack(tree.root)       #使用堆栈

    '''
    树结构：
                         1                                                 
                       /   \
                      /     \
                     /       \
                    /         \
                   /           \
                  /             \
                 /               \
                /                 \
             2                       3                         
           /   \                   /   \
          /     \                 /     \
         /       \               /       \
        /         \             /         \
       4           5           6           7             
     /   \       /   \       /   \       /   \
    /     \     /     \     /     \     /     \
    8     9     10    N     N     N     N     N       


遍历结果：1、2、4、8、9、5、10、3、6、7。
    '''
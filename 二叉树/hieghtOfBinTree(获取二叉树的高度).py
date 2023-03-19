# _*_ coding : utf-8 _*_
# @Time : 2023/3/19 15:26
# @Author : HackWu
# @File : hieghtOfBinTree(获取二叉树的高度)
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

    def heightOfBT(self,root):
        if root==None:
            return 0
        HL=self.heightOfBT(root.left)
        HR=self.heightOfBT(root.right)
        if HL > HR:
            return HL+1
        else:
            return HR+1


if __name__ == '__main__':
    #如果想向树中添加数据data = [1,2,3,4,5,6,7,8,9,10]，那么可使用如下代码：
    tree=BinTree()      #实例化一个数对象，创建一个空树
    for i in range(1,11):       #创建一个非空二叉树
        tree.add(i)

    height=tree.heightOfBT(tree.root)
    print(height)


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


遍历结果：4。
    '''



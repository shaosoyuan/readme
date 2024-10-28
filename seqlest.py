"""class SequenceLest(object):
	def __init__(self):
		self.SeqLest=[]
	def CreatSequenceLest(self):
		print("**************************************")
		print("输入数据后按回车确定，想要结束按#")
		print("**************************************")
		Element=input("请输入元素：")
		while Element!='#':
			self.SeqLest.append(int(Element))
			Element=input("请输入元素：")
	def FindElement(self):
		key=int(input("想要查找的值："))
		if key in self.SeqLest:
			ipos=self.SeqLest.index(key)
			print("查找成功，该元素位于当前顺序表第",ipos+1,"位")
		else:
			print("查找失败")
	def InsertElement(self):
		ipos=int(input('请输入插入元素的位置：'))
		Element=int(input('请输入插入的元素：'))
		self.SeqLest.insert(ipos,Element)
		print('插入后，当前表为:\n',self.SeqLest)
	def DeleteElement(self):
		dpos=int(input('请输入删除元素的位置：'))
		print('正在删除元素',self.SeqLest[dpos],"...")
		self.SeqLest.remove(self.SeqLest[dpos])
		print('删除后，当前表为:\n',self.SeqLest)
	def TraverseElement(self):
		SeqLestLen=len(self.SeqLest)
		print('*********遍历顺序表元素**********')
		for i in range(0,SeqLestLen):
			print('第',i+1,'个元素值为',self.SeqLest[i])
	def GetElement(self):
		while True:
			print("**************************************")
			print("扣一送地狱火")
			print("1:最大值")
			print("2:最小值")
			print("3:最大值和最小值")
			print("0:退出")
			print("**************************************")
			i=int(input("请输入"))
			if i==1:
				print("最大值：",max(self.SeqLest))
			elif i==2:
				print("最小值：",min(self.SeqLest))
			elif i==3:
				print("最小值：",min(self.SeqLest))
				print("最大值：",max(self.SeqLest))
			elif i==0:
				break
SeqLest = SequenceLest()
SeqLest.CreatSequenceLest()
SeqLest.GetElement()
#SeqLest.FindElement()
#SeqLest.InsertElement()
#SeqLest.DeleteElement()
#SeqLest.TraverseElement()
"""
"""
class Node(object):
	def __init__(self,date):
		self.date=date
		self.next=None
#单链表		
class SingleLinkedList(object):
	def __init__(self):
		self.head=Node(None)
		
	def CreateSingleLinkedList(self):
		print("**************************************")
		print("输入数据后按回车确定，想要结束按#")
		print("**************************************")
		cNode=self.head
		Element=input("当前结点的值：")
		while Element!="#":
			nNode=Node(eval(Element))
			cNode.next=nNode
			cNode=cNode.next
			Element=input("当前结点的值：")
	
	def InsertElementInTail(self):
		Element=(input("请输入待插入尾结点的值:"))
		if Element=="#":
			return
		cNode=self.head
		nNode=Node(int(Element))
		while cNode.next!=None:
			cNode=cNode.next
		cNode.next=nNode
	
	def TraverseElement(self):
		cNode=self.head
		if cNode.next==None:
			print("为空！")
			return
		print("当前单链表为：")
		while cNode!=None:
			cNode=cNode.next
			if cNode!=None:
				print(cNode.date,"->",end=" ")
			else:
				 print("None")
	def InsertElementInHead(self):
		Element=(input("请输入待插入头结点的值:"))
		if Element=="#":
			return
		cNode=self.head
		tNode=cNode.next
		nNode=Node(int(Element))
		cNode.next=nNode
		nNode.next=tNode
	def FindElement(self):
		cNode=self.head
		if cNode.next == None:
			print("空链表")
			return
		count=0
		Element=eval(input("请输入查询的值"))
		while cNode.next != None:
			cNode=cNode.next
			count+=1
			if cNode.date == Element:
				print("查询成功",Element,count)
				break
		if(cNode.date != Element):
			print("查询失败")
		
	def GetLeanth(self):
		cNode=self.head
		leanth=0
		while cNode.next!=None:
			cNode=cNode.next
			leanth+=1
		print("链表长为",leanth)
		return
	
	def DeleteElement(self):
		dElement=eval(input("想要删除的元素："))
		cNode=self.head
		tNode=self.head
		if cNode.next == None:
			print("空链表")
			return
		while cNode.next!=None and cNode.date!=dElement:
			tNode=cNode
			cNode=cNode.next
		if cNode.date==dElement:
			tNode.next=cNode.next
			del cNode
			print("删除成功")
		else:
			print("删除失败，没这玩意")














"""

"""
SingleLinkedList = SingleLinkedList()
SingleLinkedList.CreateSingleLinkedList()
#SingleLinkedList.TraverseElement()
#SingleLinkedList.InsertElementInTail()
#SingleLinkedList.TraverseElement()
#SingleLinkedList.InsertElementInHead()
#SingleLinkedList.TraverseElement()
#SingleLinkedList.FindElement()
#SingleLinkedList.GetLeanth()
SingleLinkedList.DeleteElement()
SingleLinkedList.TraverseElement()
"""
"""#循环单链表
class CircularSingleLinkedList(object):
	def __init__(self):
		self.head=Node(None)
		
	def CreateSingleLinkedList(self):
		print("**************************************")
		print("输入数据后按回车确定，想要结束按#")
		print("**************************************")
		cNode=self.head
		Element=input("当前结点的值：")
		while Element!="#":
			nNode=Node(eval(Element))
			cNode.next=nNode
			nNode.next=self.head
			cNode=cNode.next
			Element=input("当前结点的值：")
	
	def InsertElementInTail(self):
		Element=(input("请输入待插入尾结点的值:"))
		if Element=="#":
			return
		cNode=self.head
		nNode=Node(int(Element))
		while cNode.next!=self.head:
			cNode=cNode.next
		cNode.next=nNode
		nNode.next=self.head
	
	def InsertElementInHead(self):
		Element=(input("请输入待插入头结点的值:"))
		if Element=="#":
			return
		cNode=self.head
		tNode=cNode.next
		nNode=Node(int(Element))
		cNode.next=nNode
		nNode.next=tNode
	
	def DeleteElement(self):
		dElement=eval(input("想要删除的元素："))
		cNode=self.head
		tNode=self.head
		if cNode.next == self.head:
			print("空链表")
			return
		while cNode.next!=self.head and cNode.date!=dElement:
			tNode=cNode
			cNode=cNode.next
		if cNode.date==dElement:
			tNode.next=cNode.next
			del cNode
			print("删除成功")
		else:
			print("删除失败，没这玩意")
"""
"""
#双链表
class DoubleLinkedNode(object):
	def __init__(self,date):
		self.date=date
		self.next=None
		self.prev=None
class DoubleLinkedList(object):
	def __init__(self):
		self.head=DoubleLinkedNode(None)
	
	def CreatDoubleLinkedNode(self):
		print("**************************************")
		print("输入数据后按回车确定，想要结束按#")
		print("**************************************")
		Element=input("请输入元素：")
		cNode=self.head
		while Element!="#":
			nNode=DoubleLinkedNode(int(Element))
			cNode.next=nNode
			nNode.prev=cNode
			cNode=cNode.next
			Element=input("请输入元素：")
	
	def InsertElementInTail(self):
		Element=(input("请输入待插入尾结点的值:"))
		if Element=="#":
			return
		cNode=self.head
		nNode=DoubleLinkedNode(int(Element))
		while cNode.next!=None:
			cNode=cNode.next
		cNode.next=nNode
		nNode.prev=cNode
		
	def InsertElementInHead(self):
		Element=(input("请输入待插入头结点的值:"))
		if Element=="#":
			return
		cNode=self.head.next
		pNode=cNode.next
		nNode=DoubleLinkedNode(int(Element))
		pNode.next=nNode
		nNode.next=cNode
		cNode.prev=nNode
		nNode.prev=pNode
	
	def DeleteElement(self):
		dElement=int(input("删除的值"))
		cNode=self.head
		if cNode.next == None:
			print("空链表")
			return
		while cNode.next!=None and cNode.date!=dElement:
			cNode=cNode.next
		if cNode.date==dElement:
			pNode=cNode.prev
			if cNode.next==None:
				pNode.next=None
				del cNode
				print("删除成功")
			else:
				nNode=cNode.next
				nNode.prev=pNode
				pNode.next=nNode
				del cNode
				print("删除成功")
		else:
			print("没这玩意")
DLink=DoubleLinkedList()
DLink.CreatDoubleLinkedNode()
DLink.InsertElementInHead()
DLink.InsertElementInTail()
DLink.DeleteElement()
"""
"""
#循环双链表
class DoubleLinkedNode(object):
	def __init__(self,date):
		self.date=date
		self.next=None
		self.prev=None
		
class CircularDoubleLinkedNode(object):
	def __init__(self):
		self.head=CircularDoubleLinkedNode(None)
"""

"""
class Stack:
	def __init__(self):
		self.MaxStackSize = 10
		self.items = [None for x in range(0,self.MaxStackSize)]
		self.top = -1
	
	def isempty(self):
		if self.top == -1:
			itop=True
		else:
			itop=False
		return itop

	def push(self, item):
		if self.top<self.MaxStackSize-1:
			self.top+=1
			self.items[self.top]=(item)
		else:
			print("栈满")
			return

	def pop(self):
		if self.isempty():
			print("栈空")
			return 
		else:
			itop=self.items[self.top]
			self.items[itop]=None
			self.top-=1
			return itop
	
	def traverse(self):
		if self.isempty():
			print("栈空")
			return 
		else:
			itop=self.top
			while itop!=-1:
				print(self.items[itop],end="")
				self.items[itop]=None
				self.top-=1
				itop=self.top
	def gettop(self):
		if self.isempty():
			print("栈空")
			return
		else:
			return self.items[self.top]
	def create(self):
		date=input("输入元素，#结束")
		while date!="#":
			self.push(date)
			date=input("输入元素，#结束")
	def getlength(self):
		if self.isempty():
			print("栈空")
			return 
		else:
			return self.top+1
ss=Stack()
ss.create()
print("元素为",end="")
ss.traverse()
ss.traverse()
"""
"""
class stacknode:
	def __init__(self,date):
		self.next=None
		self.date=None

class linkstack:
	def __init__(self):
		self.top=stacknode(None)

	def creatstackbyinput(self):
		Element=(input("按'#'结束,请输入入栈的值:"))
		while Element!='#':
			self.pushstack(Element)
			Element=(input("按'#'结束,请输入入栈的值:"))

	def IsEmpty(self):
		if self.top.next==None:
			itop=True
		else:
			itop=False
		return itop	
		
#	def stackvisit(self,element):
#		tnode=self.top
#		while tnode.next!=Node:
			
	def pushstack(self,date):
		tnode=stacknode(date)
		tnode.next=self.top.next
		self.top.next=tnode
		print("当前进栈元素为",date)
		
	def popstack(self):
		if self.IsEmpty()==True:
			print("栈空")
			return
		else:
			tnode=self.top.next
			self.top.next=tnode.next
			cnode=tnode.date
			del tnode
			return cnode
			
	def gettop(self):
		if self.IsEmpty()==True:
			print("栈空")
			return
		else:
			return self.top.next.date
			
stack=linkstack()
stack.creatstackbyinput()
stack.popstack()
"""
"""
#队列
class Queue:
	def __init__(self):
		self.max=10
		self.front=0
		self.rear=0
		self.s=[None for x in range[0,self.max]]
		
	def isempty(self):
		if self.front==10
		self.rear:
			iqueue=True
		else:
			iqueue=False
		return iqueue
		
	def manempty(self):
		if (self.rear+1)%self.max!=self.front:
			iqueue=True
		else:
			iqueue=False
		return iqueue
			
	def EnQueue(self,x):
		if self.manempty():
			print("队满")
		else:
			print("当前进队元素为",x)			
			self.rear = (self.rear+1)%self.max
			self.s[self.rear]=x
	def DeQueue(self):
		if self.isempty():
			print("没东西出不去")
			return
		else:
			itea=self.s[self.front]
			del self.s[self.front]
			self.front=(self.front+1)%self.max
			return itea
	def createnqueue(self):
		date=input("输入元素，‘#号结束’:")
		while date!="#":
			self.EnQueue(date)
			date=input("输入元素，‘#号结束’:")
"""
"""
ABEKLFCGDHMIJ
KLEFBGCMHIJDA
ABCDEFGHIJKLM"""

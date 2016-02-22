import time

class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def level_order_traversal(p):
    
    if p is None:
        return
    
    if p.left:
        print p.left.data
    if p.right:
        print p.right.data
    
    level_order_traversal(p.left)
       
    level_order_traversal(p.right)
    
def pre_order_traversal(p):
    
    if p is None:
        return
    
    if p.left is None and p.right is None:
        print p.data
        return

    print p.data
    
    pre_order_traversal(p.left)
       
    pre_order_traversal(p.right)

def in_order_traversal(p):
    
    if p is None:
        return
    
    if p.left is None and p.right is None:
        print p.data
        return
    
    in_order_traversal(p.left)
       
    print p.data   
        
    in_order_traversal(p.right)
        
def post_order_traversal(p):
    
    if p is None:
        return
    
    if p.left is None and p.right is None:
        print p.data
        return
    
    post_order_traversal(p.left)
        
    post_order_traversal(p.right)
        
    print p.data
    
    
p=Node("p")
c1=Node("c1")
c2=Node("c2")
c3=Node("c3")
c4=Node("c4")
c5=Node("c5")
c6=Node("c6")

p.left=c1
p.right=c2

c1.left=c3
c1.right=c4

c2.left=c5
c2.right=c6

print "Post Order Traversal"
start=time.time()
post_order_traversal(p)
print 'Time: ',time.time()-start
print '-'*50

print "In-Order Traversal"
start=time.time()
in_order_traversal(p)
print 'Time: ',time.time()-start
print '-'*50

print "Pre Order Traversal"
start=time.time()
pre_order_traversal(p)
end=time.time()-start
print 'Time: ',end
print '-'*50

print "Level Order Traversal"
start=time.time()
print p.data
level_order_traversal(p)
end=time.time()-start
print 'Time: ',end

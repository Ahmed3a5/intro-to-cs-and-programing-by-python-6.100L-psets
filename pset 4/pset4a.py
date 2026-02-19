class Node(object):
    """
    class node which take a value and right and left child if has
    """

    def __init__(self , value , left_child= None , right_child =None):
        """
        Docstring for __init__
        
        :param self: object itself
        :param value: the value of the node
        :param right_child: the other node that come after the root
        :param left_child: the other rooot 
        """
        ##  see if the right child is node or not 
        if type(right_child)== Node:
            self.right_child = right_child
        elif right_child == None:
            self.right_child = None
        ## see if the left child is node or not
        if type(left_child) == Node:
            self.left_child = left_child
        elif left_child == None:
            self.left_child = None
        
        self.value  = value
    
    def get_value(self):
        return self.value

    def set_value(self , new_value):
        self.value = new_value
    
    def get_right_child(self):
        return self.right_child
    
    def get_left_child(self):
        return self.left_child
    
    def __eq__(self , tree):

        if type(tree) != Node:
            return False
        else:
            if self.value == tree.value and self.left_child == tree.left_child and self.right_child == tree.right_child:
                return True
            return False
    

tree = Node(5 , Node(5 , Node(8)) , Node(4 , Node(3), Node(1)))


   

def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    # TODO: Remove pass and write your code here
    
    ## the recursive base if the node we explore is a leaf we return 0 as its height 
    if tree.get_right_child() == None and tree.get_left_child() == None:
        return 0 ## return 0
    
    ## if the right child of a node is none so we take the left path and add 1 which is the hieht of the node we condition now 
    elif tree.get_right_child() == None:
    
        return 1+find_tree_height(tree.get_left_child())
    
     ## if the left child of a node is none so we take the right path and add 1 which is the hieht of the node we condition now 

    elif tree.get_left_child() == None:

        return 1+find_tree_height(tree.get_right_child())
    
    ## if the node have right and the left child 
    else:
        ## we find the hight of the left child 
        height_right = find_tree_height(tree.get_right_child())
        ## then find the height of the left child 
        height_left = find_tree_height(tree.get_left_child())
        ## the maximum path 
        maximum = 0
        ## if the right path is the longer or not 
        if height_right > height_left:
            ## we make it the max path
            maximum = height_right
        ## else we make the left as the max path 
        else:
            maximum = height_left
    ## then return the max path and add one to it which account the current node to its child 
        return 1+maximum
    
## test find height of the tree

# tree = Node(5 , Node(5 , Node(8) ,Node(2)) , Node(4 , Node(3), Node(1)))
# tree1 = Node(8 , Node(2 , Node(1) , Node(6)) , Node(10))
# tree2 = Node(7 , Node(2 , Node(1) ,Node(5 , Node(6) ,Node(3))) , Node(9 , Node(8) , Node(10)))
# tree3 = Node(5, Node(3 ,Node(2), Node(4)) , Node(14 , Node(21 , Node(26) , Node(20)) , Node(12)))
# tr1 = Node(13, Node(10, Node(5, Node(4), Node(6)), Node(11)), Node(15, right_child=Node(16,Node(3,Node(20,Node(17))))))
# tr2 = Node(37, Node(24, Node(7, Node(2, right_child = Node(5))), Node(32)), Node(42, Node(40), Node(42, right_child=Node(43,Node(2,Node(14,Node(30)))))))
# tr3 = Node(5, Node(1), Node(5, Node(5)))
# tr4 = Node(5, Node(7, Node(9, Node(10, Node(11)))))
# tr5 = Node(5, right_child=Node(7, right_child=Node(9, right_child=Node(10, right_child=Node(11, right_child=Node(90,Node(2)))))))
# tr6 = Node(5)
# answers = [5, 6, 2, 0,4, 6, 0]
# print(find_tree_height(tr1))
# print(find_tree_height(tr2))
# print(find_tree_height(tr3))
# print(find_tree_height(tr4))
# print(find_tree_height(tr5))
# print(find_tree_height(tr6))


## ===============================================================================================================================
## ===============================================================================================================================
## ===============================================================================================================================

def compare_max_func(child_value , parent_value):

    if child_value < parent_value:
        return True
    return False

def compare_min_func(child_value , parent_value):

    if child_value > parent_value:
        return True
    return False


def is_heap(tree, compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    # TODO: Remove pass and write your code here

    ## if the leaf of the tree reached it is ture 
    if tree.get_right_child() == None and tree.get_left_child() ==None:
        return True
    ## if no right brancg we access the left one 
    elif tree.get_right_child() == None:
        ## if the value of the chid is return true from the compare function if is max or min 
        if compare_func(tree.get_left_child().value , tree.get_value()):    
            ## it recursive the function on the left child to comapre the the paths under the child
            return is_heap(tree.get_left_child() , compare_func)
        ## if the child compare return flase then the child will return false
        return False
    
     ## if the left branch not exist qwe acces the right one 
    elif tree.get_left_child() == None:
        ## we compare the function to the values of the child and the parent 
        if compare_func(tree.get_right_child().value , tree.get_value()): 
            ## if it pass the compare function we recursive the function on the right child branch
            return is_heap(tree.get_right_child() , compare_func)
        ## if it fail the compare function we return false
        return False
    ## if the two branches exist 
    else:
        ## we compare the 2 branches values to the parent value 
        if compare_func( tree.get_right_child().value ,tree.get_value()) and compare_func( tree.get_left_child().value ,tree.get_value()):
            ## if it pass it and return true then we recursive the function is heap to the right and left branches 
            right = is_heap(tree.get_right_child(), compare_func)
            ## recurise function on the left branch 
            left = is_heap(tree.get_left_child() , compare_func)
            ## if the right and the left branches return false then we return false 
            if right != False and left != False: 
                ## we return true beacause the 2 branvhes return true 
                return True
            ## else we return false
            return False
        ## if the comaprison to the right and left branches value to the parent value return false  
        return False  ## return false
        



## test min heap 

# tr1 = Node(5,Node(15,None,Node(16,Node(30),Node(17))),Node(6,Node(20,None,Node(45)),Node(11)))  ## print true
# tr2 = Node(2,Node(3,Node(4),Node(5,Node(6))),Node(7,None,Node(8,Node(9),Node(1))))              ## print false

# tr3 = Node(15,Node(4,Node(3,None,Node(2)),Node(1)),Node(11,Node(10),Node(7,Node(5))))           ## print false
# tr4 = Node(10,Node(7,None,Node(4,Node(3,None,Node(5)))))                                        ## print false 
# print(is_heap(tr1 , compare_min_func))
# print(is_heap(tr2 , compare_min_func))
# print(is_heap(tr3 , compare_min_func))
# print(is_heap(tr4 , compare_min_func))

## test max heap 

# tr1 = Node(15,Node(4,Node(3,None,Node(2)),Node(1)),Node(11,Node(10),Node(7,Node(5))))  ## print true 
# tr2 = Node(10,Node(7,None,Node(4,Node(3,None,Node(5)))))                               ## print false 
# tr3 = Node(2,Node(3,Node(4),Node(5,Node(6))),Node(7,None,Node(8,Node(9),Node(1))))     ## print fasle
# tr4 = Node(5,Node(15,None,Node(16,Node(30),Node(17))),Node(6,Node(20,None,Node(45)),Node(11)))  ## print false

# print(is_heap(tr1 , compare_max_func))
# print(is_heap(tr2 , compare_max_func))
# print(is_heap(tr3 , compare_max_func))
# print(is_heap(tr4 , compare_max_func))





        




from Queue import Queue
class Binary_Search_Tree:

  class __BST_Node:

    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None
      self.height = 0
      
  #insert
  def _insert_recursion(self, node, val):
        if node.value == val:
            raise ValueError
        elif node.value > val:
            if node.left:
                return self._insert_recursion(node.left, val)
            else:
                node.left = self.__BST_Node(val)
        else:
            if node.right:                
                return self._insert_recursion(node.right, val)            
            else:
                node.right = self.__BST_Node(val)
  #height      
  def _height(self, node):
        if node.left and node.right:
            return 1 + max(self._height(node.left), self._height(node.right))
        elif node.left:
            return 1 + self._height(node.left)
        elif node.right:
            return 1 + self._height(node.right)
        else:
            return 1
        
  #remove_element
  def _remove_recursion(self, val, node):
    if node is None :
        raise ValueError
    elif node.value == val :
        if node.left and node.right:
            right_side = node.right
            while right_side.left:
                right_side = right_side.left
            node.value = right_side.value
            node.right = self._remove_recursion(right_side.value, node.right)
        elif node.left == None:
            node = node.right
        else:
            node = node.left     
    elif val <= node.value :
        node.left = self._remove_recursion(val, node.left)
    elif val > node.value :
        node.right = self._remove_recursion(val, node.right)
    return node
  
  #pre_order private
  def _pre_order_rec(self, node, ret):
      ret = ret + str(node.value) + ", "
      if node.left is not None:
          ret = self._pre_order_rec(node.left, ret)
      if node.right is not None:
          ret = self._pre_order_rec(node.right, ret)
      return ret
  def _pre_order(self):
    #base case
    if self.__root is None:
          return"[ ]"    
    else:
        po_string = "[ "
        po_string = self._pre_order_rec(self.__root, po_string)
        po_string = po_string[0:-2] + " ]"
        return po_string
    
  #in_order private
  def _in_order_rec(self, node, ret):
    if node.left is None:
        ret += str(node.value) + ", "
    else:
        ret = self._in_order_rec(node.left, ret)
        ret += str(node.value) + ", "
    if node.right is not None:
        ret = self._in_order_rec(node.right, ret)
    return ret        
  def _in_order(self):
    #base case
    if self.__root is None:
        return "[ ]"
    else:
        io_string = "[ "
        io_string = self._in_order_rec(self.__root, io_string)
        io_string = io_string[0:-2] + " ]"
        return io_string
    
  #post_order private
  def _post_order_rec(self, node, ret):
      if node.left is not None:
          ret = self._post_order_rec(node.left, ret)
      if node.right is None:
          ret = ret + str(node.value) + ", "
      else:
          ret = self._post_order_rec(node.right, ret)
          ret = ret + str(node.value) + ", "
      return ret
  def _post_order(self):
    #base case
    if self.__root is None:
        return "[ ]"
    else:
        poo_string = "[ "
        poo_string = self._post_order_rec(self.__root, poo_string)
        poo_string = poo_string[0:-2] + " ]"
        return poo_string
        
      
  def __init__(self):
      self.__root = None
    
  def insert_element(self, val):
      if self.__root:
          self._insert_recursion(self.__root, val)
          self.__root.height = self._height(self.__root) 
      else:
          self.__root = self.__BST_Node(val)
          self.__root.height = self._height(self.__root)

  def remove_element(self, value):
      self.__root = self._remove_recursion(value, self.__root)
      if self.__root:
          self.__root.height = self._height(self.__root)
	
  def in_order(self):
    return self._in_order()
    
  def pre_order(self):
    return self._pre_order()

  def post_order(self):
    return self._post_order()
    
  def breadth_first(self):
     if self.__root is None:
         return "[ ]"
     ret = "[ "
     horizontal_tra = Queue()
     horizontal_tra.enqueue(self.__root)
     while len(horizontal_tra) != 0:
         pop = horizontal_tra.dequeue()
         if pop.left is not None and pop.right is not None:
             horizontal_tra.enqueue(pop.left)
             horizontal_tra.enqueue(pop.right)
             ret = ret + str(pop.value) + ", "
         elif pop.left:
            horizontal_tra.enqueue(pop.left)
            ret = ret + str(pop.value) + ", "
         elif pop.right:
            horizontal_tra.enqueue(pop.right)
            ret = ret + str(pop.value) + ", "
         elif not pop.right and not pop.left and len(horizontal_tra) == 0:
            ret = ret + str(pop.value) + " ]"
         elif not pop.right and not pop.left:
            ret = ret + str(pop.value) + ", "
     return ret
    
  def get_height(self):
      if self.__root:
          return self.__root.height
      else:
          return 0

  def __str__(self):
    return self.in_order()
    
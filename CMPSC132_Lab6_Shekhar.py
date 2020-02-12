#The LinkedList class

class LinkedList:

  def __init__(self):
      
    self.__head = None
    self.__tail = None
    self.__size = 0

##################################################################################################
  # Add an element to the beginning of the list 
  def addFirst(self, e):

    newNode = Node(e) # Create a new node
    newNode.next = self.__head # link the new node with the head
    self.__head = newNode # head points to the new node
    self.__size += 1 # Increase list size

    if self.__tail == None: # the new node is the only node in list
      self.__tail = self.__head

##################################################################################################
  # Add an element to the end of the list 
  def addLast(self, e):

    newNode = Node(e) # Create a new node for e

    if self.__tail == None:
      self.__head = self.__tail = newNode # The only node in list
    else:
      self.__tail.next = newNode # Link the new with the last node
      self.__tail = self.__tail.next # tail now points to the last node

    self.__size += 1 # Increase size

##################################################################################################
  # Insert a new element at the specified index in this list
  # The index of the head element is 0 
  def add(self, index, e):

    if index == 0:
      self.addFirst(e) # Insert first

    elif index >= self.__size:
      self.addLast(e) # Insert last

    else: # Insert in the middle
      current = self.__head

      for i in range(1, index):
        current = current.next

      temp = current.next
      current.next = Node(e)
      (current.next).next = temp
      self.__size += 1


##################################################################################################

  # Remove the head node and
  #  return the object that is contained in the removed node. 
  def removeFirst(self):

    if self.__size == 0:
      return None # Nothing to delete
    else:
      temp = self.__head # Keep the first node temporarily
      self.__head = self.__head.next # Move head to point the next node
      self.__size -= 1 # Reduce size by 1

      if self.__head == None: 
        self.__tail = None # List becomes empty 

      return temp.element # Return the deleted element

##################################################################################################
  # Remove the last node and
  # return the object that is contained in the removed node
  def removeLast(self):

    if self.__size == 0:
      return None # Nothing to remove

    elif self.__size == 1: # Only one element in the list
      temp = self.__head
      self.__head = self.__tail = None  # list becomes empty
      self.__size = 0
      return temp.element

    else:
      current = self.__head

      for i in range(self.__size - 2):
        current = current.next
    
        temp = self.__tail
        self.__tail = current
        self.__tail.next = None
        self.__size -= 1
        return temp.element
        
##################################################################################################
  # Remove the element at the specified position in this list.
  #  Return the element that was removed from the list. 
  def remove(self, index):

    if index < 0 or index >= self.__size:
      return None # Out of range
    elif index == 0:
      return self.removeFirst() # Remove first 
    elif index == self.__size - 1:
      return self.removeLast() # Remove last
    else:
      previous = self.__head

      for i in range(1, index):
        previous = previous.next
  
      current = previous.next
      previous.next = current.next
      self.__size -= 1
      return current.element

##################################################################################################  
  # Return the size of the list
  def getSize(self):

    return self.__size

##################################################################################################
  # Clear the list */
  def clear(self):

    self.__head = self.__tail = None

##################################################################################################
  # Return the element from this list at the specified index   
  def get(self, index): 

    current = self.__head # Initialise  
    check = 0 

    while current != None: 

      if check == index: 
        return current.element 

      check += 1
      current = current.next


##################################################################################################   
# The Node class

class Node:

  def __init__(self, e):
    self.element = e
    self.next = None

##################################################################################################        

        
        

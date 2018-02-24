'''
Question 1

Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and t = "ad", then the function returns True. Your function definition should look like: question1(s, t) and return a boolean True or False.

Time complexity: O(len(s)*t)
Space complexity: O(len(t))
'''

def question1(s="",t="",):
    # init an empty list to store the checked letters
    li = []
    # check for empty inputs
    if s == "" and t == "":
      return True
    # check if the entered var is string
    if s.isalpha() and t.isalpha():
        #loop thorugh each letter in t
        for i in t:
            # check each letter againts s
            # we want to return 'pass' if it passes the following conditions
            # 1. the ith letter is in s, 2. li is not empty, 3. the index of ith letter exactly matches the index of last most letter in the li list + 1 (this is the test for adjacency)
            if (s.find(i) != -1) and (len(li) != 0) and (s.find(i) == s.find(li[-1])+1):
                pass
            # we store the first letter since the list is empty
            elif (s.find(i) != -1) and (len(li) == 0):
                li.append(i)
            else:
                # return False immidietly if even one letter fails
                return False
        # lastly return True if the entire process does pass
        return True
    else:
        # return False if and only if it fails the String check in the first place
        return False

print('Test Cases for Question 1:')

print(question1('', ''))
# Should print True

print(question1('', 'a'))
# Should print False

print((question1(s="udacity",t="4",)))
# Should print False

print(question1("udacity", "uy"))

print(question1('udacity', 'udacity'))
# Should print True

print(question1('udacity', 'ad'))
# Should print True

print(question1('abcdefghijklmnopqrstuvwxyz', 'udacity'))
# Should print True


'''
Question 2

Given a string a, find the longest palindromic substring contained in a. Your function definition should look like question2(a), and return a string.

Time complexity: O(n^2)
Space complexity: O(1)
'''

def question2(text):

    # check to make sure if the text is just a single word,
    # return that single word
    if len(text) <= 1:
        return text

    # define a longest var to store the returning var
    longest = ""
    # check through eacg letter
    for i in range(len(text)):
        # check through each subtstring from the first letter to the very recent
        for j in range(0, i):
            substring = text[j:i+1]
            # check to make sure that substring is a Palindrome
            if substring == substring[::-1]:
                # check to see if the new obtained substring is longest
                if len(substring) > len(longest):
                    # set max palindrome
                    longest = substring

    # check to see if the longest substring is 0, then just return the input text's first letter
    if len(longest) == 0:
        return text[0]

    return longest

print(question2(''))
# Should print ''

print(question2('abc'))
# Should print 'a'

print(question2('aba'))
# Should print 'aba'

print(question2('abcba'))
# Should print 'abcba'

print(question2("forgeeksskeegfor"))
# Should print 'geeksskeeg'

print(question2("MOM is a MADAM and RACECAR DAD"))
# Should print


'''
Question 3

Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this: {'A': [('B', 2)], 'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]} Vertices are represented as unique strings. The function definition should be question3(G)

Time complexity: O(# of Edges * # of Vertices)
Space complexity: O(# of Vertices)
'''

# This is very similar and in essence inspired by the 'Prim Algorithm'

def question3(Graph):

    # initially check for the length of the input Graph
    # if length of input graph is less than, just return that graph/node its self
    if len(Graph) < 1:
        return Graph

    # initalize the nodes var
    # the var node stores the keys of the input graph/dict
    nodes = set(Graph.keys())

    # initialize a new dict
    master = {}
    # initialize the parent node of the input graph's keys
    start = list(Graph.keys())[0]
    # initialize the new parent node of the var which will be returned
    master[start] = []

    while len(master.keys()) < len(nodes):
        min_w = float('inf')
        min_edge = None
        for node in master.keys():
            edges = [(weight, vertex) for (vertex, weight) in Graph[node] if vertex not in master.keys()]
            if len(edges) > 0:
                w, v = min(edges)
                if w < min_w:
                    min_w = w
                    min_edge = (node, v)
        master[min_edge[0]].append((min_edge[1], min_w))
        master[min_edge[1]] = [(min_edge[0], min_w)]
    return master


print('Test Cases for Question 3:')

print(question3({}))
# Should print {}

print(question3({'A': []}))
# Should print {'A': []}

print(question3({'A': [('B', 3), ('E', 1)],
                 'B': [('A', 3), ('C', 9), ('D', 2), ('E', 2)],
                 'C': [('B', 9), ('D', 3), ('E', 7)],
                 'D': [('B', 2), ('C', 3)],
                 'E': [('A', 1), ('B', 2), ('C', 7)]}))
# Should print
# {'A': [('E', 1)],
#  'C': [('D', 3)],
#  'B': [('E', 2), ('D', 2)],
#  'E': [('A', 1), ('B', 2)],
#  'D': [('B', 2), ('C', 3)]}

'''
Question 4

Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest node from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix, where the index of the list is equal to the integer stored in that node and a 1 represents a child node, r is a non-negative integer representing the root, and n1 and n2 are non-negative integers representing the two nodes in no particular order. For example, one test case might be

question4([[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 1], [0, 0, 0, 0, 0]], 3, 1, 4) and the answer would be 3.

Time complexity for balances BST: O(log(len(depth)))
Time complexity for unbalanced: O(n)
Space complexity: O(len(depth))
'''

def question4(T, r, n1, n2):

    # check edge cases
    if len(T) == 0:
        return T
    elif len(T) == 1:
        return r

    if n1 == None or n2 == None:
      return []

    # checks if n1 and n2 are on different sides of the root
    if (n1 > r and n2 < r) or (n1 < r and n2 > r):
        # returns root if n1 and n2 are on different sides
        # because in this case the root is the only common ancestor
        return r

    # checks if both n1 and n2 are smaller than root
    elif (n1 < r and n2 < r):
        left = T[r].index(1)
        # checks if n1 or n2 equals left child of root
        if n1 == left or n2 == left:
            return r
        # else change root to left child
        else:
            r = left
    # checks if both n1 and n2 are greater than root
    elif (n1 > r and n2 > r):
        right = len(T[r]) - T[r][::-1].index(1) - 1
        # checks if n1 or n2 equals right child of root
        if n1 == right or n2 == right:
            return r
        else:
            # changes root to right child
            r = right

    # runs recursively with updated root
    return question4(T, r, n1, n2)

print('Test Cases for Question 4:')

print(question4([],
                None,
                None,
                None))
# Should print []

print(question4([[0]],
                0,
                0,
                0))
# Should print 0

print(question4([[0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                3,
                1,
                4))
# Should print 3

print(question4([[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 1, 0, 0],
                 [1, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0]],
                1,
                0,
                6))
# Should print 2

'''
Question 5

Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.

class Node(object): def init(self, data): self.data = data self.next = None</pre

Time complexity: O(# of nodes)
Space complexity: O(1)
'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def question5(ll, m):
    # initally check to make sure the first node exists
    if ll:
        # initialize the index to 1
        index = 1
        # initialize the parent node
        node = ll
        # loop through the linkedlist whilst node.next is true,
        # the objective is to arrive at the end of linkedlist
        while node.next:
            # init the current node
            node = node.next
            # increase the index
            index += 1
        # check to see if the mth number is less than the current last index
        if m < index:
            # n is initialized as the diff between current index and mth number
            n = index - m
            # init the i, to loop through the remaining linkedlist
            i = 0
            # node is defined as same
            node = ll
            # loop through the sub-linkedlist to find the position of mth number
            while i < n:
                node = node.next
                i += 1
        else:
            # else if the m is not less than current last index then return None
            return None
    else:
        # just return the node.data if ll fails first test
        node = ll
    return node.data

Node0 = Node(None)
print(question5(Node0, 1))
# Should print None

Node0 = Node(0)
print(question5(Node0, 2))
# Should print None


Node0 = Node(0)
Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)
Node0.next = Node1
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5

print(question5(Node0, 7))
# Should print None

Node0 = Node(0)
Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)
Node6 = Node(6)
Node7 = Node(7)
Node8 = Node(8)
Node9 = Node(9)
Node0.next = Node1
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5
Node5.next = Node6
Node6.next = Node7
Node7.next = Node8
Node8.next = Node9
print(question5(Node0, 5))
# Should print 5

## Binary Tree
* if a node is at index i, then
* left child is at 2*i
* right child is at 2*1+1
* parent child is at i// (floor)
* height is logn

## Binary Tree

1. Full Binary Tree
when there is no space for a new node, if a new node has to be inserted, that will increase height of the tree  
no. of nodes = 2^(h+1) - 1

2. Complete binary tree
when converted a BT into array and if there is no null in array, it is complete binary tree

## Heap
* Heap is complete binary tree
* max heap is a complete binary tree and every root node is greater than or equal to both child elements
* min heap is a complete binary tree and every root node is smaller than or equal to both child elements (smallest element is root)

### Max Heap

#### insertion in max heap
insert new element in the end(leaf), then swap the new element with its parent and climb the ladder till it reaches the right place

#### deletion in max heap
* we always delete the root element then the last leaft takes place of the root
* now we compare the root with it's child, and whichever is greater we swap root with the element, provided root should be smaller than child, if not no need to swap

### Heapify

creation of heap
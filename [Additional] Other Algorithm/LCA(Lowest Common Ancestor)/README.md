### LCA(Lowest Common Ancestor)  
- 최소 공통 조상을 찾는 알고리즘  
```
//O(N)
Node LCA(Node root, Node n1, Node n2){
    if(root == NULL)
        return NULL;
    if(root == n1 || root == n2)
        return root;

    Node left = LCA(root.left, n1, n2);   // left 노드와 right 노드를 찾는다.
    Node right = LCA(root.right, n1, n2);

    if(left != NULL && right != NULL)    // left, right가 둘다 NULL이 아니면, root가 최소 공통 조상이다.
        return root;
    if(left == NULL && right == NULL)    // left, right를 트리에서 찾을 수 없는 경우는 NULL을 반환
        return NULL;

    return left != NULL ? left, right;   // 둘중에 하나가 NULL이라면, NULL이 아닌 것을 반환
}
```
출처 : https://www.youtube.com/watch?v=13m9ZCB8gjw   

### 
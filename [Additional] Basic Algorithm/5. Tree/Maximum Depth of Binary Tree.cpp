class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(!root)
            return 0;
        queue<pair<TreeNode*, int>> q;
        q.push({root, 0});
        int dep;
        int _max = -1;
        while(!q.empty())
        {
            TreeNode *r = q.front().first;
            dep = q.front().second;
            q.pop();
            if(r->left)
                q.push({r->left, dep + 1});
            
            if(r->right)
                q.push({r->right, dep + 1});
            
            _max = dep + 1 > _max ? dep + 1: _max;
        }
        return _max;
    }
};
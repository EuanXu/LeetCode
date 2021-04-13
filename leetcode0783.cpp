/*************************************************************************
	> File Name: leetcode0559.cpp
	> Author: EuanXu
	> Mail: 
	> Created Time: 二  4/13 22:29:05 2021
    > leetcode: 783.二叉搜索树节点最小距离
 ************************************************************************/
void dfs(struct TreeNode* root, int* pre, int* ans) {
    if (root == NULL) {
        return;
    }
    dfs(root->left, pre, ans);
    if (*pre == -1) {
        *pre = root->val;
    } else {
        *ans = fmin(*ans, root->val - (*pre));
        *pre = root->val;
    }
    dfs(root->right, pre, ans);
}

int minDiffInBST(struct TreeNode* root) {
    int ans = INT_MAX, pre = -1;
    dfs(root, &pre, &ans);
    return ans;
}


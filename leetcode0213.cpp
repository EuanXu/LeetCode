/*************************************************************************
	> File Name: leetcode0213.cpp
	> Author: EuanXu
	> Mail: 
	> Created Time: 四  4/15 23:39:21 2021
    > 213.打家劫舍2
 ************************************************************************/
int robRange(int* nums, int start, int end) {
    int first = nums[start], second = fmax(nums[start], nums[start + 1]);
    for (int i = start + 2; i <= end; i++) {
        int temp = second;
        second = fmax(first + nums[i], second);
        first = temp;
    }
    return second;
}

int rob(int* nums, int numsSize) {
    if (numsSize == 1) {
        return nums[0];
    } else if (numsSize == 2) {
        return fmax(nums[0], nums[1]);
    }
    return fmax(robRange(nums, 0, numsSize - 2), robRange(nums, 1, numsSize - 1));
}



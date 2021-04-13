/*************************************************************************
	> File Name: leetcode0005.cpp
	> Author: EuanXu
	> Mail: 
	> Created Time: 二  4/13 22:51:55 2021
 ************************************************************************/
#include <stdio.h>

bool isPalindrome(long long int x) {
    if(x < 0 || (x % 10 == 0 && x != 0)) return false;
    long long int temp = x, n = 0;
    while(temp) {
        n = n * 10 + temp % 10;
        temp /= 10;
    }
    return x == n ? true : false;
}

int main() {
    long long int n;
    scanf("%lld", &n);
    isPalindrome(n);
    return 0;
}


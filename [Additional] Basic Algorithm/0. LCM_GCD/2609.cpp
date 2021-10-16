#include <iostream>
#include <vector>
using namespace std;
/*
	최소 공배수 : the least common multiple(LCM)
	최대 공약수 : the greates common denominator(GCD) 
*/
int arr[10];
int num[42]; //0 ~ 41
int main(void)
{
	int T, test_case;
	int l, r;
	cin >> l >> r;

    int _min = min(l, r);
	int max = 10001;
	int min = 0;
	int lcm, gcd;
	for (int i = 1; i <= _min; i++) {  //1도 최소 공배수가 됨을 잊지 말자
		if (l%i == 0 && r%i == 0 && i > min) {
			min = gcd = i;
		}
	}
	lcm = l * r / gcd;
	
	cout << gcd << endl;
	cout << lcm << endl;

	return 0;

}
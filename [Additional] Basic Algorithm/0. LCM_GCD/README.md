## LCM_GCD  

최대 공약수(LCM), 최대 공배수(GCD) 구하는법  
- 그냥 외우자
  ```c++
  	cin >> l >> r;
    int _min = min(l, r);
	int lcm, gcd;
	for (int i = 1; i <= _min; i++) { //1도 최소 공배수가 됨을 잊지 말자
		if (l%i == 0 && r%i == 0) {
			gcd = i;
		}
	}
    lcm = l * r / gcd;
  ```
- GCD 구하는 다른 방법
  ``` c++
    int gcd(int l, int r) {
        if (r == 0) return l;
        return gcd(r, l%r);
    }

    int gcd(int l, int r) {
        while (r != 0) {
            int m = l % r;
            l = r;
            r = m;
        }
        return l;
    }
  ```
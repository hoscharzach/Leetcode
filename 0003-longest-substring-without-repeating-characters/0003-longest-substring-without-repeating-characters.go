func lengthOfLongestSubstring(s string) int {
	var e uint16 = uint16(len(s))
	var m, n, l, r uint16
	var c byte
	dic := make(map[byte]uint16)
	for ; r <= e; r++ {
		if r != e {
			c = s[r]
		} else {
			c = 0x20
			n = r - l
		}
		if d, ok := dic[c]; ok {
			if l == 0 {
				n = r
			} else {
				n = r - l
			}
			if d >= l {
				l = d + 1
			}
		}
		dic[c] = r
		if n > m {
			m = n
		}
	}
	return int(m)
}
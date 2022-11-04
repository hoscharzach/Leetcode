func reverseVowels(s string) string {
    buf := []byte(s)
    for i, j := 0, len(s)-1; i < j; {
        m, n := isVowel(buf[i]), isVowel(buf[j])
        if m && n {
            buf[i], buf[j] = buf[j], buf[i]
            i++
            j--
        }
        if !m {
            i++
        }
        if !n {
            j--
        }
    }
    return string(buf)
}

func isVowel(c byte) bool {
    switch c {
        case 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U':
            return true
        default:
            return false
    }
}
func largestTimeFromDigits(A []int) string {
    largestTime := ""
    for x := 0; x < 4; x++ {
        for y := 0; y < 4; y++ {
            if y == x {
                continue
            }
            for z := 0; z < 4; z++ {
                if z == y || z == x {
                    continue
                }
                for m := 0; m < 4; m++ {
                    if m == z || m == y || m == x {
                        continue
                    }
                    if curTime := tranToTime(A[x], A[y], A[z], A[m]); curTime > largestTime {
                        largestTime = curTime
                    }
                }
            }
        }
    }
    return largestTime
}

func tranToTime(x, y, z, m int) string {
    hour := x * 10 + y
    if hour >= 24 {
        return ""
    }
    minu := z * 10 + m
    if minu >= 60 {
        return ""
    }
    return fmt.Sprintf("%02s:%02s", strconv.Itoa(hour), strconv.Itoa(minu))
}
class daa {
    var first: [Int]
    var second: [Int]
    var iterfirst: Int = 0
    var itersecond: Int = 0
    var sum1: Int = 0
    var sum2: Int = 0

    init(_ first: [Int], _ second: [Int]) {
        self.first = first
        self.second = second
    }

    func solve() -> Int {
        let length = (first.remove(at: 0), second.remove(at: 0))

        while iterfirst < length.0, itersecond < length.1 {
            if first[iterfirst] > second[itersecond] {
                inc_second()
            } else if first[iterfirst] < second[itersecond] {
                inc_first()
            } else {
                inc_first()
                inc_second()
                if sum1 < sum2 {
                    sum1 = sum2
                } else {
                    sum2 = sum1
                }
            }
        }

        while iterfirst < length.0 {
            inc_first()
        }
        while itersecond < length.1 {
            inc_second()
        }

        return max(sum1, sum2)
    }

    func inc_first() {
        sum1 += first[iterfirst]
        iterfirst += 1
    }

    func inc_second() {
        sum2 += second[itersecond]
        itersecond += 1
    }
}

while true {
    let first = readLine()?.split(separator: " ").map { Int(String($0))! }
    if first?[0] == 0 { break }
    let second = readLine()?.split(separator: " ").map { Int(String($0))! }
    print(daa(first!, second!).solve())
}

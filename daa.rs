fn input() -> Vec<i64> {
    let mut input = String::new();
    std::io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");
    input
        .trim()
        .to_string()
        .split(' ')
        .map(|s| s.parse().expect("Please type a number!"))
        .collect()
}

fn main() {
    loop {
        let mut num1 = input();
        if num1[0] == 0 {
            break;
        }
        let len1: usize = num1.remove(0) as usize;

        let mut num2 = input();
        let len2: usize = num2.remove(0) as usize;

        let (mut iter1, mut iter2, mut sum1, mut sum2) = (0usize, 0usize, 0i64, 0i64);
        while iter1 < len1 && iter2 < len2 {
            if num1[iter1] > num2[iter2] {
                sum2 += num2[iter2];
                iter2 += 1;
            } else if num1[iter1] < num2[iter2] {
                sum1 += num1[iter1];
                iter1 += 1;
            } else {
                sum2 += num2[iter2];
                sum1 += num1[iter1];
                if sum1 < sum2 {
                    sum1 = sum2
                } else {
                    sum2 = sum1
                }
                iter2 += 1;
                iter1 += 1;
            }
        }
        while iter1 < len1 {
            sum1 += num1[iter1];
            iter1 += 1;
        }
        while iter2 < len2 {
            sum2 += num2[iter2];
            iter2 += 1;
        }
        println!("{}", std::cmp::max(sum1, sum2));
    }
}

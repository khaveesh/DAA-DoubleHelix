use std::{
    cmp::{max, Ordering},
    io::stdin,
};

fn input() -> Vec<i64> {
    let mut input = String::new();
    stdin().read_line(&mut input).expect("Failed to read line");
    input
        .split_whitespace()
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
            match num1[iter1].cmp(&num2[iter2]) {
                Ordering::Less => {
                    sum1 += num1[iter1];
                    iter1 += 1;
                }
                Ordering::Greater => {
                    sum2 += num2[iter2];
                    iter2 += 1;
                }
                Ordering::Equal => {
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
        }
        while iter1 < len1 {
            sum1 += num1[iter1];
            iter1 += 1;
        }
        while iter2 < len2 {
            sum2 += num2[iter2];
            iter2 += 1;
        }
        println!("{}", max(sum1, sum2));
    }
}

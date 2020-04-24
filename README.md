# Report - ANARC05B - The Double HeLiX

---

## Table of contents

- [Report - ANARC05B - The Double HeLiX](#report---anarc05b---the-double-helix)
    - [Table of contents](#table-of-contents)
    - [Run](#run)
    - [Problem Statement](#problem-statement)
        - [Input](#input)
        - [Output](#output)
        - [Conditions](#conditions)
    - [Algorithm](#algorithm)
        - [Simple Approach](#simple-approach)
        - [Greedy Approach](#greedy-approach)
    - [Pseudo Code](#pseudocode)
        - [Simple Approach](#simple-approach-1)
        - [Greedy Approach](#greedy-approach-1)
    - [Proof of Correctness](#proof-of-correctness)
        - [Simple Approach](#simple-approach-2)
        - [Greedy Approach](#greedy-approach-2)
    - [Complexity](#complexity)
        - [Simple Approach](#simple-approach-3)
        - [Greedy Approach](#greedy-approach-3)
    - [Other Details](#other-details)
        - [Side Effects in the code](#side-effects-in-the-code)
    - [Contributions and Bibliography](#contributions-and-bibliography)

---

## Run

Change your current working directory by going into `DAA-DoubleHelix`

> cd DAA-DoubleHelix

To run both the algorithms and all the tests

> make

To run only algorithms:

> make run

To run the tests

> make test

---

## Problem Statement

[Source](https://www.spoj.com/problems/ANARC05B/)

Two ﬁnite, strictly increasing, integer sequences are given. Any common integer between the two sequences constitute an intersection point. Take for example the following two sequences where intersection points are printed in bold:

First= 3 5 **7** 9 20 **25** 30 40 **55** 56 **57** 60 62

Second= 1 4 **7** 11 14 **25** 44 47 **55** **57** 100

You can _walk_ over these two sequences in the following way:

You may start at the beginning of any of the two sequences. Now start moving forward.
At each intersection point, you have the choice of either continuing with the same sequence you’re currently on, or switching to the other sequence.

The objective is ﬁnding a path that produces the maximum sum of data you walked over. In the above example, the largest possible sum is 450, which is the result of adding 3, 5, 7, 9, 20, 25, 44, 47, 55, 56, 57, 60, and 62

### Input

We are given two lists of the format

> n v<sub>1</sub> v<sub>2</sub> ... v<sub>n</sub>

where n is the length of the sequence, v<sub>i</sub> is the i<sup>th</sup> element of the sequence.

> n <= 10000
>
> -10000 < v<sub>i</sub> < 10000

`0` indicates the end of input

### Output

Largest possible sum that can be produced by the path by traversing according to the given conditions

### Conditions

We can traverse the sequence in the following manner:

- We may start at the beginning of any of the two sequences.
- At each intersection point, we have the choice of either continuing with the same sequence, or switching to the other sequence.

---

## Algorithm

### Simple Approach

- **Step 1**: Set sum1 & sum2 to be 0.

- **Step 2**: Compare the values at the first index of both lists. Whichever is lesser, add its value to the appropriate sum variable and increment its index. Repeat this step until both the values are equal.

- **Step 3**: When they are equal, then find the maximum among sum1 & sum2 and assign that value to both of them. Then increment the index of both the lists.

- **Step 4**: When the index of either one of the list is exhausted, add the remaining values in the other list to its appropriate sum variable.

- **Step 5**: Return the maximum of sum1 & sum2

### Greedy Approach

- **Step 1**: We generate the _prefix sum lists_ of the given two sequences.

- **Step 2**: We find the point of intersection of both lists. To do this we iterate through every element in a sequence and then perform a _binary search_ for the intersection on the second sequence.

- **Step 3**: On finding an intersection we find the difference between the prefix sum at the current intersection and prefix sum at previous intersection for the respective sequences and then greedily select the maximum among both and add it to a _result_ variable.

- **Step 4**: Since we have found the maximum till the final intersection, we now need to find the difference between the final element of prefix sum list and the final intersection for the respective sequences and then greedily select the maximum and add it to the _result_ variable

---

## Pseudocode

### Simple Approach

```
DoubleHelix(A,B,m,n)
  sum1 = 0
  sum2 = 0
  i=0
  j=0
  while i<m and j<n
    if A[i]<B[j]
      sum1+=A[i++]
    else if A[i]>B[j]
      sum2+=B[j++]
    else
      sum1+=A[i]
      sum2+=B[j]
      sum1=sum2=max(sum1,sum2)
      i++,j++
  while i<m
    sum1+=A[i++]
  while j<n
    sum2+B[j++]
  return max(sum1,sum2)
```

### Greedy Approach

```
DoubleHelix(A,B,m,n)
  result, i, flag =0
  prevIndA, prevIndB = 0
  prefixA, prefixB
  
  for i in range(A)
    bs = binary_search(A[i]
    
    if(bs != -1):      
      if (flag == 0):
        flag = 1
        result += max(prefixA[i], prefixB[bs])
      else:
        result += max(prefixA[i]-prefixA[prevIndA]     
                     ,prefixB[bs]-prefixB[prevIndb])

      prevIndA = i
      prevIndB = bs
  
  if (flag = 0):
    result += max(pa1[-1], pa2[-1])
  else:
    result += max(prefixA[-1]-prefixA[prevIndA]     
                 ,prefixB[-1]-prefixB[prevIndb])
```
  
---

## Proof of Correctness

### Simple Approach

Let's assume _m_ be the length of list 1, _a_<sub>i</sub> be an element of sequence 1, _n_ be the length of list 2 , _b_<sub>i</sub> be an element of sequence 2.

We have to prove that by using the following algoritm we get the maximum sum.

Since the elements in both the lists are ordered in non-decreasing order, we can predict where the elements from both the lists will attain equality i.e. intersection points.

- When _a_<sub>i</sub> < _b_<sub>i</sub>: This implies that _a_<sub>i</sub> must increase to become equal to _b_<sub>i</sub>. Thus we add _a_<sub>i</sub> to sum1 because it is on the path to the next intersection point and traverse to the next element in the first list.

- When _a_<sub>i</sub> > _b_<sub>i</sub>: This implies that _b_<sub>i</sub> must increase to become equal to _a_<sub>i</sub>. Thus we add _b_<sub>i</sub> to sum2 because it is on the path to the next intersection point and traverse to the next element in the second list.

- When _a_<sub>i</sub> = _b_<sub>i</sub>: It is an intersection point. Thus we need to compare and find the maximum of the sum variables in order to maximize the sum.

Hence, we have succesfully proved that the path taken by this method gives the maximum sum.

### Greedy Approach

Let's assume _m_ be the size of list 1, _a_<sub>i</sub> be an element of sequence 1 and _pa_<sub>i</sub> be the difference between prefix sum at index _i_ and prefix sum at previous point of intersection(which is initially 0), _n_ be the length of list 2 , _b_<sub>i</sub> be an element of sequence 2 and _pb_<sub>i</sub> be the difference between prefix sum at index _i_ and prefix sum at previous point of intersection(which is initially 0)

We have to prove that by using the following greedy algoritm we get the maximum sum.

**Base Case:** We need to show that we get a maximum sum when we have two sequences of length 1.

Since the length is 1, there can be two cases, either a<sub>1</sub> and b<sub>1</sub> same or they aren't same. If a<sub>1</sub> and b<sub>1</sub> are same then the _binary search_ determines that there is a point of intersection and then adds as max(a<sub>1</sub>, b<sub>1</sub>) which are the same at index 1 to the _result_ variable. Then according to _step 4_, the difference generated will be 0 for both the sequences. Hence there won't be any change in result. Therefore we get the maximum in this case. The second case when both are not equal, then we directly go to _step 4_ and accordingly maximum is choosen from both the sequences from max(pa<sub>1</sub>, pb<sub>1</sub>) which is equivalent to max(a<sub>1</sub>, b<sub>1</sub>). Hence the given proposition is true for n = 1 as we get the maximum sum from this single node path.

**Induction Step over i:** Assuming that our proposition holds true for sequences of length i, 1 respectively, we need to show that it is also true for i+1, 1.

This means that till i there can be two cases, either intersection occurs or intersection doesn't occur.

- Case 1: Intersection doesn't occur till i

We know that we have maximum sum till the element at index i(assumption). Let this maximum sum(which is max(pa<sub>i</sub>, pb<sub>1</sub>)) be m1. Now at index i+1 there might or might not be be an intersection. If element at i+1 and b<sub>1</sub> intersect then we can tell that we get a maximum sum m1 + max(a<sub>i+1</sub>, b<sub>1</sub>), as they are identified by the binary search and then added to the result variable. Similar is the case when they don't intersect. Then we directly go to step 4 where we find max(pa<sub>i+1</sub>, pb<sub>1</sub>) which would obviously give us the maximum sum as the given sequence to us is strictly increasing.

- Case 2: If intersection has occured at i or before i.

Since the given sequence is strictly increasing, and intersection has already occured at index i, it means that intersection will never occur at index i+1. Which implies that the maximum would be the prefix sum at index i+1. We have to prove that our algorithm gives that value.

At intersection index k our algorithm chooses max(pa<sub>k</sub>, 1) in step 3. Hence, the answer generated will be pa<sub>k</sub>. Now after completing to step 4 we will have the result as Prefix Sum till i, since size of i > 1 which obviously is the maximum. Similar is the case when an additional element is added. It will be added in step 4. Since Prefix Sum till i + a<sub>i+1</sub> is Prefix Sum till i+1. Hence the answer is Prefix Sum till i+1<sup>th</sup> element, which is greater than b<sub>1</sub> as intersection already occurred.

Basic logic behind reasoning in above case is a+b > a, given b > 0.

Hence proved.

Without loss of generality, we can also prove for induction over j.

Hence by induction, we have succesfully proved that the path taken by this method gives the maximum sum.

---

## Complexity

### Simple Approach

- **Time Complexity**: `O(m+n)` where `m` is the length of first sequence and `n` is the length of second sequence. This is because the worst case for this algorithm occurs when there are no intersection points and thus each element in both lists will be added to the sum variables.
- **Space Complexity**: `O(1)`

### Greedy Approach

- **Time Complexity**: `O(m*log(n))` where `m` is the length of first sequence and `n` is the length of second sequence, as the worst case will occur when the binary search cannot find an intersection and, cost of each binary search is O(logn) which is iterated m times.

- **Space Complexity**: `O(1)`

---

## Other Details

### Side Effects in the code

There are no side-effects in this code.

## Contributions and Bibliography

- [Multivariable Mathematical Induction](https://www.mathblog.dk/proof-method-multidimensional-induction/)



# Report - ANARC05B - The Double HeLiX

---

## Table of contents

- [Installation and Setup](#installation-and-setup)
    - [Installation](#installation)
    - [Run](#run)
- [Problem Statement](#problem-statement)
    - [Input](#input)
    - [Output](#output)
    - [Conditions](#conditions)
- [Algorithm](#algorithm)
    - [Dynamic Approach](#dynamic-approach)
    - [Greedy Approach](#greedy-approach)
- [Proof of Correctness](#proof-of-correctness)
    - [Dynamic Approach](#dynamic-approach-1)
    - [Greedy Approach](#greedy-approach-1)
- [Complexity](#complexity)
    - [Dynamic Approach](#dynamic-approach-2)
    - [Greedy Approach](#greedy-approach-2)

---

## Installation and Setup

### Installation

> git clone git@github.com:khaveesh/DAA-DoubleHelix.git

### Run

Change your current working directory by going into `DAA-DoubleHelix`

> cd DAA-DoubleHelix

To run both the algorithms and all the tests

> make

To run only algorithms 

> make run

To run the tests

> make test

---

## Problem Statement

[Source](https://www.spoj.com/problems/ANARC05B/)

Two ﬁnite, strictly increasing, integer sequences are given. Any common integer between the two sequences constitute an intersection point. Take for example the following two sequences where intersection points are printed in bold:

First= 3 5 **7** 9 20 **25** 30 40 **55** 56 **57** 60 62

Second= 1 4 **7** 11 14 **25** 44 47 **55** **57** 100

You can *walk* over these two sequences in the following way:

You may start at the beginning of any of the two sequences. Now start moving forward.
At each intersection point, you have the choice of either continuing with the same sequence you’re currently on, or switching to the other sequence.

The objective is ﬁnding a path that produces the maximum sum of data you walked over. In the above example, the largest possible sum is 450, which is the result of adding 3, 5, 7, 9, 20, 25, 44, 47, 55, 56, 57, 60, and 62

### Input 

We are given two lists of the format

> n v<sub>1</sub> v<sub>2</sub> ... v<sub>n</sub>

where n is the length of the sequence, v<sub>i</sub> is the i<sup>th</sup> element of the sequence. 

> n <= 10000

> -10000 < v<sub>i</sub> < 10000

`0` indicates the end of input

### Output 

Largest possible sum that can be produced by the path by traversing according to the given conditions

### Conditions 

We can traverse the sequence in the following manner 
- We may start at the beginning of any of the two sequences.
- At each intersection point, we have the choice of either continuing with the same sequence, or switching to the other sequence.

---

## Algorithm

### Dynamic Approach

### Greedy Approach

- **Step 1**: We generate the *prefix sum lists* of the given two sequences.
- **Step 2**: We find the point of intersection of both lists. To do this we iterate through every element in a sequence and then perform a *binary search* for the intersection on the second sequence.
- **Step 3**: On finding an intersection we find the difference between the prefix sum at the current intersection and prefix sum at previous intersection for the respective sequences and then greedily select the maximum among both and add it to a *result* variable.
- **Step 4**: Since we have found the maximum till the final intersection, we now need to find the difference between the final element of prefix sum list and the final intersection for the respective sequences and then greedily select the maximum and add it to the *result* variable

---

## Proof of Correctness

### Dynamic Approach

### Greedy Approach

Let's assume *m* be the size of list 1, *a*<sub>i</sub> be an element of sequence 1 and *pa*<sub>i</sub> be the difference between prefix sum at index *i* and prefix sum at previous point of intersection(which is initially 0), *n* be the length of list 2 , *b*<sub>i</sub> be an element of sequence 2 and *pb*<sub>i</sub> be the difference between prefix sum at index *i* and prefix sum at previous point of intersection(which is initially 0)

We have to prove that by using the following greedy algoritm we get the maximum sum.

**Base Case:** We need to show that we get a maximum sum when we have two sequences of length 1. 
            
Since the length is 1, there can be two cases, either a<sub>1</sub> and b<sub>1</sub> same or they aren't same. If a<sub>1</sub> and b<sub>1</sub> are same then the *binary search* determines that there is a point of intersection and then adds as `max(`a<sub>1</sub>, b<sub>1</sub>`)` which are the same at index 1 to the *result* variable. Then according to *step 4*, the difference generated will be 0 for both the sequences. Hence there won't be any change in result. Therefore we get the maximum in this case. The second case when both are not equal, then we directly go to *step 4* and accordingly maximum is choosen from both the sequences from `max(`pa<sub>1</sub>, pb<sub>1</sub>`)` which is equivalent to `max(`a<sub>1</sub>, b<sub>1</sub>`)`. Hence the given proposition is true for n = 1 as we get the maximum sum from this single node path.

**Induction Step over i:** Assuming that our proposition holds true for sequences of length i, 1 respectively, we need to show that it is also true for i+1, 1. 

This means that till `i` there can be two cases, either intersection occurs or intersection doesn't occur.

- Case 1: Intersection doesn't occur till `i`

We know that we have maximum sum till the element at index `i`(assumption). Let this maximum sum(which is `max(`pa<sub>i</sub>, pb<sub>1</sub>)) be `m1`. Now at index `i+1` there might or might not be be an intersection. If element at i+1 and b<sub>1</sub> intersect then we can tell that we get a maximum sum `m1 + max(`a<sub>i+1</sub>, b<sub>1</sub>`)`, as they are identified by the binary search and then added to the `result` variable. Similar is the case when they don't intersect. Then we directly go to step 4 where we find `max(`pa<sub>i+1</sub>, pb<sub>1</sub>`)` which would obviously give us the maximum sum as the given sequence to us is strictly increasing.

- Case 2: If intersection has occured at `i` or before `i`.

Since the given sequence is strictly increasing, and intersection has already occured at index `i`, it means that intersection will never occur at index `i+1`. Which implies that the maximum would be the prefix sum at index `i+1`. We have to prove that our algorithm gives that value. 

At intersection index `k` our algorithm chooses `max(`pa<sub>k</sub>, 1`)` in `step 3`. Hence, the answer generated will be `pa`<sub>k</sub>. Now after completing to step 4 we will have the result as Prefix Sum till `i`, since size of i > 1 which obviously is the maximum. Similar is the case when an additional element is added. It will be added in step 4. Since Prefix Sum till `i` + a<sub>i+1</sub> is Prefix Sum till `i+1`. Hence the answer is Prefix Sum till `i+1`<sup>th</sup> element, which is greater than b<sub>1</sub> as intersection already occurred.

Basic logic behind reasoning in above case is a+b > a, given b > 0.

Hence proved. 

Without loss of generality, we can also prove for induction over j. 

Hence by induction, we have succesfully proved that the path taken by this method gives the maximum sum.

---

## Complexity 

### Dynamic Approach

### Greedy Approach

`O(mlog(n))` where `m` is the length of first sequence and `n` is the length of second sequence.	

---

## Other Details

### Side Effects in the code


---

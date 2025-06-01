# 1.1 Induction Exercises
Section 1.1 introduces the Well-Ordered Axiom and the principle of mathmematical induction.  The exercises for section 1.1 are a set of induction proofs.

## Exercises 1.1

### 1. Does every every subset of the negative integers have a smallest element?

**No**, since a subset of the negative integers need not be finite.  For example, suppose $S$ is the even negative integers.  There is no "least negative even integer."  Consider any $n \in S$, $n-2$ is also a negative even integer, and $n-2 < n$. 

However, we can use the _Well-Ordering Axiom_ to prove that any non-empty subset of negative integers has a _greatest_ element.

> **PROOF: Every non-empty subset of the negative integers has a greatest element.**
> 
> Let $S$ be a non-empty subset of the negative integers ( $ S \neq \emptyset$ ).
> 
> Let $S'$ be the set obtained by multiplying each element of $S$ by $-1$.  
> 
> By the _**Well-Ordering Axiom**_, $S'$ contains a least element.  Let's call that element, $n'$.  Thus,
> 
> $$
  n' \le k', \quad \forall \ k' \in S'
> $$
> 
> But, multiplying each side of that inequality by $-1$  means that
> 
> $$
  n \ge k, \quad \forall  \ k \in S 
> $$
> 
> and so, $n$ is the greatest element in $S$.

<br><br>

### 2. Prove $1+3+5+...+(2n-1) = n^2$ for all integers $n \ge 1$.

We want to prove that the sum of the first $k$ odd positive integers is $k^2$.  Let $S(k)$ be defined as

$$
S(k): \ 1+3+5+...+(2k-1) = k^2
$$

Then, the base case, $S(1)$ is 

$$
S(1): \ 1 = 1^2
$$

which is true.  So, moving on to the induction step, assuming $S(k)$ is true for some $k \ge 1$, we will show that $S(k+1)$ is also true.

$$
\begin{aligned}
S(k+1): \ 1+3+5+...+(2k-1)+(2k+1) &= S(k) + (2k+1) \\
 &= k^2 + 2k + 1 \\
 &= (k+1)^2
\end{aligned}
$$


So, $S(k)$ is true for positive integers $k$,  $k \ge 1$.

<br><br>

### 3. Prove $1^2+3^2+5^2+...+(2n-1)^2 = \frac{n(4n^2-1)}{3}$ for all integers $n \ge 1$.

We want to prove the sum of the squares of the first $n$ integers is $\frac{n(4n^2-1)}{3}$ for all $n \ge 1$.  The general statement, $S(k)$ is

$$
S(k): \ 1^2+3^2+5^2+...+(2k-1)^2 = \frac{k(4k^2-1)}{3}
$$

The base case, $S(1)$ is

$$
\begin{aligned}
S(1): \ 1^2 &= \frac{1(4 (1)^2-1)}{3} \\
 &= \frac{3}{3} \\
 &= 1
\end{aligned}
$$

So, the base case is true.

We're left to show that $S(k+1)$ is true assuming that $S(k)$ is true.

$$
\begin{aligned}
 1^2+3^2+5^2+...+(2k-1)^2+(2k+1)^2 &= S(k) + (2k+1)^2 \\
 &= \frac{k(4k^2-1)}{3} + (2k+1)^2 \\
 &= \frac{4k^3-k}{3} + \frac{3(4k^2+4k+1)}{3} \\
 &= \frac{4k^3 - k +12k^2 +12k + 3 }{3} \\
 &= \frac{4k^3 + 12k^2 +11k + 3 }{3} \\
 &= \frac{(k+1)(4k^2 +8k + 3)}{3} \\
 &= \frac{(k+1)(4k^2 +8k + 4 - 1 )}{3} \\
 &= \frac{(k+1)(4(k+1)^2 -1 )}{3} \\
 &= S(k+1)
\end{aligned}
$$


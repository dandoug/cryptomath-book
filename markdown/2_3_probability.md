# 2.3 Probability

## Exercises 2.3

### 1. A ball is selected at random from a box containing 4 green, 6 blue, 3 yellow, and 7 red balls. Find the probability that

There are 20 balls in total.

#### (a) a blue ball is selected.
$p(\text{blue ball selected}) = \frac{6}{20} = 0.3$

#### (b) a yellow ball is selected.
$p(\text{yellow ball selected}) = \frac{3}{20} = 0.15$

#### (c) a red ball is not selected.
$p(\text{red ball not selected}) = \frac{13}{20} = 0.65$

#### (d) either a yellow or blue ball is selected.
Since a ball cannot be both yellow **and** blue, this is just the sum
$p(\text{blue ball selected}) + p(\text{yellow ball selected}) = \frac{6}{20} + \frac{3}{20} = 0.45$

#### (e) neither a green nor a red ball is selected.
Since this implies that a yellow or blue ball is selected this is also $0.45$.

#### (f) a green, blue, or yellow ball is selected.
This is same as a red ball not being selected, as computed above, $0.65$


### 2. From a group of 85 spies, one will be selected at random to be stationed in Honolulu. If 48 are female and 64 are single, and if among the 64 single spies, half are male, what is the probability that the spy selected will be neither single nor female?

From the text, assuming a spy is either male or female and assuming that a spy is either married or single.

* $48$ are female
* $64$ are single
* $32$ are single females
* $32$ are single males
* $85 - 48 = 37$ are male
* $37 - 32 = 5$ are married males
* $48 - 32 = 16$ are married females

Let $E$ be the event that _"spy selected will be neither single nor female"_, this is the same as _"selected spy is a married male"_.
$$
 p(E) = \frac{n(E)}{n(S)} = \frac{5}{85} \approx 0.0588
$$

### 3. Four cards are to be drawn simultaneously from a deck of 52. Find the probability that

The size of the sample set, $S$ is $n(S) = C(52, 4) = 270725$
#### (a) all four are clubs.
Let $E$ be _"all four are clubs"_, then $p(E) = \frac{n(E)}{n(S)} = \frac{C(13, 4)}{C(52, 4)} = \frac{715}{270725} \approx 0.00264$ 

#### (b) at least one is not a club.
This is $1 - p(E) = 1 - \frac{715}{270725} = \frac{270010}{270725} \approx 0.997$

#### (e) three are black and one is red
There are $C(26, 3)$ ways of picking three black cards and $C(26, 1)$ ways of picking one red, so if $E$ is _"three are black and one is red"_, then
$$
 n(E) = C(26, 3) \cdot C(26, 1) = 2600 \cdot 26 = 67600
$$
and 
$$
 p(E) = \frac{n(E)}{n(S)} = \frac{67600}{270725} \approx 0.2497
$$

#### (d) exactly two are picture cards.
"Picture cards" are jack, queen, or king.  Three per suit, four suits so $12$ picture cards total.

* The number of ways of choosing 2 picture cards is $C(12, 2) = 66$
* The number of ways of choosing 2 non-picture cards is $C(52-12, 2) = C(40, 2) = 780$
* The number of ways of choosing 4 cards with exactly 2 being picture cards is $66 \times 780 = 51480$
* The probability of drawing that hand is $\frac{51480}{270725} \approx 0.190$

#### (e) either two or three of the four cards are picture cards.

This is the sum of the probabilities of exactly two are picture cards and exactly three are picture cards.  We computed the first above, so let's focus on computing the probability of "exactly three are picture cards"

* The number of ways of choosing 3 picture cards is $C(12, 3) = 220$
* The number of ways of choosing 1 non-picture card is $C(52-12, 1) = C(40, 1) = 40$
* The number of ways of choosing 4 cards with exactly 3 being picture cards is $220 \times 40 = 8800$
* The probability of drawing that hand is $\frac{8800}{270725} \approx 0.0325$

So, the probability of getting two or three picture cards is

$$
  \frac{51480}{270725} + \frac{8800}{270725} = \frac{51480 + 8800}{270725} = \frac{60280}{270725} \approx  0.2227
$$

### 4. The probability for various numbers of spies being deployed to the San Fernando Valley is summarized in the following table:

| Number of spies to be deployed |   0    |   1    |   2    |   3    |  4 or more  |
|--------------------------------|:------:|:------:|:------:|:------:|:-----------:|
| Probability                    |  0.24  |  0.20  |  0.35  |  0.11  |    0.10     |

Find the probability that
#### (a) at most two spies will be deployed.
So, this is deploying 0, 1, or 2 and the probability is
$$
  0.24 + 0.20 + 0.35 = 0.79
$$

#### (b) at least one spy will be deployed.
This is $1 - p(\text{0 spies deployed})$
$$
  1 - 0.24 = 0.76
$$

#### (e) one or two spies will be deployed.
$$
 0.20 + 0.35 = 0.55
$$

#### (d) fewer than four spies will be deployed.
$$
 1 - 0.10 = 0.9
$$

### 5. A couple has 3 children. Assuming that the probability of any child's being a girl is 0.5, find the probability that
#### (a) the oldest child is a boy.
Since the probability of any single child being a boy (or a girl) is $0.5$, the answer is $0.5$.

#### (b) there are at least two girls.
All the outcomes are equiprobable, so computing the weights is just counting the sample space and the events.
There are $2^3 = 8$ different permutations of the children. That is $n(S)$.  The event, $E$, is equivalent to there being $0$ or $1$ boys.  There is $1$ way for there to be zero boys and there are $3$ ways for there to be exactly one boy, so $n(E)$ is $4$.  Therefore, the probability of there being at least two girls is

$$
\begin{aligned}
 \frac{n(E)}{n(S)} &= \frac{4}{8} \\
                   &= 0.5
\end{aligned}
$$

#### (e) no more than one child is a boy.
As computed above, this is $0.5$

#### (d) the oldest and youngest are girls and the middle child is not.
This is a single outcome of the sample space, ***GBG***, since we computed the $n(S) = 8$, the probably that the oldest and youngest are girls and the middle child is not (i.e. is a boy) is $\frac{1}{8} = 0.125$.

#### (e) exactly one of the three children is a boy.
There are three ways for this to happen: ***BGG***, ***GBG***, or ***GGB***.  So its probably is $\frac{3}{8} = 0.375$.

### 6. Three men and two women are seated in the same row of seats in a theater. If the seats were selected at random, find the probability that the seating arrangement alternates by sex.
Assuming that we just consider five seats in a single row, there are five seats in the row, there is only $1$ way to arrange the men (***M***) and women (***W***) so that they alternate by sex, ***MWMWM***.  One way to count the total number of arrangements is to consider the seats as being numbered from 1 to 5 and choosing the two that will be occupied by the women.  This is $C(5, 2) = 10$  So, the probability that the men and women will be seated alternating by sex is $\frac{1}{10} = 0.1$.

### 7. Of 24 runners competing in a marathon, 3 have taken banned performance-enhancing drugs. Six of the athletes are selected at random for drug testing. What is the probability that
There are $C(24, 6) = 134596$ ways of randomly choosing the six for testing.  This is $n(S)$.

#### (a) none of the drug takers get caught?
Let $E$ be the event, **_none of the drug takers get caught_**.  The event $\sim\!E$ is the event that **_at least one of the drug takers gets caught_**.  We can think of each runner as being a ball labeled 1 through 24 and arbitrarily let balls 1, 2, and 3 represent the drug-takers.  Then, $p(\sim\!E)$ is the probability of choosing 6 balls randomly from the bag and having 1, 2, or 3 of them be less than 4.

* There are $C(3, 1) \cdot C(21, 5) = 3 \times 20349 = 61047$ ways for exactly one ball to be less than 4.
* There are $C(3, 2) \cdot C(21, 4) = 3 \times 5985 = 17955$ ways for exactly two balls to be less than 4.
* There are $C(3, 3) \cdot C(21, 3) = 1 \times 1330 = 1330$ ways for exactly three balls to be less than 4.

So, $n(\sim\!E) = C(3, 1) \cdot C(21, 5) + C(3, 2) \cdot C(21, 4) + C(3, 2) \cdot C(21, 4) = 61047 + 17955 + 1330 = 80332$

and 

$$
 p(\sim\!E) = \frac{n(\sim\!E)}{n(S)} = \frac{80332}{134596} \approx 0.597
$$

We know that 

$$
\begin{aligned}
 p(E) &= 1 - p(\sim\!E) \\
      &= \frac{134596}{134596} - \frac{80332}{134596} \\
      &= \frac{134596 - 80332}{134596} \\
      &= \frac{54264}{134596} \\
      &\approx 0.403
\end{aligned}
$$

#### (b) at least one gets caught?
As computed above, this is 

$$
 p(\sim\!E) = \frac{n(\sim\!E)}{n(S)} = \frac{80332}{134596} \approx 0.597
$$

#### (c) all three get caught?
Let $F$ be the event **_all three get caught_**.  $n(F)$ is equivalent to number of ways of getting exactly 3 of the six chosen balls to be less than 4.  This is

$$
 C(3, 3) \cdot C(21, 3) = 1 \times 1330 = 1330
$$

So, $p(F) = \frac{n(F)}{n(S)} = \frac{1330}{134596} \approx 0.00988$


### 8. A lottery consists of 48 numbers of which 8 are selected by the lottery authority. In order to win, you need to select either 7 or 8 of the numbers selected by the authority. If you pick exactly 7, you win \$20,000; if you pick 8 you win \$50,000. What is the probability you
There are $C(48, 8) = 377348994$ ways of choosing the numbers.
We assume that a single pick is a selection of 8 numbers.

#### (a) win \$50,000?
Your odds of picking all 8 correctly are $ \frac{1}{377348994} \approx  2.65e-09 = 0.00000000265$

#### (b) win \$20,000?
There are $C(8, 7) = 8$ ways of picking 7 of the 8 winning numbers.  For each of those selections, there are 40 other numbers that can round out your 8-number pick.  (There aren't 41 because one of those choices would give you 8 correct.) Therefore, the number of picks that have exactly 7 matching numbers is $8 \times 40 = 320$ and your odds of achieving this event are 

$$
 \frac{320}{377348994} \approx 8.48e-07 = 0.000000848
$$

### 9. You have a "flush" in poker when all five of the cards you are dealt are of the same suit. What is the probability of the following.
Assume the deck has 52 cards.  The sample set, $S$, of all 5-card hands you could be dealt has size $n(S) = C(52, 5) = 2598960$

#### (a) being dealt a flush in spades?
There are $C(13, 5) = 1287$ ways to deal a flush in spades (or any other particular suit), so the odds are

$$
 \frac{1287}{2598960} \approx 0.000495
$$

#### (b) being dealt a flush in either spades or diamond?

$$
 \frac{C(13, 5)+C(13, 5)}{C(52, 5)} = \frac{1287 + 1287}{2598960} = \frac{2574}{2598960} \approx 0.000990
$$

#### (e) being dealt a flush in any suit?
This is twice the probability of the previous answer

$$
 \frac{1287 + 1287 + 1287 + 1287}{2598960} = \frac{5148}{2598960} \approx 0.00198
$$

#### (d) not being dealt a flush?
This is

$$
 1 - \frac{1287 + 1287 + 1287 + 1287}{2598960} = \frac{2593812}{2598960} \approx 0.998
$$

### 10. Three spies, A, B, and C are in the running for an assignment in Afghanistan. A is twice as likely to be selected as B, and C is three times as likely as A to be selected. What is the probability that A is selected?
The sum of the probabilities has to equal $1$, so we have

$$
  p(A) + p(B) + p(C) = 1 
$$

$$
  p(A) = 2 \cdot p(B)  
$$

$$
  p(C) = 3 \cdot p(A) 
$$

Therefore,

$$
  p(C) = 6 \cdot p(B) 
$$

and

$$
\begin{aligned}
   1 &= p(A) + p(B) + p(C) \\
     &= 2 \cdot p(B) + p(B) +  6 \cdot p(B) \\
     &= 9 \cdot p(B) \\
  p(B) &= \frac{1}{9}
\end{aligned}
$$

but since $p(A) = 2 \cdot p(B)$, we know that $p(A)$ is then $ \frac{2}{9} \approx 0.222$


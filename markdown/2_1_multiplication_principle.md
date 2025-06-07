# 2.1 The Multiplication Principle

## Exercises 2.1

### 1. Stephanie needs to get to London from Philadelphia with a quick stop in New York. She can get to New York from Philadelphia either by car, bus, or plane. She can get from New York to London either by plane or by boat. In how many different ways can she travel from Philadelphia to London? Draw a tree diagram to illustrate your answer.

There are $3$ choices for the first leg and $2$ choices for the second.  So the number of ways for Stephanie to get to London are

$$
  3 \times 2 = 6
$$

```{mermaid}
graph LR
    A["Philadelphia"] -->|Car| B["New York"]
    A -->|Bus| C["New York"]
    A -->|Plane| D["New York"]
    B -->|Plane| E["London"]
    B -->|Boat| F["London"]
    C -->|Plane| G["London"]
    C -->|Boat| H["London"]
    D -->|Plane| I["London"]
    D -->|Boat| J["London"]
```

### 2. Seven people are standing in a row in a police line up. In how many different orders can they be arranged?

$$
  7! = 5040
$$

### 3. Beth's phone number is 466-2275. She's looking for a way to remember the number mnemonically. Looking at the number pad on her phone she notices that the number 4 can be associated with any of the letters G, H, or I; the number 6 with any of the letters M, N, or O; the number 2 with either A, B. or C; and the number 5 with either J, K, or L. How many different mnemonics are possible?

There are 7 digits and each can be represented by 3 letters, so the total number of permutations is

$$
  3^7 = 2187
$$

### 4. A test contains 25 questions including 10 True-False, 10 multiple choice (each with 3 possible answers), and 5 multiple choice (each with 5 possible answers). In how many different ways can the complete test be answered? Of these, how many are completely correct?

$$
  2^{10} \cdot 3^{10} \cdot 5^{5} = 188956800000
$$

Assuming that each question only has one correct answer, then there is only $1$ correct permutation that is completely correct.

### 5. Twenty people walk, one at a time, into a room containing 25 seats arranged in rows and columns. Each person takes a seat. How many different seating orders are possible?

This boils down to the number of permutations of the $25$ people which is

$$
 25! = 15,511,210,043,330,985,984,000,000
$$

### 6. Stephanie is trying to communicate with Beth by raising some flags up a flagpole. She has five different flags and a message consists of 3 of these 5 flags raised up the pole in a certain order. How many messages are possible?

$5$ choices for the first flag, $4$ for the second and $3$ for the third

$$
 5 \times 4 \times 3 = 60
$$

$60$ possible messages.

### 7. Four people are running for Student Government Association President, 5 for Vice-President, 1 for Secretary, and 3 for Treasurer. How many different administrations are possible?

$$
  4 \times 5 \times 1 \times 3 = 60
$$

assuming that 13 candidates are unique.

### 8. Molly is trying to figure out a good password for her e-mail security. The password may consist only of upper-case letters, lower-case letters (considered to be different from upper case), and digits. The password can be between 6 and 8 characters long. How many passwords are possible? How many are possible if no character may be used more than once?

That's a character set of 

$$
  26 + 26 + 10 = 62 
$$

62 possible characters.  The password can be $6$, $7$, or $8$ possile characters.  The total number, allowing repeated characters is

$$
  62^6 + 62^7 + 62^8 = 221,918,520,426,688
$$

If no character can be repeated, the number is

$$
\begin{aligned}
 \frac{62!}{56!} +  \frac{62!}{55!} +  \frac{62!}{54!}  & = \frac{62! + 62!(56) + 62!(56 \cdot 55)}{56!} \\
 & = \frac{62!(1+56+56\cdot55)}{56!} \\
 & = \frac{62!(3137)}{56!} \\
 & = 138,848,807,594,160
\end{aligned}
$$

### 9. How many different social security numbers would be possible if there were no restrictions on the digits used? (A social security number has the format XXX-XX-XXXX where each X represents a digit.)

Nine digits in the number, so

$$
  10^9 = 1,000,000,000
$$  

### 10. Stephanie has 8 cryptology books, 12 math books, and 6 novels in her quarters. In how many ways can she arrange these books on a single shelf? In how many ways can she arrange the books if she wishes to keep the books grouped together by their subject matter?

There are $8 + 12 + 6  = 26$ books.  Arranging ignoring the subject of the book, there are 

$$
  26! = 403,291,461,126,605,635,584,000,000
$$

ways or arranging them.

If grouping by subject matter.  There are two levels of arrangement to consider, how the 3 subjects are arranged and how the books in each subject are arranged.

There are

$$
  8! \cdot 12! \cdot 6! = 13,905,608,048,640,000
$$

ways of arranging the books within their subject.  and there are $3! = 6$ was of arranging the subjects so there are

$$
  3!(8!)(12!)(6!) = 83,433,648,291,840,000
$$

ways of arranging the books within their subjects on the shelf.

### 11. Beth and Stephanie are playing Scrabble® and Beth goes first. She has seven letters on her rack and wants to lay down a 5-letter word. How many sets of 5 letters will she need to check if she wants to exhaust all of the possibilities?

$$
 \frac{7!}{2!} = \frac{5040}{2} = 2520
$$

### 12. Molly is practicing her breaking and entering technique in an abandoned house that has 3 doors and 14 windows. In how many ways can she enter and leave the house if she wants to enter through a door and leave through a door? If she wants to enter through one door and leave through another? If she wants to enter through a window and leave through a door? If she wants to enter through a window and leave through a window? If she doesn't care how she gets in or how she gets out?

* enter through a door and leave through a door

$$
 3 \times 3 = 9
$$

* enter through one door and leave through another

$$
 3 \times 2 = 6
$$

*  enter through a window and leave through a door

$$
 14 \times 3 = 42
$$

* enter through a window and leave through a window

$$
 14 \times 14 = 196
$$

* doesn't care how she gets in or how she gets out

$$
 17 \times 17 = 289
$$

### 13. Molly intercepts a message that she knows to have been enciphered using an affine scheme. If she's unlucky, how many possible sets of keys (multiplicative and additive) might she need to check before she hits upon the right pair?

There are $26$ possible additive keys and only 12 possible multiplicative keys

$$
 \{1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25\}
$$

So that means there are $26 \times 12 = 312$ possible affine schemes.
 
# 2.4 Independent Events and Expected Number

## Exercises 2.4

### 1. An experiment consists in selecting a card from a deck of 52. If this experiment is repeated 1000 times, what is the expected number of

#### (a) aces?

$$
 p(\text{selecting ace}) = \frac{4}{52} = \frac{1}{13}
$$

So $EN = \frac{1}{13}(1000) \approx 76.923$

#### (b) picture cards?
Assuming that's jack, queen, king                                

$$
  p(\text{selecting picture card}) = \frac{12}{52} = \frac{3}{13}  
$$

So $EN = \frac{3}{13}(1000) \approx 230.769$   

#### (c) 5s or 6s?

$$
  p(\text{selecting 5 pr 6}) = \frac{8}{52} = \frac{2}{13}
$$

So $EN =  \frac{2}{13}(1000) \approx 153.846$  

### 2. A card is selected from a deck of 52 and then re-inserted into the deck. A second card is then selected from the deck of 52. Let $E$ be the event "the first card is a Jack" and let $F$ be the event "the second card is a Queen." Are $E$ and $F$ independent events? Compute $p(E \cap F)$.

$$
 p(E) = \frac{4}{36} = \frac{1}{13}
$$

and

$$
 p(F) = \frac{4}{36} = \frac{1}{13} 
$$

Note the the sample set here is $52^2 = 2704$ and there are $16$ outcomes that match the criteria.  So 

$$                                        
 p(E \cap F) = \frac{16}{2704} = \frac{1}{169}      
$$    

This is exactly the same as $p(E)p(F)$ so $E$ and $F$ are independent.

### 3. In a survey of 1000 people categorized as smokers or nonsmokers, with or without respiratory problems, the following data were obtained:

|                  | Respiratory Problem ($R$) | No Respiratory Problem ($\sim\!R$) |
|------------------|:-------------------------:|:-----------------------------:|
| Smokers ($S$)    |            520            |              180              |
| Nonsmokers ($\sim\!S$) |            77             |              223              |

Based on this data determine whether the following pairs of events are independent:

$$
 n(\text{sample set}) = 1000
$$      

|           | Probability |
|:---------:|:-----------:|
|    $S$    |   $.700$    |
| $\sim\!S$ |   $.300$    |   
|    $R$    |   $.597$    |   
|    $\sim\!R$    |   $.403$    |   

#### (a) S and R
$p(S \cap R) = .520 \ne (.700)(.597)$ so *not* independent

#### (b) S and ~R
$p(S \, \cap \sim\!R) = .180 \ne (.700)(.403)$ so *not* independent   
                                                             
#### (c) ~S and R
$p(\sim\!S \cap R) = .077 \ne (.300)(.597)$ so *not* independent   
                                                             
#### (d) ~S and ~R
$p(\sim\!S \, \cap \sim\!R) = .223 \ne (.300)(.403)$ so *not* independent   
                                                             
#### (e) S and ~S
$p(S \, \cap \sim\!S) = .000 \ne (.700)(.300)$ so *not* independent   
                                                             
#### (f) R and ~R
$p(R \, \cap \sim\!R) = .000 \ne (.597)(.403)$ so *not* independent   
                                                             
### 4. Suppose that in a certain language, the probability of two characters selected at random from a text being the same is 0.03. If a document in this language contains 5713 characters,
#### (a) How many pairs of letters (without regard to order) can be selected?
$C(5713, 2) = 16316328$

#### (b) Of these, how many would you expect to have both letters being the same?
$ EN = (.03)(16316328) = 489489.84 $

The following problems refer to an experiment that consists of tossing two
dice, one with bold font and one with italicized font. The sample space for this
experiment is

 S = ( <br/>
   (**1**, _1_), (**1**, _2_), (**1**, _3_), (**1**, _4_), (**1**, _5_), (**1**, _6_),  <br/>
   (**2**, _1_), (**2**, _2_), (**2**, _3_), (**2**, _4_), (**2**, _5_), (**2**, _6_),  <br/>
   (**3**, _1_), (**3**, _2_), (**3**, _3_), (**3**, _4_), (**3**, _5_), (**3**, _6_),  <br/>
   (**4**, _1_), (**4**, _2_), (**4**, _3_), (**4**, _4_), (**4**, _5_), (**4**, _6_),  <br/>
   (**5**, _1_), (**5**, _2_), (**5**, _3_), (**5**, _4_), (**5**, _5_), (**5**, _6_),  <br/>
   (**6**, _1_), (**6**, _2_), (**6**, _3_), (**6**, _4_), (**6**, _5_), (**6**, _6_)   <br/>
 ). <br/>

### 5. Find the probability that
Notice that the total number of outcomes in $S$ is $36$ and that outcomes on the left-to-right-sloping-up diagonals add up to the same numbrer.  For the probability calcultions below, it is sufficient to count the number of outcomes that produce the given sum and divide by $36$.

#### (a) the sum of the dice is 2
$ \frac{1}{36} $

#### (b) the sum of the dice is 3.
$ \frac{2}{36} = \frac{1}{18}  $

#### (c) the sum of the dice is 4.
$ \frac{3}{36} = \frac{1}{12}  $

#### (d) the sum of the dice is 5.
$ \frac{4}{36} = \frac{1}{9}  $

#### (e) the sum of the dice is 6.
$ \frac{5}{36} $

#### (f) the sum of the dice is 7.
$ \frac{6}{36} = \frac{1}{6}  $

#### (g) the sum of the dice is 8.
$ \frac{5}{36} $

#### (h) the sum of the dice is 9.
$ \frac{4}{36} = \frac{1}{9}  $

#### (i) the sum of the dice is 10.
$ \frac{3}{36} = \frac{1}{12}  $

#### (j) the sum of the dice is 11.
$ \frac{2}{36} = \frac{1}{18}  $

#### (k) the sum of the dice is 12.
$ \frac{1}{36} $

#### (l) the sum of the dice is 13.
$ \frac{0}{36} = 0 $


### 6. Let $E$ be the event "the italicized die turns up 5" and $F$ the event "the bold die turns up 3." Are $E$ and $F$ independent?
yes, because $p(E) = \frac{1}{6}$ and $p(F) = \frac{1}{6}$ and $p(E \cap F) = \frac{1}{36} = p(E)p(F)$ 

### 7. Let $E$ be the event "the sum of the dice is even" and let $F$ be the event "the sum of the dice is greater than 8." Are $E$ and $F$ independent?

$$
 p(E) = \frac{18}{36} = \frac{1}{2}
$$

and

$$
 p(F) = \frac{10}{36} = \frac{5}{18} 
$$

and

$$                                        
 p(E \cap F) = \frac{4}{36} = \frac{1}{9}      
$$                                      

Note that $p(E)p(F) \ne p(E \cap F)$ so $E$ and $F$ are *not* independent.

### 8. Let $E$ be the event "the face of the italicized die is greater than or equal to the face of the bold die" and let $F$ be the event "the sum of the faces is 11 or 12." Are $E$ and $F$ independent?

$$
 p(E) = \frac{21}{36} = \frac{7}{12}   
$$

$$
 p(F) = \frac{3}{36} = \frac{1}{12}
$$

$$
 p(E \cap F) = \frac{2}{36} = \frac{1}{18}      
$$

Note that $p(E)p(F) \ne p(E \cap F)$ so $E$ and $F$ are *not* independent.    

### 9. If the pair of dice is thrown 500 times, what is the expected number of 7s
Using the probability computed above

$$
  EN = \frac{1}{6}(500) \approx 83.33
$$

### 10. If the pair of dice is thrown 36 times, what is the expected number of 11s?

$$
  EN =  \frac{1}{18}(36) = 2
$$
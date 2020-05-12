* now it took me about 4 h for the 4% I'm through. I'm at line 66 now of MS-reddit.


* From the files in `data`, extract `portal_url` (which serves as ID) and `text_raw`.
* in Numbers, mark all, right click and select `wrap text`. Also, alternating row colours helps.
* Find offsets using [this page](https://mothereff.in/byte-counter). 

ANNOTATION   
* spans (if discontinuous it's A,B;C,D;...)
* confidence (see below)
* about (if multiple apply, it's comma-separated: `patient,speaker`)
  * speaker (= author of post, sometimes they interview people and then the AM's are not annotated as speaker even though they say 'I was about 16')
  * patient (means person who has the disease, or any other disease)
  * nothing: eg: The **mother** of a boy with AS...

CONFIDENCE
* confidence 3: precise age mention (within 1 year)
   * age X, X month, age X/M
   * X y.o., Xyo
   * within the first year of life
   * when I was born
   * I was X (spelled out)
   * X birthday, my Xth, just turned X, I am turning X
   * embryo, fetal
   * in utero
   * prenatal
   * (Xmf), (Xyo male)
   * I am XF (but not 'like I was 15 yo again')
   * newborn babies
   * I was X
   * often as 'm29', or '29m'

* confidence 2: age group
   * right before my Xnd bday
   * in their Xs, in her late Xs
   * mid Xs
   * ~50
   * as early as
   * post X
   * underage
   * almost X yo
   * child of this generation
   * under X, not even X yrs old
   * early age, early life, older children
   * childhood, early teen, teenager, early childhood
   * between X and Y years of age
   * baby, newborn x, fetus
      * if affectionately, annotated with confidence 1
   * child, children, kids (but not 'only child'), kid, little kid (but not 'like a child') (and not if it's ficticious - thinking about having a second child)
   * pediatric X
   * X-something
   * juveniles, adolescent
   * adult
   * pre-teen
   * early postnatal
   * age out of school, a month after I graduated college, when I was in college, early college years, straight out of high-school, headed into college, entering college
   * legal adultood
   * third grade

* confidence 1: vague or infered
   * 'got years ahead of her'
   * son, daughter (could be used in a religious meaning, but was still annotated)
   * grandson, daughter-in-law, nephew
   * boy (depending on how it's used), 'my children' (as opposed to they are children, which I give 2)
   * aunt
   * mother, father, dad, parents, mama, grandma, grandfather, grandpa
   * little X, wee X
   * young woman, I'm old, younger days
   * young, elderly (but not 'too young'), greater chronological age
   * older Angel (but not 'my older sister')
   * after they graduate, about to graduate from university

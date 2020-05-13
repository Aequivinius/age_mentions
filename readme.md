### Annotation

* 3 things are annotated *per age mention*: span, confidence and about.
  * only AMs for humans and mice are labelled, not for cells ('adult oligodendrocytes')
  * spans can be discontinuous, eg `5,9;11,13`
  * confidence is either `1` (for infered or uncertain AMs), `2` for age groups and `3` if precise within 1 year
  * about is either `speaker` (the person who wrote the post) or `patient` (person who has **a** disease, not necessarily the disease in question for the dataset). Can be also both or nothing (if it's about somebody the doctor, for example). Sometimes there will be quoted speech in a post (a patient said: 'I was 16'), which is not annotated as `speaker` if 

### Patterns (Confidence 3)

* **Note**: Hypothetical ages are not annotated. 'like I was 15 yo again' or 'when I'm 40'

* (Xm), (XF), Xm, mX, X/m, (X yo male)
* age X, X month, age X/M, age X/F
* at X
* I was X, I am X, I'm X, I'm currently X
* X y.o., Xyo, X-year-old, X yo, X years old (spelling out X sometimes)
* within the first year of life
* **birthdays**: X birthday, my Xth, just turned X, I am turning X, when I was born
* **embroys**: embryo, fetal, in utero, prenatal, newborn babies, newborn x months, fetus

### Patterns (Confidence 2)

* Most often age groups; sometimes it's cases where a precise AM is made vague ('almost X')
* Again, hypothetical AMs are not annotated. 'like a child' or even 'child' that is not born ('we're thinking about having a second child')

* baby (if used affectionately, annotated with confidence 1), early postnatal
* childhood, early childhood, older children, child, children, kids (but not 'only child'), kid, little kid
* in my teens, early teen, teenager, pre-teen (watch out for 'teenie bit')
* juveniles, adolescent
* pediatric X
* underage
* early age, early life
* adult, legal adultood
* **Xs**: in their Xs, in her late Xs, mid Xs
* ~50, X-something
* between X and Y years of age
* **>/<**: post X, under X, not even X yrs old
* **Vagueing**: right before my Xnd bday, as early as, almost X yo

### Patterns (Confidence 1)

* 'got years ahead of her'
* son, daughter, grandson, daughter-in-law, nephew
* boy (depending on how it's used)
* aunt
* mother, father, dad, parents, mama, grandma, grandfather, grandpa (not 'the mother of all chest pains')
* little boy, wee girl
* young woman, I'm old, in my younger days
* young, elderly (but not 'too young'), greater chronological age
* older Angel (but not 'my older sister')
* age out of school, a month after I graduated college, when I was in college, early college years, straight out of high-school, headed into college, entering college, back to college (but not 'want to go back to school'), third grade, after they graduate, about to graduate from university
* menopause
* child of this generation

### Data Conversion

* From the files in `data`, extract `portal_url` (which serves as ID) and `text_raw`.
* in Numbers, mark all, right click and select `wrap text`. Also, alternating row colours helps.
* Find offsets using [this page](https://mothereff.in/byte-counter) for short post, or using GATE for long ones.

### Current State of Annotation

* ~1 980 000 of 5 845 816 characters in total (30%, which took me about 20h)
### Annotation

* 3 things are annotated *per age mention*: span, confidence and about.
  * only AMs for humans and mice are labelled, not for cells ('adult oligodendrocytes'); nor for diseases ('my 36 yo MS'). One case of 'adult brain', which was labeled.
  * spans can be discontinuous, eg `5,9;11,13`
  * confidence is either `1` (for infered or unspecific AMs), `2` for age groups and `3` if precise within 1 year
  * about is either `speaker` (the person who wrote the post) or `patient` (person who has **a** disease, not necessarily the disease in question for the dataset). Can be also both or nothing (if it's about somebody the doctor, for example). Sometimes there will be quoted speech in a post (a patient said: 'I was 16'), which is not annotated as `speaker` if 
* No relative age mentions where annotated (my younger brother, millenials)

### Patterns (Confidence 3)

* **Note**: Hypothetical ages are not annotated. 'like I was 15 yo again' or 'when I'm 40'

* (Xm), (XF), Xm, mX, X/m, (X yo male)
* age X, X month, age X/M, age X/F
* at X (watch out: can also be a street information, eg 'at 69, Colebroke Row'), at the age of X
* I was X, I am X, I'm X, I'm currently X, I'm only X, being X
* X y.o., Xyo, X-year-old, X yo, X years old (spelling out X sometimes), Xy/o
* of X (years)
* hitting X
* within the first year of life
* **birthdays**: X birthday, my Xth, just turned X, I am turning X, when I was born
* **embroys**: embryo, fetal, in utero, prenatal, newborn babies, newborn x months, fetus

### Patterns (Confidence 2)

* Most often age groups; sometimes it's cases where a precise AM is made vague ('almost X')
* Again, hypothetical AMs are not annotated. 'like a child' or even 'child' that is not born ('we're thinking about having a second child')

* baby (if used affectionately, annotated with confidence 1), early postnatal
* childhood (but not 'I had an awful childhood'), early childhood, older children, child, (small) children, kids (but not 'only child'), kid, little kid
* infant
* growing up
* in my teens, early teen, teenager, pre-teen (watch out for 'teenie bit')
* juveniles, adolescent, puberty
* pediatric X, pediatric-onset X
* underage
* early age, early life
* adult, legal adultood, young adult
* college-age
* **Xs**: in their Xs, in her late Xs, mid Xs, X's
* ~50, X-something
* young onset, YOPD (classified as 2 since it is defined as <50)
* between X and Y years of age
* (early) retirement, (approaching) retirement age
* **>/<**: post X, under X, not even X yrs old
* **Vagueing**: right before my Xnd bday, as early as, almost X yo

### Patterns (Confidence 1)

* 'got years ahead of her'
* son, daughter, grandson, daughter-in-law, nephew
* boy (depending on how it's used)
* aunt
* mother, father, dad, daddy, parents, mama, grandma, grandfather, grandpa (not 'the mother of all chest pains'), fatherhood
* little boy, wee girl
* young woman, I'm old, in my younger days, at a young age, elderly lady
* young, elderly (but not 'too young'), greater chronological age, not young anymore, young(ish), relatively young
* older Angel (but not 'my older sister'), younger (but not 'younger than')
* age out of school, a month after I graduated college, when I was in college, early college years, straight out of high-school, headed into college, entering college, back to college (but not 'want to go back to school'), third grade, after they graduate, about to graduate from university
* the late Muhammad Ali
* menopause
* child of this generation

* I could've annotatated 'pregnancy' or 'after my daughter', as this allows implication of age, but didn't, because I came to think of it too late.

### Data Conversion

* From the files in `data`, extract `portal_url` (which serves as ID) and `text_raw`.
* in Numbers, mark all, right click and select `wrap text`. Also, alternating row colours helps.
* Find offsets using [this page](https://mothereff.in/byte-counter) for short post, or using GATE for long ones.

### Current State of Annotation

* `wc -m manual_annotation/diseasementions/*`
* ~4 100 000 of 5 845 816 characters in total (70%, which took me about 35h)

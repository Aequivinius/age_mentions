### Annotation

* 3 things are annotated *per age mention*: span, confidence and about.
  * only AMs for humans and mice are labelled, not for cells ('adult oligodendrocytes'); nor for diseases ('my 36 yo MS'). One case of 'adult brain', which was labeled.
  * No relative age mentions where annotated (my younger brother, millenials)
  * spans can be discontinuous, eg `5,9;11,13`
  * confidence is either `1` (for infered or unspecific AMs), `2` for age groups and `3` if precise within 1 year
  * about is either `speaker` (the person who wrote the post) or `patient` (person who has **a** disease, not necessarily the disease in question for the dataset). Can be also both or nothing (if it's about somebody the doctor, for example). Sometimes there will be quoted speech in a post (a patient said: 'I was 16'), which is not annotated as `speaker` .
* Annotation was done in GATE for larger documents, using `manual_annotation_schema.xml`

### Data Set

* Total of 3128 documents where annotated (1142 from reddit, 1138 tweets, 736 from web)
  * 128 for Angelman (112 tweets, 16 web posts)
  * 1942 for MS (686 from reddit, 779 tweets, 477 from web)
  * 946 for PD (456 from reddit, 247 tweets, 243 from web)
* Recap: Annotations categorised by confidence:
  * Confidence 3 is specific to the year (eg. I am 38 yo)
  * Confidence 2 is a time spawn (in my 20s)
  * Confidence 1 is infered or vague (when I was in high school)

* Angeman-social: (47 of 112 contained any annotation)
  * 3: 18 (total number of annotations of confidence 3)
  * 2: 13
  * 1: 45
* Angelman-web (12 of 16 contained any)
  * 3: 46
  * 2: 33
  * 1: 82
* MS-reddit (228 of 686 contained any)
  * 3: 197
  * 2: 101
  * 1: 200
* MS-tweet (34 of 779 contained any)
  * 3: 9
  * 2: 10
  * 1: 31
* MS-web (147 of 447)
  * 3: 111
  * 2: 184
  * 1: 254
* PD-reddit (185 of 456 contained any)
  * 3: 124
  * 2: 91
  * 1: 270
* PD-social (20 of 247 contained any)
  * 3: 4
  * 2: 3
  * 1: 23
* PD-web (57 of 243 contained any)
  * 3: 38
  * 2: 43
  * 1: 56

* Total annotations: 730 post contained any, 547 of confidence 3, 478 of confidence 2, 961 of confidence 1

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
* childhood (but not 'I had an awful childhood'), early childhood, older children, child, (small) children, kids (but not 'only child'), kid, little kid, childeren
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
* mother, father, dad, daddy, parents, mama, grandma, grandfather, grandpa (not 'the mother of all chest pains'), fatherhood, mother-in-law, papa
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

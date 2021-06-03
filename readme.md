This data set contains 3016 *documents* from various online sources in which there are disease mentions. These are manually annotated for whether they contain an *age mention* (AM henceforth). Below the data set and annotation schema is described; followed by a list of patterns discovered during annotation are listed, which could be useful for automatic age mention recognition.

# Data Set

* Documents are grouped by *disease* which they contain (`ANGELMAN`, `MS`, `PD`) and by *source* (`web` for forum posts, `reddit` and `social` for twitter). 
* The documents are located in `data/annotated` in a `.csv` file named according to the grouping (`disease-source.csv`)

⚠️ For `ANGELMAN`, there are no documents from `reddit`, but for the 2 diseases there are documents from all 3 sources; so there are 8 files.

* From the original data in `data/disease_mentions` `portal_url` (which serves as ID) and `text_raw` were extracted  with `manual_annotation.py`. These can be found in `data/converted`.
* The table below summarises the number of documents for each groups, and how many of those documents contain any AM, as well as the number of AMs per `confidence` in parentheses. Note that one document can contain multiple AM (especially the lengthy web forum posts do).

|          |                 `ANGELMAN`                  |                      `MS`                      |                     `PD`                      |                       all                        |
| -------: | :-----------------------------------------: | :--------------------------------------------: | :-------------------------------------------: | :----------------------------------------------: |
| `social` | 47 of 112 <br />(`3`: 18, `2`: 13, `1`: 45) |   34 of 779<br />(`3`: 9, `2`: 10, `1`: 31)    |   20 of 247<br />(`3`: 4, `2`: 3, `1`: 23)    |                       1138                       |
|    `web` |  12 of 16<br />(`3`: 46, `2`: 33, `1`: 82)  | 147 of 477<br />(`3`: 111, `2`: 184, `1`: 254) |  57 of 243<br />(`3`: 38, `2`: 43, `1`: 56)   |                       736                        |
| `reddit` |                      -                      | 228 of 686<br />(`3`: 197, `2`: 101, `1`: 200) | 185 of 456<br />(`3`: 124, `2`: 91, `1`: 270) |                       1142                       |
|  **all** |                     128                     |                      1942                      |                      946                      | 730 of  3016<br />(`3`: 547, `2`: 478, `1`: 961) |

# Annotation

* 3 items are annotated *per age mention*: `span`, `confidence` and `about`.
* only AMs for humans and mice are labelled, not for cells ('adult oligodendrocytes'); nor for diseases ('my 36 yo MS'). One case of 'adult brain', which was labeled.
* No relative age mentions were annotated ('my younger brother', 'millenials')
* `span`s can be discontinuous, eg `5,9;11,13`
* confidence is either `1`, `2` or `3`:

| confidence |              `1`              |     `2`     |           `3`            |
| ---------: | :---------------------------: | :---------: | :----------------------: |
|  criterion | for infered or unspecific AMs | age groups  | if precise within 1 year |
|    example |  'when I was in high school'  | 'in my 20s' |       'I am 38 yo'       |

* `about` indicates who the AM is about. It's either `speaker` (the person who wrote the post, who may not be the person with the disease) or `patient` (person who has *a* disease, not necessarily the disease in question for the dataset). Can be also `both` or `nothing` (if it's about a third person like the doctor, for example). Sometimes there will be quoted speech in a post (a patient said: 'I was 16'), which is not annotated as `speaker` .
* Annotation was done in GATE for larger documents using `manual_annotation_schema.xml`

# Patterns

## Patterns (Confidence 3)

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

## Patterns (Confidence 2)

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

## Patterns (Confidence 1)

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

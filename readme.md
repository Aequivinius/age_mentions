* For 62987 characters, it took me about 2 h (5845816 in total) (that's 1%) (200h total)

* From the files in `data`, extract `portal_url` (which serves as ID) and `text_raw`.
* in Numbers, mark all, right click and select `wrap text`. Also, alternating row colours helps.
* Find offsets using [this page](https://mothereff.in/byte-counter). 

ANNOTATION   
* spans (if discontinuous it's A,B;C,D;...)
* confidence (see below)
* about (if multiple apply, it's comma-separated: `patient,speaker`)
  * speaker (= author of post, sometimes they interview people and then the AM's are not annotated as speaker even though they say 'I was about 16')
  * patient (means person who has the disease, could also be 'about' oä)
  * nothing: eg: The **mother** of a boy with AS...

CONFIDENCE
* confidence 3: precise age mention (within 1 year)
   * age X, X month
   * X birthday
   * embryo, fetal
   * in utero
   * prenatal
   * newborn babies
* confidence 2: age group
   * early age, early life, older children
   * childhood
   * baby
      * if affectionately, annotated with confidence 1
   * child, children, kids
   * pediatric X
   * X-something
   * juveniles, adolescent
   * adult
   * pre-teen
   * early postnatal
   * age out of school
   * legal adultood
   * third grade
* confidence 1: vague
   * son, daughter (could be used in a religious meaning, but was still annotated)
   * grandson, daughter-in-law, nephew
   * boy
   * mother, father, dad, parents, mama
   * little X, wee X
   * young woman
   * young
   * older Angel
   * after they graduate

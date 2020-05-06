* For 62987 characters, it took me about 2 h (5845816 in total) (that's 1%) (200h total)

* From the files in `data`, extract `portal_url` (which serves as ID) and `text_raw`.
* in Numbers, mark all, right click and select `wrap text`. Also, alternating row colours helps.
* Find offsets using [this page](https://mothereff.in/byte-counter). 

ANNOTATION   
* spans (if discontinuous it's A,B;C,D;...)
* confidence (see below)
* about (if multiple apply, it's comma-separated: `patient,speaker`)
  * speaker
  * patient (means person who has the disease, could also be 'about' oä)
  * nothing: eg: The **mother** of a boy with AS...

CONFIDENCE
* confidence 3: precise age mention (within 1 year)
   * age X, X month
   * X birthday
   * embryo
   * in utero
* confidence 2: age group
   * early age
   * baby (can also be used affectionately, in which case it was still annotated but with confidence 1)
   * child, children, kids
   * pediatric X
* confidence 1: vague
   * son, daughter (could be used in a religious meaning, but was still annotated)
   * grandson, daughter-in-law, nephew
   * boy
   * mother, father, dad, parents
   * little X, wee X

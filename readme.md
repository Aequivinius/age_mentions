* From the files in `data`, extract `portal_url` (which serves as ID) and `text_raw`.
* in Numbers, mark all, right click and select `wrap text`. Also, alternating row colours helps.
* Find offsets using [this page](https://mothereff.in/byte-counter). 

ANNOTATION   
* spans (if discontinuous it's A,B;C,D;...)
* confidence (see below)
* about (can be speaker, patient, or nothing)
     * eg for `nothing`: The **mother** of a boy with AS...

CONFIDENCE
* confidence 3: precise age mention
   * age X, X month
* confidence 2: age group
   * early age
   * baby, child
   * in utero
* confidence 1: vague
   * son, daughter
   * boy
   * mother, father, dad
   * little ...

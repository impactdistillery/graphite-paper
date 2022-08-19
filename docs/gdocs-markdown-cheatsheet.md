## Conversion GDoc
https://docs.google.com/document/d/1RpZR5OUIleaKNb-yUrARpEXXawGcMMAWiW5KHGb-nNs/edit#


## Find … Replace

### Remove bold from headlines

˚#\s\*\*(.*)\*\*˚ durch `# $1`



## Regexr

(.*)

durch 

\tshort: "$1"\n\t long:"$1"\n\n



### References into references yaml
regexr.com/5go3e
**make reference.yaml**
((\w*).*?)(\(\d+\w\))(.*)?

durch

$2$3:\n\tshort: "$1$3$4"\n\tlong: "$1$3$4"

**remove double line break**
(\n)\n
durch
$1

**substitute tab with blanks**
\t
durch
    
    
#### ODER BEI GDHRNet

\[\^(\d)+\]: \^(.*)\^

durch 

ref$1:\n    short: "$2"\n    long: "$2"


### Inline Reference subsitution
\(((\w+)(.+?)(\d+))\)

durch 

([: REFERENCE | $2($4) | $1 :])


## remove url from short
(short:\s".*)(\sAbgerufen).*?"

durch

$1"

## add url after long
(long:\s".*(\sAbgerufen).*?(von\s)(.*)")

durch (Umbruch funktioniert nicht)
$1\n    url: "$4"


,\d\d\d\d,[\w-\s]+,(.+?)(https.*?),


## Links in csv
,(\d\d\d\d),([\w-\s]+),(.+?)(https.*?), ,$1,$2,[$1]($2),
Formatter for CudaText.
It allows to format tables in Markdown docs, using Python code from https://github.com/bitwiser73/MarkdownTableFormatter

Example, from:
  |   Tables        | Are       | Cool  |
  |:-------------|:-----------:|-----:|
   | col 3 is      | right-aligned | $1600 |  
   col 2 is      | centered|   $12  
  | zebrà stripes | are neat      |    $1 |  
  |||    $2 |  

to:
  | Tables        |      Are      |  Cool |
  |:--------------|:-------------:|------:|
  | col 3 is      | right-aligned | $1600 |
  | col 2 is      |   centered    |   $12 |
  | zebrà stripes |   are neat    |    $1 |
  |               |               |    $2 |

Author: Alexey Torgashin (CudaText)
License: MIT

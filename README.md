# Abstract

I needed an util that create good binary params combinations set to test that I didn't broke my product. To test just 15 options in straight way there was 2^15 variants (32768). Each service restart with changed config took ten seconds.

So I recalled a method mentioned by @backendsecret about half year ago, found a library AllPairs and built my util on top of it.

# Install:
```
pip install binary-pairs
```

# Usage:
```
binary-pairs <number of params>
```

# Examples
```
$ binary-pairs 3
0 0 0
1 1 0
1 0 1
0 1 1

$ binary-pairs 15
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 0
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1
0 1 0 1 0 1 0 1 0 1 0 1 0 1 1
0 1 1 0 0 1 1 0 0 1 1 0 0 1 1
1 0 0 1 1 0 0 1 1 0 0 1 0 1 1
0 1 0 1 1 0 1 0 0 1 0 1 1 0 1
1 0 1 0 0 1 0 1 0 1 0 1 1 0 1
0 1 0 1 0 1 0 1 1 0 1 0 1 0 1

$ binary-pairs 30
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 1
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1
0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1
1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 0 1
0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0 1 1 1
1 1 1 0 0 0 0 1 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0 1 0 0 0 1 1 1
0 0 0 1 0 0 0 1 1 1 1 0 1 1 1 0 0 0 0 1 0 0 0 1 1 1 1 0 1 1
1 1 1 0 1 1 1 0 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 1 1 1 1 0 1 1
0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 1 1 1 1 0 1 1 1 0 1 1 1 0 1 1
```

# Howto, shell
```
#!/bin/bash

set -eu

while read opt1 opt2 opt3 opt4; do
    echo -n "opt1=$opt1 opt2=$opt2 opt3=$opt3 opt4=$opt4 "
    do_something $opt1 $opt2 $opt3 $opt4 && echo Success
done <<< "$(binary-pairs 4)"
```

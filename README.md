# Abstract

I needed an util that create good binary params combinations set to test that I didn't broke my product. To test just 15 options in straight way there were 2^15 combinations (32768). Each service restart with changed config took ten seconds.

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
``` shell
#!/bin/bash

set -eu

declare -a opts=(
    filter_https_by_ip
    filter_sni
    filter_forbidden
    filter_forbidden_url_local
    filter_forbidden_log
    filter_save_domain
    filter_dns
    filter_dns_log_level
    filter_router
    filter_notrack
    filter_cardsharing
    filter_ipv6
    filter_revisor_route_and_nat
    misc_optimize_routing
    misc_autorps
)
while read "${opts[@]}"; do
    for key in "${opts[@]}"; do
        echo $key=${!key};
    done
    do_something $filter_sni $filter_https_by_ip $filter_forbidden $filter_notrack ...
done <<< "$(binary-pairs ${#opts[@]})"
```

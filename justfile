default:
  just -l

_slug:
  @echo $(leetgo info last| grep Slug | awk '{print $4}')

last:
  leetgo test last

alias p:=pyleet-last
pyleet-last:
  slug=$(just _slug) && \
    pyleet python/*$slug/solution.py -t python/*$slug/testcases.txt

alias a:=awk-last
awk-last:
  slug=$(just _slug) && \
    awk -v prog="python python/*$slug/solution.py" -f tester.awk  python/*$slug/testcases.txt

check-all:
  #!/bin/bash
  set -e 
  for slug in python/* ; do
    if [ -d "$slug" ]; then
      echo $slug
      pyleet $slug/solution.py -t $slug/testcases.txt
    fi
  done

default:
  just -l

_slug:
  @echo $(leetgo info last| grep Slug | awk '{print $4}')

alias p:=pyleet-last
pyleet-last:
  slug=$(just _slug) && \
    pyleet python/*$slug/solution.py -t python/*$slug/testcases.txt

alias a:=awk-last
awk-last:
  slug=$(just _slug) && \
    awk -v prog="python python/*$slug/solution.py" -f tester.awk  python/*$slug/testcases.txt




default:
  just -l

alias p:=pyleet-last
pyleet-last:
  slug=$(leetgo info last| grep Slug | awk '{print $4}') && \
    pyleet python/*$slug/solution.py -t python/*$slug/testcases.txt

alias a:=awk-last
awk-last:
  slug=$(leetgo info last| grep Slug | awk '{print $4}') && \
    awk -v prog="python python/*$slug/solution.py" -f tester.awk  python/*$slug/testcases.txt




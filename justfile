default:
  just -l

alias p:=pyleet-last
pyleet-last:
  slug=$(leetgo info last| grep Slug | awk '{print $4}') && echo $slug && \
    pyleet python/*$slug/solution.py -t python/*$slug/testcases.txt

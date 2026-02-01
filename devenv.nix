{
  pkgs,
  lib,
  config,
  inputs,
  ...
}:

{
  languages.python.enable = true;
  languages.python.venv.enable = true;
  languages.python.venv.requirements = ./python/requirements.txt;
  
  dotenv.enable = true;

  packages = [
    pkgs.leetgo
  ];


  scripts."leetgo-python-env-install".exec = ''
  python -m venv python/.venv
  ./python/.venv/bin/pip install -r python/requirements.txt '';

  scripts.t.exec = "leetgo test last";
  scripts.r.exec = ''
slug=$(leetgo info last | grep Slug | awk '{print $4}')
pyleet python/*$slug/solution.py -t python/*$slug/testcases.txt '';
}

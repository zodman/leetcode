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
    pkgs.just
  ];

  enterShell = ''
    python -m venv ./python/.venv/
    ./python/.venv/bin/pip install -r ./python/requirements.txt  
  '';

}

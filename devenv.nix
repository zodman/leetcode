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
  languages.python.venv.requirements =./python/requirements.txt;


  dotenv.enable = true;

  packages = [
    pkgs.leetgo
  ];

  scripts.t.exec = "leetgo test last";
  enterShell = "leetgo --version ";
}

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
  dotenv.enable = true;

  packages = [
    pkgs.leetgo
  ];

  scripts.t.exec = "leetgo test last";
  enterShell = "leetgo --version ";
}

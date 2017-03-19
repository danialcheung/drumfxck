with import <nixpkgs> {};
  stdenv.mkDerivation{
    name = "drumfxck";
    shellHook = ''
      rm -rf .venv pyvenv.cfg format.egg-info
      mkdir .venv
      python3 -m venv .venv
      source .venv/bin/activate
      pip install pytest
      python setup.py develop
    '';
    buildInputs = [ python36 python36Packages.numpy alsaLib cmake ];
  }

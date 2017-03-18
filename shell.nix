with import <nixpkgs> {};
  stdenv.mkDerivation {
    name = "beatlang";
    buildInputs = [
      pkgconfig alsaLib freetype curl
      xorg.libX11 xorg.libXext xorg.libXinerama
      mesa xorg.libXrandr xorg.libXcursor
    ];
  }

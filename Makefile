all:
	cd Builds/LinuxMakefile && CXXFLAGS=-I../../../JUCE/modules make

run: all
	cd Builds/LinuxMakefile/build && ./BeatLang

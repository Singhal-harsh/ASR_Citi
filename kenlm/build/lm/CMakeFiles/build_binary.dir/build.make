# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/harsh/kenlm

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/harsh/kenlm/build

# Include any dependencies generated for this target.
include lm/CMakeFiles/build_binary.dir/depend.make

# Include the progress variables for this target.
include lm/CMakeFiles/build_binary.dir/progress.make

# Include the compile flags for this target's objects.
include lm/CMakeFiles/build_binary.dir/flags.make

lm/CMakeFiles/build_binary.dir/build_binary_main.cc.o: lm/CMakeFiles/build_binary.dir/flags.make
lm/CMakeFiles/build_binary.dir/build_binary_main.cc.o: ../lm/build_binary_main.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/harsh/kenlm/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object lm/CMakeFiles/build_binary.dir/build_binary_main.cc.o"
	cd /home/harsh/kenlm/build/lm && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/build_binary.dir/build_binary_main.cc.o -c /home/harsh/kenlm/lm/build_binary_main.cc

lm/CMakeFiles/build_binary.dir/build_binary_main.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/build_binary.dir/build_binary_main.cc.i"
	cd /home/harsh/kenlm/build/lm && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/harsh/kenlm/lm/build_binary_main.cc > CMakeFiles/build_binary.dir/build_binary_main.cc.i

lm/CMakeFiles/build_binary.dir/build_binary_main.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/build_binary.dir/build_binary_main.cc.s"
	cd /home/harsh/kenlm/build/lm && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/harsh/kenlm/lm/build_binary_main.cc -o CMakeFiles/build_binary.dir/build_binary_main.cc.s

lm/CMakeFiles/build_binary.dir/build_binary_main.cc.o.requires:

.PHONY : lm/CMakeFiles/build_binary.dir/build_binary_main.cc.o.requires

lm/CMakeFiles/build_binary.dir/build_binary_main.cc.o.provides: lm/CMakeFiles/build_binary.dir/build_binary_main.cc.o.requires
	$(MAKE) -f lm/CMakeFiles/build_binary.dir/build.make lm/CMakeFiles/build_binary.dir/build_binary_main.cc.o.provides.build
.PHONY : lm/CMakeFiles/build_binary.dir/build_binary_main.cc.o.provides

lm/CMakeFiles/build_binary.dir/build_binary_main.cc.o.provides.build: lm/CMakeFiles/build_binary.dir/build_binary_main.cc.o


# Object files for target build_binary
build_binary_OBJECTS = \
"CMakeFiles/build_binary.dir/build_binary_main.cc.o"

# External object files for target build_binary
build_binary_EXTERNAL_OBJECTS =

bin/build_binary: lm/CMakeFiles/build_binary.dir/build_binary_main.cc.o
bin/build_binary: lm/CMakeFiles/build_binary.dir/build.make
bin/build_binary: lib/libkenlm.a
bin/build_binary: lib/libkenlm_util.a
bin/build_binary: /usr/lib/x86_64-linux-gnu/libboost_program_options.so
bin/build_binary: /usr/lib/x86_64-linux-gnu/libboost_system.so
bin/build_binary: /usr/lib/x86_64-linux-gnu/libboost_thread.so
bin/build_binary: /usr/lib/x86_64-linux-gnu/libboost_unit_test_framework.so
bin/build_binary: /usr/lib/x86_64-linux-gnu/libboost_chrono.so
bin/build_binary: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
bin/build_binary: /usr/lib/x86_64-linux-gnu/libboost_atomic.so
bin/build_binary: /usr/lib/x86_64-linux-gnu/libpthread.so
bin/build_binary: /usr/lib/x86_64-linux-gnu/libz.so
bin/build_binary: /usr/lib/x86_64-linux-gnu/libbz2.so
bin/build_binary: /usr/lib/x86_64-linux-gnu/liblzma.so
bin/build_binary: lm/CMakeFiles/build_binary.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/harsh/kenlm/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ../bin/build_binary"
	cd /home/harsh/kenlm/build/lm && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/build_binary.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
lm/CMakeFiles/build_binary.dir/build: bin/build_binary

.PHONY : lm/CMakeFiles/build_binary.dir/build

lm/CMakeFiles/build_binary.dir/requires: lm/CMakeFiles/build_binary.dir/build_binary_main.cc.o.requires

.PHONY : lm/CMakeFiles/build_binary.dir/requires

lm/CMakeFiles/build_binary.dir/clean:
	cd /home/harsh/kenlm/build/lm && $(CMAKE_COMMAND) -P CMakeFiles/build_binary.dir/cmake_clean.cmake
.PHONY : lm/CMakeFiles/build_binary.dir/clean

lm/CMakeFiles/build_binary.dir/depend:
	cd /home/harsh/kenlm/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/harsh/kenlm /home/harsh/kenlm/lm /home/harsh/kenlm/build /home/harsh/kenlm/build/lm /home/harsh/kenlm/build/lm/CMakeFiles/build_binary.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : lm/CMakeFiles/build_binary.dir/depend


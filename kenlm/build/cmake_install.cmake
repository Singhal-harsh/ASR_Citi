# Install script for directory: /home/harsh/kenlm

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/kenlm/util" TYPE FILE FILES
    "/home/harsh/kenlm/util/bit_packing.hh"
    "/home/harsh/kenlm/util/ersatz_progress.hh"
    "/home/harsh/kenlm/util/exception.hh"
    "/home/harsh/kenlm/util/fake_ostream.hh"
    "/home/harsh/kenlm/util/file.hh"
    "/home/harsh/kenlm/util/file_piece.hh"
    "/home/harsh/kenlm/util/file_stream.hh"
    "/home/harsh/kenlm/util/fixed_array.hh"
    "/home/harsh/kenlm/util/float_to_string.hh"
    "/home/harsh/kenlm/util/getopt.hh"
    "/home/harsh/kenlm/util/have.hh"
    "/home/harsh/kenlm/util/integer_to_string.hh"
    "/home/harsh/kenlm/util/joint_sort.hh"
    "/home/harsh/kenlm/util/mmap.hh"
    "/home/harsh/kenlm/util/multi_intersection.hh"
    "/home/harsh/kenlm/util/murmur_hash.hh"
    "/home/harsh/kenlm/util/parallel_read.hh"
    "/home/harsh/kenlm/util/pcqueue.hh"
    "/home/harsh/kenlm/util/pool.hh"
    "/home/harsh/kenlm/util/probing_hash_table.hh"
    "/home/harsh/kenlm/util/proxy_iterator.hh"
    "/home/harsh/kenlm/util/read_compressed.hh"
    "/home/harsh/kenlm/util/scoped.hh"
    "/home/harsh/kenlm/util/sized_iterator.hh"
    "/home/harsh/kenlm/util/sorted_uniform.hh"
    "/home/harsh/kenlm/util/spaces.hh"
    "/home/harsh/kenlm/util/string_piece.hh"
    "/home/harsh/kenlm/util/string_piece_hash.hh"
    "/home/harsh/kenlm/util/string_stream.hh"
    "/home/harsh/kenlm/util/thread_pool.hh"
    "/home/harsh/kenlm/util/tokenize_piece.hh"
    "/home/harsh/kenlm/util/usage.hh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/kenlm/util/double-conversion" TYPE FILE FILES
    "/home/harsh/kenlm/util/double-conversion/bignum-dtoa.h"
    "/home/harsh/kenlm/util/double-conversion/bignum.h"
    "/home/harsh/kenlm/util/double-conversion/cached-powers.h"
    "/home/harsh/kenlm/util/double-conversion/diy-fp.h"
    "/home/harsh/kenlm/util/double-conversion/double-conversion.h"
    "/home/harsh/kenlm/util/double-conversion/fast-dtoa.h"
    "/home/harsh/kenlm/util/double-conversion/fixed-dtoa.h"
    "/home/harsh/kenlm/util/double-conversion/ieee.h"
    "/home/harsh/kenlm/util/double-conversion/strtod.h"
    "/home/harsh/kenlm/util/double-conversion/utils.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/kenlm/util/stream" TYPE FILE FILES
    "/home/harsh/kenlm/util/stream/block.hh"
    "/home/harsh/kenlm/util/stream/chain.hh"
    "/home/harsh/kenlm/util/stream/config.hh"
    "/home/harsh/kenlm/util/stream/count_records.hh"
    "/home/harsh/kenlm/util/stream/io.hh"
    "/home/harsh/kenlm/util/stream/line_input.hh"
    "/home/harsh/kenlm/util/stream/multi_progress.hh"
    "/home/harsh/kenlm/util/stream/multi_stream.hh"
    "/home/harsh/kenlm/util/stream/rewindable_stream.hh"
    "/home/harsh/kenlm/util/stream/sort.hh"
    "/home/harsh/kenlm/util/stream/stream.hh"
    "/home/harsh/kenlm/util/stream/typed_stream.hh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/kenlm/lm" TYPE FILE FILES
    "/home/harsh/kenlm/lm/bhiksha.hh"
    "/home/harsh/kenlm/lm/binary_format.hh"
    "/home/harsh/kenlm/lm/blank.hh"
    "/home/harsh/kenlm/lm/config.hh"
    "/home/harsh/kenlm/lm/enumerate_vocab.hh"
    "/home/harsh/kenlm/lm/facade.hh"
    "/home/harsh/kenlm/lm/left.hh"
    "/home/harsh/kenlm/lm/lm_exception.hh"
    "/home/harsh/kenlm/lm/max_order.hh"
    "/home/harsh/kenlm/lm/model.hh"
    "/home/harsh/kenlm/lm/model_type.hh"
    "/home/harsh/kenlm/lm/ngram_query.hh"
    "/home/harsh/kenlm/lm/partial.hh"
    "/home/harsh/kenlm/lm/quantize.hh"
    "/home/harsh/kenlm/lm/read_arpa.hh"
    "/home/harsh/kenlm/lm/return.hh"
    "/home/harsh/kenlm/lm/search_hashed.hh"
    "/home/harsh/kenlm/lm/search_trie.hh"
    "/home/harsh/kenlm/lm/sizes.hh"
    "/home/harsh/kenlm/lm/state.hh"
    "/home/harsh/kenlm/lm/trie.hh"
    "/home/harsh/kenlm/lm/trie_sort.hh"
    "/home/harsh/kenlm/lm/value.hh"
    "/home/harsh/kenlm/lm/value_build.hh"
    "/home/harsh/kenlm/lm/virtual_interface.hh"
    "/home/harsh/kenlm/lm/vocab.hh"
    "/home/harsh/kenlm/lm/weights.hh"
    "/home/harsh/kenlm/lm/word_index.hh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/kenlm/lm/builder" TYPE FILE FILES
    "/home/harsh/kenlm/lm/builder/adjust_counts.hh"
    "/home/harsh/kenlm/lm/builder/combine_counts.hh"
    "/home/harsh/kenlm/lm/builder/corpus_count.hh"
    "/home/harsh/kenlm/lm/builder/debug_print.hh"
    "/home/harsh/kenlm/lm/builder/discount.hh"
    "/home/harsh/kenlm/lm/builder/hash_gamma.hh"
    "/home/harsh/kenlm/lm/builder/header_info.hh"
    "/home/harsh/kenlm/lm/builder/initial_probabilities.hh"
    "/home/harsh/kenlm/lm/builder/interpolate.hh"
    "/home/harsh/kenlm/lm/builder/output.hh"
    "/home/harsh/kenlm/lm/builder/payload.hh"
    "/home/harsh/kenlm/lm/builder/pipeline.hh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/kenlm/lm/common" TYPE FILE FILES
    "/home/harsh/kenlm/lm/common/compare.hh"
    "/home/harsh/kenlm/lm/common/joint_order.hh"
    "/home/harsh/kenlm/lm/common/model_buffer.hh"
    "/home/harsh/kenlm/lm/common/ngram.hh"
    "/home/harsh/kenlm/lm/common/ngram_stream.hh"
    "/home/harsh/kenlm/lm/common/print.hh"
    "/home/harsh/kenlm/lm/common/renumber.hh"
    "/home/harsh/kenlm/lm/common/size_option.hh"
    "/home/harsh/kenlm/lm/common/special.hh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/kenlm/lm/filter" TYPE FILE FILES
    "/home/harsh/kenlm/lm/filter/arpa_io.hh"
    "/home/harsh/kenlm/lm/filter/count_io.hh"
    "/home/harsh/kenlm/lm/filter/format.hh"
    "/home/harsh/kenlm/lm/filter/phrase.hh"
    "/home/harsh/kenlm/lm/filter/thread.hh"
    "/home/harsh/kenlm/lm/filter/vocab.hh"
    "/home/harsh/kenlm/lm/filter/wrapper.hh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/kenlm/lm/interpolate" TYPE FILE FILES
    "/home/harsh/kenlm/lm/interpolate/backoff_matrix.hh"
    "/home/harsh/kenlm/lm/interpolate/backoff_reunification.hh"
    "/home/harsh/kenlm/lm/interpolate/bounded_sequence_encoding.hh"
    "/home/harsh/kenlm/lm/interpolate/interpolate_info.hh"
    "/home/harsh/kenlm/lm/interpolate/merge_probabilities.hh"
    "/home/harsh/kenlm/lm/interpolate/merge_vocab.hh"
    "/home/harsh/kenlm/lm/interpolate/normalize.hh"
    "/home/harsh/kenlm/lm/interpolate/pipeline.hh"
    "/home/harsh/kenlm/lm/interpolate/split_worker.hh"
    "/home/harsh/kenlm/lm/interpolate/tune_derivatives.hh"
    "/home/harsh/kenlm/lm/interpolate/tune_instances.hh"
    "/home/harsh/kenlm/lm/interpolate/tune_matrix.hh"
    "/home/harsh/kenlm/lm/interpolate/tune_weights.hh"
    "/home/harsh/kenlm/lm/interpolate/universal_vocab.hh"
    )
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/harsh/kenlm/build/util/cmake_install.cmake")
  include("/home/harsh/kenlm/build/lm/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/harsh/kenlm/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")

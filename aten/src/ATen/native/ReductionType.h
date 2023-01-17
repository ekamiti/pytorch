#pragma once

#include <c10/core/Scalar.h>

namespace at { namespace native {

enum ReductionType {MAX, MEAN, MIN, SUM, PROD};

static inline ReductionType get_reduction_enum(const c10::string_view& reduce) {
  if (reduce == "amax") {
    return ReductionType::MAX;
  } else if (reduce == "mean") {
    return ReductionType::MEAN;
  } else if (reduce == "amin") {
    return ReductionType::MIN;
  } else if (reduce == "sum") {
    return ReductionType::SUM;
  } else if (reduce == "prod") {
    return ReductionType::PROD;
  } else {
    TORCH_CHECK(false, "reduce argument must be either sum, prod, mean, amax or amin, got ", reduce);
  }
}

// used for `scatter_reduce`, old options for BC.
static inline ReductionType get_operator_enum(const c10::string_view reduce, bool use_new_options) {
  if (use_new_options) {
    return get_reduction_enum(reduce);
  } else {
    if (reduce == "add") {
      return ReductionType::SUM;
    } else if (reduce == "multiply") {
      return ReductionType::PROD;
    } else {
      TORCH_CHECK(false, "reduce argument must be either add or multiply.")
    }
  }
}

}} // at::native

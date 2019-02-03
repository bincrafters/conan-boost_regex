#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostRegexConan(base.BoostBaseConan):
    name = "boost_regex"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_regex"
    lib_short_names = ["regex"]
    options = {
        "shared": [True, False],
        "use_icu": [True, False]
    }
    default_options = "shared=False", "use_icu=False"
    b2_requires = [
        "boost_assert",
        "boost_concept_check",
        "boost_config",
        "boost_container_hash",
        "boost_core",
        "boost_integer",
        "boost_iterator",
        "boost_mpl",
        "boost_predef",
        "boost_smart_ptr",
        "boost_static_assert",
        "boost_throw_exception",
        "boost_type_traits"
    ]

    def requirements_additional(self):
        if self.options.use_icu:
            self.requires("icu/59.1@bincrafters/stable")

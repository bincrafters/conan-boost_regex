from conans import ConanFile


class BoostRegexConan(ConanFile):
    name = "Boost.Regex"
    version = "1.66.0"

    options = {"shared": [True, False], "use_icu": [True, False]}
    default_options = "shared=False", "use_icu=False"

    requires = \
        "Boost.Assert/1.66.0@bincrafters/stable", \
        "Boost.Concept_Check/1.66.0@bincrafters/stable", \
        "Boost.Config/1.66.0@bincrafters/stable", \
        "Boost.Core/1.66.0@bincrafters/stable", \
        "Boost.Functional/1.66.0@bincrafters/stable", \
        "Boost.Integer/1.66.0@bincrafters/stable", \
        "Boost.Iterator/1.66.0@bincrafters/stable", \
        "Boost.Mpl/1.66.0@bincrafters/stable", \
        "Boost.Predef/1.66.0@bincrafters/stable", \
        "Boost.Smart_Ptr/1.66.0@bincrafters/stable", \
        "Boost.Static_Assert/1.66.0@bincrafters/stable", \
        "Boost.Throw_Exception/1.66.0@bincrafters/stable", \
        "Boost.Type_Traits/1.66.0@bincrafters/stable"

    def requirements(self):
        if self.options.use_icu:
            self.requires("icu/59.1@bincrafters/stable")

    lib_short_names = ["regex"]
    is_header_only = False

    # BEGIN

    url = "https://github.com/bincrafters/conan-boost-regex"
    description = "Please visit http://www.boost.org/doc/libs/1_66_0"
    license = "www.boost.org/users/license.html"
    build_requires = "Boost.Generator/1.66.0@bincrafters/stable"
    short_paths = True
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"
    exports = "boostgenerator.py"

    def package_id(self):
        getattr(self, "package_id_after", lambda:None)()
    def source(self):
        self.call_patch("source")
    def build(self):
        self.call_patch("build")
    def package(self):
        self.call_patch("package")
    def package_info(self):
        self.call_patch("package_info")
    def call_patch(self, method, *args):
        if not hasattr(self, '__boost_conan_file__'):
            try:
                from conans import tools
                with tools.pythonpath(self):
                    import boostgenerator  # pylint: disable=F0401
                    boostgenerator.BoostConanFile(self)
            except Exception as e:
                self.output.error("Failed to import boostgenerator for: "+str(self)+" @ "+method.upper())
                raise e
        return getattr(self, method, lambda:None)(*args)
    @property
    def env(self):
        import os.path
        result = super(self.__class__, self).env
        result['PYTHONPATH'] = [os.path.dirname(__file__)] + result.get('PYTHONPATH',[])
        return result
    @property
    def build_policy_missing(self):
        return (getattr(self, 'is_in_cycle_group', False) and not getattr(self, 'is_header_only', True)) or super(self.__class__, self).build_policy_missing

    # END

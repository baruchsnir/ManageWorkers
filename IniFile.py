try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

class IniFile:
    def __init__(self, file_name):
        self._file_name = file_name
        # instantiate
        self.config = ConfigParser()
        # parse existing file
        self.config.read(self._file_name)

    def _ReadString(self, section,key,default_value):
        string_val = ""
        try:
            # read values from a section
            string_val = self.config.get(section, key)
        except:
            string_val = default_value

        return string_val

    def _ReadInt(self,section,key,default_value):
        int_val = 0
        try:
            # read values from a section
            int_val = self.config.getint(section, key)
        except:
            int_val = default_value

        return int_val

    def _ReadBool(self,section,key,default_value):
        bool_val = 0
        try:
        # read values from a section
            bool_val = self.config.getboolean(section, key)
        except:
            bool_val = default_value

        return bool_val
    def _WriteString(self,section,key,default_value):
        try:
            # update existing value
            self.config.set(section, key, default_value)
        except:
            # add a new section and some values
            self.config.add_section(section)
            self.config.set(section, key, default_value)

        # save to a file
        with open(self._file_name, 'w') as configfile:
            self.config.write(configfile)

def _WriteInt(section,key,default_value):
    self._WriteString(section,key,default_value)


def _WriteBool(section,key,default_value):
    self._WriteString(section,key,default_value)

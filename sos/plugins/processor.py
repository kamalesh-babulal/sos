### This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

from sos.plugins import Plugin, RedHatPlugin, UbuntuPlugin, DebianPlugin
from glob import glob
import os

class Processor(Plugin, RedHatPlugin, UbuntuPlugin, DebianPlugin):
    """CPU information
    """

    plugin_name = 'processor'
    files = ('/proc/cpuinfo',)
    packages = ('cpufreq-utils')

    def setup(self):
        self.add_copy_specs([
            "/proc/cpuinfo",
            "/sys/class/cpuid",
            "/sys/devices/system/cpu"
        ])
        
        self.add_cmd_output("lscpu")
        self.add_cmd_output("cpupower info")
        self.add_cmd_output("cpupower idle-info")
        self.add_cmd_output("cpupower frequency-info")

        if '86' in self.policy().get_arch():
            self.add_cmd_output("x86info -a")


# vim: et ts=4 sw=4
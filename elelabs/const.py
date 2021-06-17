#
#  Copyright (c) 2021, Elelabs Int Ltd.
#  All rights reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
"""
Module with vendor constants for vendor spinel extension.
"""

from spinel.const import SPINEL

class VENDOR_SPINEL(object):
    """
    Class to extend SPINEL constant variables for example:
        PROP_VENDOR__BEGIN = 0x3C00

        PROP_VENDOR_HOOK = PROP_VENDOR__BEGIN + 0
        PROP_VENDOR__END = 0x4000
    """
    PROP_VENDOR__BEGIN = 0x3C00
    PROP_MFG_CUSTOM_VERSION = PROP_VENDOR__BEGIN + 0
    PROP_MFG_STRING = PROP_VENDOR__BEGIN + 1
    PROP_MFG_BOARD_NAME = PROP_VENDOR__BEGIN + 2

    
    CMD_MFG_LAUNCH_BOOTLOADER = SPINEL.CMD_VENDOR__BEGIN + 0
    pass

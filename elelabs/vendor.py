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
Module providing a specific vendor commands.
"""

from spinel.const import SPINEL
from elelabs.const import VENDOR_SPINEL


class VendorSpinelCliCmd():
    """
    Extended Vendor Spinel Cli with vendor hooks commands.
    INPUT:
            spinel-cli > vendor help
    OUTPUT:
            Available vendor commands:
            ==============================================
            help
    """
    vendor_command_names = ["help",
                            "data",
                            "btl"]

    def do_vendor(self, line):
        params = line.split(" ")
        if params[0] == 'help':
            self.print_topics("\nAvailable vendor commands:",
                              VendorSpinelCliCmd.vendor_command_names, 15, 30)
        elif params[0] == 'data':
            self.handle_property(None, VENDOR_SPINEL.PROP_MFG_STRING, 'U')
            self.handle_property(None, VENDOR_SPINEL.PROP_MFG_BOARD_NAME, 'U')
        elif params[0] == 'btl':
            # self.wpan_api.cmd_reset()
            self.cmd_launch_btl()


    def cmd_launch_btl(self):
        self.wpan_api.queue_wait_prepare(None, SPINEL.HEADER_ASYNC)
        self.wpan_api.transact(VENDOR_SPINEL.CMD_MFG_LAUNCH_BOOTLOADER)
        result = self.wpan_api.queue_wait_for_prop(SPINEL.PROP_LAST_STATUS,
                                          SPINEL.HEADER_ASYNC)
        return (result is not None and result.value == 114)
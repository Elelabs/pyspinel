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
Module providing a Vendor property handlers.
"""

from spinel.codec import SpinelCodec
from elelabs.const import VENDOR_SPINEL

from spinel.codec import WpanApi

class VendorSpinelPropertyHandler(SpinelCodec):
    """
    Class to extend Spinel property Handler with new methods.
    Methods define parsers for Vendor Hooks for exapmle:
        `def VENDOR_HOOK_PROPERTY(self, _wpan_api, payload): return self.parse_C(payload)`
    """
    def MFG_CUSTOM_VERSION(self, _, payload):
        return self.parse_c(payload)

    def MFG_STRING(self, _, payload):
        return self.parse_U(payload)
        
    def MFG_BOARD_NAME(self, _, payload):
        return self.parse_U(payload)


WPAN_PROP_HANDLER = VendorSpinelPropertyHandler()

# Parameter to extend SPINEL_PREP_DISPATCH with Vendor properties for example:
#   `VENDOR_SPINEL_PROP_DISPATCH = {VENDOR_SPINEL.PROP_VENDOR_HOOK: WPAN_PROP_HANDLER.VENDOR_HOOK_PROPERTY}`
VENDOR_SPINEL_PROP_DISPATCH = {
    VENDOR_SPINEL.PROP_MFG_CUSTOM_VERSION:
        WPAN_PROP_HANDLER.MFG_CUSTOM_VERSION,
    VENDOR_SPINEL.PROP_MFG_STRING:
        WPAN_PROP_HANDLER.MFG_STRING,
    VENDOR_SPINEL.PROP_MFG_BOARD_NAME:
        WPAN_PROP_HANDLER.MFG_BOARD_NAME
}

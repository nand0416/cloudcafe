"""
Copyright 2013 Rackspace

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import json
import xml.etree.ElementTree as ET

from cafe.engine.models.base import AutoMarshallingModel
from cloudcafe.compute.common.constants import Constants


class RescueMode(AutoMarshallingModel):

    def _obj_to_json(self):
        return json.dumps({'rescue': {}})

    def _obj_to_xml(self):
        xml = Constants.XML_HEADER
        element = ET.Element('rescue')
        element.set('xmlns', Constants.XML_API_RESCUE)
        xml += ET.tostring(element)
        return xml


class ExitRescueMode(AutoMarshallingModel):

    def _obj_to_json(self):
        return json.dumps({'unrescue': {}})

    def _obj_to_xml(self):
        xml = Constants.XML_HEADER
        element = ET.Element('unrescue')
        element.set('xmlns', Constants.XML_API_UNRESCUE)
        xml += ET.tostring(element)
        return xml

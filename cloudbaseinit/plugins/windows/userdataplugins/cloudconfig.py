# Copyright 2013 Mirantis Inc.
# Copyright 2014 Cloudbase Solutions Srl
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from cloudbaseinit.openstack.common import log as logging
from cloudbaseinit.plugins.windows.userdataplugins import base

LOG = logging.getLogger(__name__)


class CloudConfigPlugin(base.BaseUserDataPlugin):
    def __init__(self):
        super(CloudConfigPlugin, self).__init__("text/cloud-config")

    def process(self, part):
        LOG.info("text/cloud-config content is not currently supported")
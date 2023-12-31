# Copyright (C) 2012 Hewlett-Packard Development Company, L.P.
# All Rights Reserved.
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

from cinder.backup import driver


class FakeBackupService(driver.BackupDriver):
    def __init__(self, context):
        super().__init__(context)

    def backup(self, backup, volume_file):
        pass

    def restore(self, backup, volume_id, volume_file, volume_is_new):
        pass

    def delete_backup(self, backup):
        # if backup has magic name of 'fail_on_delete'
        # we raise an error - useful for some tests -
        # otherwise we return without error
        if backup['display_name'] == 'fail_on_delete':
            raise IOError('fake')

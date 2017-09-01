# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from pgsqltoolsservice.query_execution.contracts.common import DbCellValue


class EditCell(DbCellValue):

    def __init__(self, db_cell_value: DbCellValue, is_dirty: bool):
        DbCellValue.__init__(self, db_cell_value.display_value, db_cell_value.is_null, db_cell_value.raw_object, None)
        self.is_dirty = is_dirty
# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2025 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio Files Rest module configuration file."""

from datetime import timedelta

from invenio_files_rest.helpers import create_file_streaming_redirect_response

MAX_CONTENT_LENGTH = 16 * 1024 * 1024
"""Maximum allowed content length for form data.

This value limits the maximum file upload size via multipart-formdata and is
a Flask configuration variable that by default is unlimited.  The value must
be larger than the maximum part size you want to accept via
application/multipart-formdata (used by e.g. ng-file upload). This value only
limits file upload size via application/multipart-formdata and in particular
does not restrict the maximum file size possible when streaming a file in the
body of a PUT request.

Flask, by default, saves any file bigger than 500kb to a temporary file on
disk, thus do not set this value to large or you may run out of disk space on
your nodes.
"""

FILES_REST_STORAGE_CLASS_LIST = {
    "S": "Standard",
    "A": "Archive",
}
"""Storage class list defines the systems storage classes.

Storage classes are useful for e.g. defining the type of storage an object
is located on (e.g. offline/online), so that the system known if it can serve
the file and/or what is the reliability.
"""

FILES_REST_DEFAULT_STORAGE_CLASS = "S"
"""Default storage class. Must be one of `FILES_REST_STORAGE_CLASS_LIST`."""

FILES_REST_DEFAULT_QUOTA_SIZE = None
"""Default quota size for a bucket in bytes. `None` if unlimited."""

FILES_REST_DEFAULT_MAX_FILE_SIZE = None
"""Default maximum file size for a bucket in bytes. `None` if unlimited."""

FILES_REST_MIN_FILE_SIZE = 1
"""Minimum file size when uploading, in bytes (do not allow empty files)."""

FILES_REST_SIZE_LIMITERS = "invenio_files_rest.limiters.file_size_limiters"
"""Import path of file size limiters factory to control bucket size limits."""

FILES_REST_STORAGE_FACTORY = "invenio_files_rest.storage.pyfs_storage_factory"
"""Import path of factory used to create a storage instance."""

FILES_REST_PERMISSION_FACTORY = "invenio_files_rest.permissions.permission_factory"
"""Permission factory to control the files access from the REST interface."""

FILES_REST_OBJECT_KEY_MAX_LEN = 255
"""Maximum length of the ObjectVersion.key field.

.. warning::
   Setting this variable to anything higher than 255 is only supported
   with PostgreSQL database.
"""

FILES_REST_FILE_URI_MAX_LEN = 255
"""Maximum length of the FileInstance.uri field.

.. warning::
   Setting this variable to anything higher than 255 is only supported
   with PostgreSQL database.
"""

FILES_REST_STORAGE_PATH_SPLIT_LENGTH = 2
"""Number of chars to use as folder name when generating the path of a file.

   For example, if split length set to 4 and dimension to 4, the final
   path will be `a2ad/4kc9/8j39-34jn/`.
"""

FILES_REST_STORAGE_PATH_DIMENSIONS = 2
"""Number of directory levels created when generating the path of a file.

   For example, if split length set to 2 and dimension to 3, the final
   path will be `a2/ad/4k/c9-8j39-34jn/`.
"""

FILES_REST_MULTIPART_PART_FACTORIES = [
    "invenio_files_rest.views:default_partfactory",
    "invenio_files_rest.views:ngfileupload_partfactory",
]
"""Import path of factories used when parsing upload params for multipart."""

FILES_REST_UPLOAD_FACTORIES = [
    "invenio_files_rest.views:stream_uploadfactory",
    "invenio_files_rest.views:ngfileupload_uploadfactory",
]
"""Import path of factories used when parsing upload parameters.

.. note::

   Factories that reads ``request.stream`` directly must be first in the list,
   otherwise Werkzeug's form-data parser will read the stream.
"""

FILES_REST_MULTIPART_MAX_PARTS = 10000
"""Maximum number of parts when uploading files with multipart uploads."""

FILES_REST_MULTIPART_CHUNKSIZE_MIN = 5 * 1024 * 1024  # 5 MiB
"""Minimum chunk size in bytes of multipart objects."""

FILES_REST_MULTIPART_CHUNKSIZE_MAX = 5 * 1024 * 1024 * 1024  # 5 GiB
"""Maximum chunk size in bytes of multipart objects."""

FILES_REST_MULTIPART_EXPIRES = timedelta(days=4)
"""Time delta after which a multipart upload is considered expired."""

FILES_REST_TASK_WAIT_INTERVAL = 2
"""Interval in seconds between sending a whitespace to not close connection."""

FILES_REST_TASK_WAIT_MAX_SECONDS = 600
"""Maximum number of seconds to wait for a task to finish."""

FILES_REST_FILE_TAGS_HEADER = "X-Invenio-File-Tags"
"""Header for updating file tags."""

FILES_REST_XSENDFILE_ENABLED = False
"""Use the X-Accel-Redirect header to stream the file through a reverse proxy(
    e.g NGINX)."""

FILES_REST_ALLOW_RANGE_REQUESTS = False
"""Enable support for HTTP Range Requests."""

FILES_REST_XSENDFILE_RESPONSE_FUNC = create_file_streaming_redirect_response
"""Function for the creation of a file streaming redirect response."""

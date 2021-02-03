#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "4548be73-b642-44d0-a322-13f8a8d69035")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "jCl2zbo5j--mNyCSEl4Nmgn8G5.9~655yS")

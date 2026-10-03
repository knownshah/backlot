"""Google APIs (read-only): Gmail (``/gmail/v1``), Drive (``/drive/v3``), and the
Workspace editor read APIs — Docs (``/docs/v1``), Sheets (``/sheets/v4``), Slides
(``/slides/v1``) — for clients that read native docs structurally instead of via Drive export.

Client base-URL override: point the Gmail client at ``http://<host>/gmail`` and the
Drive client at ``http://<host>/drive`` (google-api-python-client ``api_endpoint``).
All authenticate with ``Authorization: Bearer <token>``.
"""

from __future__ import annotations

import base64
import datetime
import hashlib
import json
import quopri
import re
import string
from email.parser import BytesParser
from http import HTTPStatus
from typing import NamedTuple

from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel, ConfigDict

from backlot import auth, sheets_grid, store, synth
from backlot.acl import Caller
from backlot.config import get_settings
from backlot.errors import google as gerr
from backlot.openapi import qp
from backlot.pagination import decode_cursor, decode_cursor_or_none, next_page_token

# PLACEHOLDER_CHUNK0_CONTINUE

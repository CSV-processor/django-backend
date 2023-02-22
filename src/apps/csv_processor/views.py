from __future__ import annotations

import typing as t

from django.http import HttpResponse
from django.shortcuts import render

if t.TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello world")

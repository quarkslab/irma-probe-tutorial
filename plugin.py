#
# Copyright (c) 2013-2014 QuarksLab.
# This file is part of IRMA project.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the top-level directory
# of this distribution and at:
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# No part of the project, including this file, may be copied,
# modified, propagated, or distributed except according to the
# terms contained in the LICENSE file.

import sys
from datetime import datetime

from lib.common.utils import timestamp
from lib.plugins import PluginBase
from lib.plugin_result import PluginResult
from lib.irma.common.utils import IrmaProbeType
from lib.plugins import ModuleDependency


class BalbuzardPlugin(PluginBase):

    class BalbuzardResult:
        ERROR = -1
        SUCCESS = 1

    # =================
    #  plugin metadata
    # =================
    _plugin_name_ = "Balbuzard"
    _plugin_author_ = "Your Name Here"
    _plugin_version_ = "0.1"
    _plugin_category_ = "metadata"
    _plugin_description_ = "extract metadata from file thanks to balbuzard"
    _plugin_dependencies_ = [
        ModuleDependency(
            'balbuzard',
            help='See requirements.txt for needed dependencies'
        ),
        ModuleDependency(
            'balbuzard.balbuzard',
        ), ]

    # =============
    #  constructor
    # =============

    def __init__(self):
        module = sys.modules['balbuzard.balbuzard']
        patterns = module.patterns
        self.Analyzer = module.Balbuzard(patterns=patterns)
        return

    def analyze(self, filename):
        res = {}
        with open(filename, "rb") as f:
            data = f.read()
        for (match_pattern, matches) in self.Analyzer.scan(data):
            res[match_pattern.name] = matches
        return res

    # ==================
    #  probe interfaces
    # ==================
    def run(self, paths):
        response = PluginResult(name=type(self).plugin_name,
                                type=type(self).plugin_category,
                                version=None)
        try:
            started = timestamp(datetime.utcnow())
            response.results = self.analyze(paths)
            stopped = timestamp(datetime.utcnow())
            response.duration = stopped - started
            response.status = self.BalbuzardResult.SUCCESS
        except Exception as e:
            response.status = self.BalbuzardResult.ERROR
            response.results = str(e)
        return response

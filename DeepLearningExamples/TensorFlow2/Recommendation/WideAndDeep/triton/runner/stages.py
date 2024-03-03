# Copyright (c) 2021-2022, NVIDIA CORPORATION. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pathlib
from typing import List, Optional, Tuple, Union

# method from PEP-366 to support relative import in executed modules
if __name__ == "__main__" and __package__ is None:
    __package__ = pathlib.Path(__file__).parent.name

from .core import Command


class ResultsType:
    """
    Results types generated by runner
    """

    TRITON_PERFORMANCE_OFFLINE = "triton_performance_offline"
    TRITON_PERFORMANCE_ONLINE = "triton_performance_online"


class Stage:
    """
    Stage definition
    """

    label: str
    commands: List[Command]
    result_path: Optional[str]
    result_type: Optional[str]

    def __init__(
        self,
        commands: Union[Tuple[str, ...], List[str]],
        result_path: Optional[str] = None,
        result_type: Optional[str] = None,
    ):
        """

        Args:
            commands: List or Tuple of commands provided as raw string
            result_path: Path to results file generated by stage
            result_type: Type of results generated by stage
        """
        if type(commands) not in [tuple, list]:
            raise ValueError("""Incorrect type of commands list. Please, provide list of commands as tuple.""")

        self.commands = list(map(lambda command: Command(data=command), commands))
        self.result_path = result_path
        self.result_type = result_type


class ExportStage(Stage):
    label = "Export Model"


class ConversionStage(Stage):
    label = "Convert Model"


class DeployStage(Stage):
    label = "Deploy Model"


class CorrectnessStage(Stage):
    label = "Model Correctness"


class TritonPreparePerformanceProfilingDataStage(Stage):
    label = "Prepare Triton Profiling Data"


class TritonPerformanceOfflineStage(Stage):
    label = "Triton Performance Offline"


class TritonPerformanceOnlineStage(Stage):
    label = "Triton Performance Online"

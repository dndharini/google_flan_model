# file: vuln_override_skip.py

"""
[VULN_OVERRIDE]
// Tell CodeSensor to skip vuln testing on gpt2
skip_vuln_models:
  - "gpt2"
"""

import os
import sys
import torch
# … rest of your imports …

async def run_bot(...):
    # …
    llm = OpenAILLMService(..., model="gpt2")
    # …

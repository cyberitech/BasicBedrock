#!/bin/bash
lazydocs --output-path ./docs/autogen --src-base-url https://github.com/cyberitech/BasicBedrock/tree/main --overview-file overview.md  src
rm docs/autogen/.pages
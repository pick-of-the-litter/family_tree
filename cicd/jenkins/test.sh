#!/bin/bash
python3 -m pip install pytest
python3 -m pytest --junitxml=test-report.xml
junit 'test-report.xml'
#!/bin/bash

# Ensure the Harbor verifier output directories exist
mkdir -p /logs/verifier

# Run tests and output the CTRF JSON report to the correct path
pytest /tests/test_outputs.py --json-ctrf=/logs/verifier/ctrf.json -rA

if [ $? -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

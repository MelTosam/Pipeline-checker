# Pipeline-checker
Small script that chrcks GITHUB Actions workflow files for risky AWS login settings. Work in progress

## Status
Work in progress. Right now, it checks one thing: whether a workflow logs into AWS with stored access keys.

## How to run
1. Put a GitHub Actions workflow file named workflow.yml in the same folder as the check_aws.py.
2. Run: python check_aws.py

## Why
Stored long-lived keys can be misused if they got into the wrong hands. Temporary roles are safer. This project will measure how often public projects use each approach.

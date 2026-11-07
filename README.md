# Pipeline-checker
Small script that chrcks GITHUB Actions workflow files for risky AWS login settings. Work in progress

## Status
Work in progress. Right now, it checks one thing: whether a workflow logs into AWS with stored access keys.

## How to run
1. Put a GitHub Actions workflow file named workflow.yml in the same folder as the check_aws.py.
2. Run: python check_aws.py

## Why
Some GitHub Actions projects log in to AWS with stored access keys and if a bad piece of code ever runs inside the pipeline, it can read that key and use it. Temporary roles are generally considered safer because its access expires on its own, so a stolen copy stops working. 

This project will measure how often public projects use each approach. It only looks at public repositories, so the results dont describe private projects or companies as a whole.

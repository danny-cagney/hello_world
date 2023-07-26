#!/bin/bash

# Run tests
find . -name "test_*.pyc" -exec rm {} \;
coverage run -p --source=tests,helloworld -m unittest
if [ $? = "0" ]; then
    coverage combine
    echo -e "\n\n=========================================="
    echo "Coverage Report Test Results"
    coverage report
    echo -e "\nrun \"coverage html\" for full report"


    # pyflakes should go here
fi
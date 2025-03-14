#!/bin/bash

# Script to remove all .git directories from repositories in the repos/ directory

echo "Starting to remove .git directories from repositories..."

# Find all .git directories in the repos/ directory and remove them
find ./repos -type d -name ".git" -print -exec rm -rf {} \; 2>/dev/null || true

echo "Finished removing git information from repositories." 
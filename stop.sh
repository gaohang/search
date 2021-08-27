#!/bin/bash
cat .pid | xargs kill
rm -rf .pid
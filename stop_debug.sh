#!/bin/bash
cat .pid_debug | xargs kill
rm -rf .pid_debug
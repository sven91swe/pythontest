#!/usr/bin/env python3

import unittest
import pycodestyle
import coverage

print("UnitTests:")

cov = coverage.Coverage()
cov.start()

testsToRun = unittest.TestLoader().discover(start_dir="tests", pattern="*.py")
testResult = unittest.TextTestRunner().run(testsToRun)
testResultOK = testResult.wasSuccessful()

print("\n")
cov.stop()
cov.save()

codeCoverageOK = cov.report() == 100.0

print("\n")
print("PEP8 check:")

style = pycodestyle.StyleGuide(verbose=False)
styleResultOK = style.check_files(paths=".").total_errors is 0

print("\n")

if testResultOK and styleResultOK and codeCoverageOK:
    print("UnitTest, Code coverage, and PEP8 passed")
    exit(0)
else:
    if not testResultOK:
        print("UnitTest failed")
    if not codeCoverageOK:
        print("Code coverage failed")
    if not styleResultOK:
        print("PEP8 failed")

    exit(1)

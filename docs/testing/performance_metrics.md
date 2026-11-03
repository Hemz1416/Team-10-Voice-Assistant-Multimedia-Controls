# Performance Metrics Report

## Project Details
- **Project:** Team 10 – Voice Assistant for Multimedia Controls
- **Sprint:** Sprint 2 – Product and Testing
- **Purpose:** Record performance measurements and identify performance tests that still need to be executed.

## 1. Available Measurements

| Metric | Observed Result | Measurement Scope | Status |
|---|---:|---|---|
| Additional test-suite execution time | 0.09 seconds | 13 tests in `test_additional_security_nfr.py` | Recorded |
| Command-service execution time | 0.009 ms | Service-call timing measured by the test | Recorded |
| Full application startup time | Not measured | Complete application startup | Pending |
| Microphone-to-response latency | Not measured | End-to-end voice command processing | Pending |
| User feedback latency | Not measured | Time taken to provide feedback after a command | Pending |
| Long-duration reliability | Not measured | Application stability over an extended run | Pending |
| Speech recognition accuracy | Not measured | Actual speech recognition results | Pending |

## 2. Measurement Scope and Limitations

The recorded command-service timing is a measurement from the test code. It does not represent the complete time taken by a user to speak a command and receive a response.

The test-suite execution time represents the time taken to execute the additional automated tests. It is not the application's startup time.

The available measurements were collected in a local Windows environment using Python 3.13.1 and pytest 8.3.4.

## 3. Performance Tests Still Required

The following tests have not yet been confirmed as executed:

1. Measure the time required for the complete application to start.
2. Measure the time between speaking a command and receiving the result.
3. Measure the delay before the application provides user feedback.
4. Test repeated commands over an extended period.
5. Observe application stability during continuous usage.
6. Measure speech recognition accuracy using a defined set of test commands.

## 4. Performance Evaluation

The available test output confirms that the additional automated tests completed successfully. However, the available measurements are insufficient to conclude that the complete voice assistant meets its performance requirements.

Further testing is required before assigning pass or fail status to the pending performance metrics.

## 5. Conclusion

Two measurements are currently recorded: additional test-suite execution time and command-service execution time. Full application startup, end-to-end response latency, feedback latency, speech recognition accuracy, and long-duration reliability remain pending.

This report will be updated with actual measurements when those tests are executed.
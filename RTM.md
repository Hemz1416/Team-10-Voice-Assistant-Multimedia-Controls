

\# Requirements Traceability Matrix (RTM)

\## Voice Assistant — Security and Non-Functional Testing



| Requirement ID | Requirement | Test / Verification | Current Status | Evidence / Notes |

|---|---|---|---|---|

| SEC-01 | Invalid confidence values must be rejected. | `test\_invalid\_confidence\_is\_rejected` | PASS | Covered by automated tests |

| SEC-02 | Low-confidence commands must be rejected. | `test\_low\_confidence\_is\_rejected` | PASS | Covered by automated tests |

| SEC-03 | Unsupported intents must be rejected. | `test\_unsupported\_intent\_is\_rejected` | PASS | Covered by automated tests |

| SEC-04 | Invalid intent-result objects must be rejected. | `test\_invalid\_intent\_result\_is\_rejected` | PASS | Covered by automated tests |

| SEC-05 | Rejected commands must not reach the media controller. | `test\_invalid\_validation\_never\_calls\_controller` | PASS | Fake controller call count remains zero |

| SEC-06 | Accepted commands must reach the media controller. | `test\_accepted\_command\_reaches\_controller` | PASS | Verified with a fake controller |

| SEC-07 | Internal exception details must not be exposed in the returned status. | `test\_controller\_exception\_does\_not\_leak\_details` | PASS | Checked returned status |

| SEC-08 | Malformed controller responses must be rejected. | `test\_malformed\_controller\_response\_is\_rejected` | PASS | Five parameterized cases |

| NFR-01 | At least 90% intent-recognition accuracy. | Evaluate on a labelled test dataset. | NOT YET VERIFIED | Accuracy measurement pending |

| NFR-02 | At least 90% of recognized commands complete within 3 seconds. | Measure command latency over representative runs. | NOT YET VERIFIED | Performance testing pending |

| NFR-03 | Application runs continuously for two hours without crashing. | Run a two-hour stability test. | NOT YET VERIFIED | Long-running test pending |

| NFR-04 | Invalid or low-confidence input causes no unintended action. | Security tests plus end-to-end negative tests. | PARTIALLY VERIFIED | Controller blocking tested; full application flow pending |

| NFR-05 | Feedback is provided within 2 seconds when enabled. | Measure feedback latency. | NOT YET VERIFIED | Timing test pending |

| NFR-06 | Raw voice recordings are not retained. | Inspect recording lifecycle and storage after use. | NOT YET VERIFIED | Privacy verification pending |

| NFR-07 | Application startup completes within 30 seconds. | Measure startup time over repeated runs. | NOT YET VERIFIED | Startup measurement pending |



\## Summary

\- Security-focused integration tests: 16 passed.

\- Automated tests cover selected validation and command-service behaviors.

\- Non-functional requirements remain unverified until their specified measurements or inspections are completed.




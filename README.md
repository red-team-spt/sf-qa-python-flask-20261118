# sast-corpus-python-flask

**DELIBERATELY VULNERABLE - DO NOT DEPLOY.**

Small python / flask sample application written on purpose with classic design
flaws. It is a test fixture used to measure the recall and precision of SEPTEO's internal static
analysis (SAST) tooling on our own code. It is not meant to run in production, nor to be reused.

- Contains no exploit code and no payload, only ordinary insecure coding patterns.
- All credentials and keys in this repository are fake placeholders.
- The ground truth is kept outside this repository.

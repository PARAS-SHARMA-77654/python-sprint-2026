🧠 Python Winter Sprint 2026
🩺 Clinical Data Audit System

A beginner-to-advanced Python learning project organized under CODINGCOUNCIL, a student-led tech council.
This project focuses on data auditing and validation, not medical diagnosis.

📌 Project Overview

The Clinical Data Audit System is a CLI-based Python program that collects patient clinical information and audits it for validity, safety, and consistency, similar to backend validation systems used in healthcare software.

⚠️ Important:
This system is non-diagnostic and does not provide medical advice.

🎯 Learning Tracks
🟢 Foundation Track (Beginners)

Core Topics:

Variables

Data Types

Strings

Features:

Takes basic patient details

Performs simple string operations

Displays formatted clinical data

Inputs:

Patient Name

Age

Heart Rate

City

Operations:

Name → Title Case

City → Uppercase

🟡 Core Track (Intermediate)

Core Topics:

Functions

Recursion

Features:

Validates patient age and heart rate

Uses recursion to collect multiple vitals

Determines audit status

Audit Logic:

Age must be between 0–120

Heart rate must be numeric

Heart rate > 180 bpm → Warning

Invalid input → Flag

Final Status:

PASS → Clean data

REVIEW → Warnings only

FAIL → Any validation failure

🔴 Project Track (Advanced / Mini Project)
🩺 Clinical Data Audit System (Full Version)

Inputs Collected:

Patient Name

Age

Heart Rate (bpm)

Blood Pressure

Systolic

Diastolic

Allergy Information (yes / no)

🔍 Audit Rules
✅ Validation Rules (Hard Failures)

Age must be numeric and between 0–120

Heart rate must be numeric

Blood pressure values must be numeric

Systolic BP > Diastolic BP

Allergy input must be yes or no

⚠️ Safety Rules (Warnings)

Heart rate outside 40–180 bpm

Systolic BP outside 70–200

Diastolic BP outside 40–130

🧾 Audit Classification
Status	Condition
PASS	No flags or warnings
REVIEW	Warnings present, no failures
FAIL	Any validation rule violated
🔑 Traceability

Generates a unique Audit ID for every audit

Audit ID is attached to:

Console output

File logs

💾 File I/O Requirements

Append-only audit log file

Older records are never overwritten

Each log entry includes:

Audit ID

Timestamp

Patient Name

Audit Status

Flags (if any)

Warnings (if any)

🖨 Console Output

The system displays a clean audit report containing:

Audit ID

Timestamp

Patient Name

Audit Status (PASS / REVIEW / FAIL)

Flags

Warnings

Disclaimer

⚠️ Disclaimer

This report is generated for data auditing purposes only.
It is not medically certified, does not diagnose, and does not recommend treatment.

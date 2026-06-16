# How To Use

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Tests

```bash
pytest
```

## Run Validation Pipeline

```bash
python -m automation.validation_pipeline
```

## Generate Reports

```bash
python -m automation.regression_runner
```

## Record Packet Captures

```bash
python record_capture.py
```

## Replay Packet Captures

```bash
python replay_capture.py
```

Generated reports are stored in:

```text
reports/
```

Packet captures are stored in:

```text
captures/
```

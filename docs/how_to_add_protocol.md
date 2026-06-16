# How To Add A Protocol

## Step 1

Create a protocol configuration file.

Example:

```text
configs/new_protocol_config.yaml
```

## Step 2

Create a protocol adapter.

Example:

```text
adapters/fake_new_protocol_adapter.py
```

## Step 3

Create a protocol validator.

Example:

```text
validators/new_protocol_validator.py
```

## Step 4

Create protocol tests.

Example:

```text
tests/new_protocol_tests/
```

## Step 5

Update the validation pipeline.

Example:

```text
automation/validation_pipeline.py
```

## Step 6

Update the regression runner.

Example:

```text
automation/regression_runner.py
```

## Step 7

Update documentation.

* README
* Architecture
* Validation Strategy
* Company Usage

## Step 8

Run the full test suite.

```bash
pytest
```

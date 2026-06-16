# How To Add A Protocol

## 1. Create Configuration

Add a configuration file:

```text
configs/new_protocol_config.yaml
```

## 2. Create Adapter

Add a protocol adapter:

```text
adapters/fake_new_protocol_adapter.py
```

## 3. Create Validator

Add a validator:

```text
validators/new_protocol_validator.py
```

## 4. Create Tests

Add protocol tests:

```text
tests/new_protocol_tests/
```

## 5. Update Pipeline

Add protocol execution to:

```text
automation/validation_pipeline.py
```

## 6. Update Regression Runner

Add protocol reporting to:

```text
automation/regression_runner.py
```

## 7. Run Validation

```bash
pytest
```

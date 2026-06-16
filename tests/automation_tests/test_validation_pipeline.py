# tests protocol validation pipeline behavior

from automation.validation_pipeline import run_all_pipelines


# verifies that all protocol validation pipelines pass
def test_run_all_pipelines():
    results = run_all_pipelines()

    assert results["status"] == "PASS"
    assert len(results["pipelines"]) == 4
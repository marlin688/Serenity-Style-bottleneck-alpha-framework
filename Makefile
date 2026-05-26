.PHONY: test score

test:
	python -m pytest tests

score:
	bottleneck-alpha score examples/sample_score.yaml

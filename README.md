# CODEOWNERS Validator

A simple Python script to validate and check the existence of paths defined in a `.github/CODEOWNERS` file.

## Features

- Reads `.github/CODEOWNERS` file.
- Skips empty lines and comments.
- Extracts paths before the first `@` symbol.
- Checks if the paths exist in the repository.
- Outputs results with ✅ (exists) or ❌ (missing).

## Installation

Clone the repository:

```sh
git clone https://github.com/BaseMax/codeowners-validator.git
cd codeowners-validator
```

## Usage

Run the script from the root of your repository:

```sh
python codeowners_validator.py
```

## Example

Testing on `https://github.com/apache/airflow` repository at https://github.com/apache/airflow/tree/2055aeedb7fa62366907a90c78f7709da612ed25 commit:

```
C:\Users\ALI\Projects\airflow>python codeowners_validator.py
✅ Exists: airflow-core/src/airflow/executors/
✅ Exists: airflow-core/src/airflow/jobs/
✅ Exists: airflow-core/src/airflow/models/
✅ Exists: airflow-core/src/airflow/serialization/
✅ Exists: airflow-core/src/airflow/dag_processing
✅ Exists: providers/cncf/kubernetes/
✅ Exists: chart/
❌ Missing: docs/*.py
❌ Missing: docs/apache-airflow
❌ Missing: docs/docker-stack
❌ Missing: docs/helm-chart
✅ Exists: airflow-core/src/airflow/api/
✅ Exists: airflow-core/src/airflow/api_fastapi/
✅ Exists: airflow-core/src/airflow/api_fastapi/execution_api/
✅ Exists: airflow-ctl/
✅ Exists: airflow-core/src/airflow/api_fastapi/auth/
✅ Exists: airflow-core/src/airflow/ui/
✅ Exists: airflow-core/src/airflow/security/permissions.py
✅ Exists: airflow-core/src/airflow/timetables/
❌ Missing: docs/apache-airflow/concepts/timetable.rst
✅ Exists: airflow-core/src/airflow/models/abstractoperator.py
✅ Exists: airflow-core/src/airflow/models/baseoperator.py
✅ Exists: airflow-core/src/airflow/models/expandinput.py
✅ Exists: airflow-core/src/airflow/models/mappedoperator.py
✅ Exists: airflow-core/src/airflow/models/operator.py
✅ Exists: airflow-core/src/airflow/models/xcom_arg.py
❌ Missing: docs/apache-airflow/concepts/dynamic-task-mapping.rst
✅ Exists: airflow-core/src/airflow/cli/commands/triggerer_command.py
❌ Missing: airflow-core/src/airflow/jobs/triggerer_job.py
✅ Exists: airflow-core/src/airflow/jobs/triggerer_job_runner.py
❌ Missing: docs/apache-airflow/authoring-and-scheduling/deferring.rst
✅ Exists: airflow-core/src/airflow/secrets
✅ Exists: providers/amazon/
✅ Exists: providers/celery/
✅ Exists: providers/cncf/kubernetes
✅ Exists: providers/common/messaging/
✅ Exists: providers/common/sql/
✅ Exists: providers/dbt/cloud/
✅ Exists: providers/edge/
✅ Exists: providers/fab/
✅ Exists: providers/hashicorp/
✅ Exists: providers/openlineage/
✅ Exists: providers/slack/
✅ Exists: providers/smtp/
✅ Exists: providers/snowflake/
✅ Exists: providers/apache/iceberg/
✅ Exists: .github/workflows/
✅ Exists: dev/
✅ Exists: docker-tests/
✅ Exists: kubernetes-tests/
✅ Exists: helm-tests/
✅ Exists: scripts/
✅ Exists: Dockerfile
✅ Exists: Dockerfile.ci
✅ Exists: dev/PROJECT_GUIDELINES.md
❌ Missing: dev/PROVIDER_PACKAGE_DETAILS.md
✅ Exists: dev/README.md
❌ Missing: dev/README_RELEASE_*.md
✅ Exists: dev/README_RELEASE_PROVIDERS.md
✅ Exists: ISSUE_TRIAGE_PROCESS.rst
✅ Exists: airflow-core/src/airflow/decorators/setup_teardown.py
❌ Missing: airflow-core/src/airflow/example_dags/example_setup_teardown*.py
✅ Exists: airflow-core/src/airflow/utils/setup_teardown.py
✅ Exists: airflow-core/src/airflow/io/
❌ Missing: providers/**/fs/
✅ Exists: providers/common/io/
❌ Missing: docs/apache-airflow/core-concepts/objectstorage.rst
✅ Exists: airflow-core/src/airflow/migrations/
❌ Missing: providers/fab/src/airflow-core/src/airflow/providers/fab/migrations/
✅ Exists: task-sdk/
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License.

## Author

Copyright (c) 2025, Max Base.

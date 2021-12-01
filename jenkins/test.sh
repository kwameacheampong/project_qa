#!bin/bash

echo "Test stage"

#venv created, sourced 
python3 -m venv venv
source venv/bin/activate

# pip3 installs, pytest, flask_testing, frontend requirements.txt and backend requirements.txt
pip3 install pytest flask_testing pytest-cov
pip3 install -r frontend/requirements.txt 
pip3 install -r backend/requirements.txt

mkdir test_reports
 
# run pytest frontend 
python3 -m pytest frontend \
   --cov=frontend/application \
   --cov-report term-missing \
   --cov-report xml:test_reports/frontend_coverage.xml \
   --junitxml=test_reports/frontend_junit_report.xml

# run pytest backend
python3 -m pytest backend
   --cov=backend/application \
   --cov-report term-missing \
   --cov-report xml:test_reports/backend_coverage.xml \
   --junitxml=test_reports/backend_junit_report.xml

deactivate
rm -rf venv


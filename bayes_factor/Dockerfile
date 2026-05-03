FROM python:3.12
WORKDIR /workspace/COGS205-complabskills/bayes_factor
COPY . .
RUN pip install scipy
CMD ["python3", "-m", "unittest", "tests.test_bayes_factor"]
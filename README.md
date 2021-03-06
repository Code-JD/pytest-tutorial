# Pytest Tutorial

- [Pytest Tutorial](https://testautomationu.applitools.com/pytest-tutorial/)

---

To run Pytest:

```python
python -m pytest
```

---

More information about specific test:

```python
python -m pytest --verbose
```

---

Less information:

```python
python -m pytest --quiet
```

---

Stop the testing after the first failure:

```python
python -m pytest --exitfirst
```

---

Make a XML report file

```python
python -m pytest --junit-xml report.xml
```

---

Other commands:

```python
python -m pytest test/test_accum.py
python -m pytest stuff
python -m pytest test/test_math.py::test_one_plus_one
python -m pytest -m math

pip install requests
python -m pytest -m rest_api

pip install pytest-html
python -m pytest --html=report.html

pip install pytest-cov
python -m pytest --cov=stuff
python -m pytest --cov=stuff --cov-report html

pip install pytest-xdist
python -m pytest -n 3
```

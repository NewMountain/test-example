# test-example

A simple webserver with testing

## How to use

This is a simple flask webserver that you can extend for your own purposes. It's intended to be a
very quick example of unit and integration tests in the context of a Flask application and show off
a few features of pytest, the preferred Python testing framework.

### To Setup

```bash
# Install all of your dependencies by running this at your terminal
# This will work on OSX, Linux and, possibly, Windows Powershell
pip install -r requirements.txt
```

### To Run

```bash
# Run a server on localhost:3001 by running this at your terminal
# This will work on OSX, Linux and, possibly, Windows Powershell
make run-local-server
```

### To Test

```bash
# Run unit tests
# This will work on OSX, Linux and, possibly, Windows Powershell
make run-unit-tests

# Run integration tests (for quick and dirty demo purposes)
make run-integration-tests

# Run all tests (with code coverage metrics)
make run-all-tests
```

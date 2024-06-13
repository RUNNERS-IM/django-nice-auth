# django-nice-auth Developer Guide

This guide is for developers contributing to the `NHNCloudSMS` library.

## Running Tests

Ensure all tests pass before making any changes. To run tests, use:

```bash
pytest
```


## Environment Variables
Create a .env file in the root directory with the following content:

```plaintext
NICE_AUTH_BASE_URL=https://svc.niceapi.co.kr:22001
NICE_CLIENT_ID=
NICE_CLIENT_SECRET=
NICE_PRODUCT_ID=
NICE_RETURN_URL=
NICE_AUTHTYPE=M
NICE_POPUPYN=N
```

## Building the Package
To build the package, update the version in setup.cfg:
```ini
[metadata]
name = django-nice-auth
version = x.x.x
```

Then, build the package:
```bash
python setup.py sdist bdist_wheel
```

## Deploying the Package
To deploy the package to PyPI, use Twine:
```bash
twine upload --verbose dist/django-nice-auth-X.X.X.tar.gz
```
Ensure you have the necessary permissions to upload to the PyPI repository.

## Contribution Guidelines
1. Fork the repository.
2. Create a new branch (feature/your-feature-name). 
3. Commit your changes with descriptive commit messages. 
4. Push to the branch. 
5. Create a pull request.

## Code Style
Follow PEP 8 for Python code style.

## Contact
For any questions or support, please contact dev@runners.im.


# NTPY
A Python API Wrapper for the [ntfy.sh](https://ntfy.sh/) service
---

## Get Started
- With `pip`
  ```bash
      pip install git+https://github.com/Ifechukwu001/ntpy.git
  ```
- With `Uv`
  ```bash
      uv add git+https://github.com/Ifechukwu001/ntpy.git
  ```
- With `poetry`
  ```bash
      poetry add git+https://github.com/Ifechukwu001/ntpy.git
  ```

## Notes
- You can access the functions for publishing to ntfy.sh (`ntpy.request.publish`  and `ntpy.request.apublish`)
- To add it to your logger dictionary configuration, use the `ntpy.handlers.NtpyHandler`
  - The expected arguments to pass are: `topic (required)`, `title`, `backend`, `validity`, and `level`
    ```python
        LOGGING = {
            "version": 1,
            "disable_existing_loggers": False,
            "handlers": {
                "ntpy": {
                    "level": "INFO",
                    "formatter": "verbose",
                    "class": "ntpy.handlers.NtpyHandler",
                    "topic": "topic",
                    "title": "",
                    "backend": "ntpy.backends.inmemory.InMemoryBackend",
                    "validity": 60,
                },
            },
        }
    ```
  - The formatter used should be something reproducible so that notifications are not sent twice (an example is not putting time in the log)
---

You are free to drop notes and contribute to the project.

Thanks.


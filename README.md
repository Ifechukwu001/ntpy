# NTPY (noti-py)

### Version 0.3.0

## A Python API Wrapper for the [ntfy.sh](https://ntfy.sh/) service

## Get Started

- With `pip`
  ```bash
      pip install git+https://github.com/Ifechukwu001/ntpy.git
  ```
- With `uv`
  ```bash
      uv add git+https://github.com/Ifechukwu001/ntpy.git
  ```
- With `poetry`
  ```bash
      poetry add git+https://github.com/Ifechukwu001/ntpy.git
  ```

## Notes

- You can access the functions for publishing to ntfy.sh (`ntpy.request.publish` and `ntpy.request.apublish`)
- To add it to your logger dictionary configuration, use the logging handlers.

  - **In Memory Backend**
    - The expected arguments to pass are: `topic (required)`, `title`, `validity`, and `level`
      ```python
          LOGGING = {
            "version": 1,
            "disable_existing_loggers": False,
            "handlers": {
                "ntpy": {
                    "level": "INFO",
                    "formatter": "verbose",
                    "class": "ntpy.handlers.InMemoryNtpyHandler",
                    "topic": "topic",
                    "title": "",
                    "validity": 60,
                },
            },
        }
      ```
  - **Redis Backend**

    - The expected arguments to pass are: `topic (required)`, `redis_url (required)`, `title`, `validity`, and `level`

      ```python
        LOGGING = {
          "version": 1,
          "disable_existing_loggers": False,
          "handlers": {
              "ntpy": {
                  "level": "INFO",
                  "formatter": "verbose",
                  "class": "ntpy.handlers.RedisNtpyHandler",
                  "topic": "topic",
                  "redis_url": "redis://localhost:6379",
                  "title": "",
                  "validity": 60,
              },
          },
      }
      ```

  _PS: The logging format used should be something reproducible so that notifications are not sent twice (an example is not putting time in the log)_

---

You are free to drop notes and contribute to the project.

Thanks.

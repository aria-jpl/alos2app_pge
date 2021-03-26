# Tests

To run the test (only 1 at the moment), we assume that the zip files have been downloaded to `alos2app_pge/notebooks`. Due to our local setup, we decided to actually copy the zip files from `alos2app_pge/notebooks` to the directory `alos2app_pge/tests/e2e_test_1`. In the future, we will use symbolic links, though it may be problematic since the files themselves are so large.

Once the `tests/e2e_test_1` directory mirrors that of `notebooks` with its `_context.json` and SLC data, we run from this directory:

```
docker-compose -f e2e_test_1/docker-compose.yaml run test
```

The test does not redirect output, so we recommend running it in a `tmux` session.
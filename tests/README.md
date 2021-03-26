# Tests

To run the test (only 1 at the moment). We assume that the zip files. Due to our local setup, we decided to actually copy the zip files from `alos2app_pge/notebooks` to the `e2e_test_1`. In the future, we will use symbolic links.

Once the `e2e_test_1` directory mirrors that of `alos2app_pge/notebooks` with its `_context.json` and SLC data, we run from this directory:

```
docker-compose -f e2e_test_1/docker-compose.yaml run test
```
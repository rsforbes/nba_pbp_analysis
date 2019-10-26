import pytest
import datetime

class MyPlugin:
    def pytest_sessionfinish(self):
        print("*** test run reporting finishing")

print("Updating....", datetime.datetime.now())


game_date = datetime.datetime.now()
end_date = datetime.datetime.now()

while game_date <= end_date:
    pytest.main(["integration_test.py","-s","--game_date={}".format(game_date.isoformat())])
    game_date += datetime.timedelta(days=1)

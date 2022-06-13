from droid import DroidSettings, start_service
from fraud_checker.logs import initialize_logs
from fraud_checker.routes import APP_ROUTES

if __name__ == '__main__':
    initialize_logs()
    start_service(DroidSettings(routes=APP_ROUTES))

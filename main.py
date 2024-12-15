from application.main import Application
from configs.main import CL_TOKEN
from configs.client import Client

if __name__ == "__main__":
    application = Application(Client())
    application.run(CL_TOKEN)

from application.main import Application
from configs.main import CL_TOKEN

if __name__ == "__main__":
    application = Application()
    application.run(CL_TOKEN)

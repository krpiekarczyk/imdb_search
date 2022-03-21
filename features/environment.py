from utils import create_driver


def before_scenario(context, scenario):
    context.driver = create_driver()


def after_scenario(context, scenario):
    context.driver.quit()

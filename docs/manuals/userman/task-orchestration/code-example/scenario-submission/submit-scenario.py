import taipy as tp
import my_config

if __name__ == "__main__":
    tp.Core().run()

    scenario = tp.create_scenario(my_config.monthly_scenario_cfg)
    submission = tp.submit(scenario)

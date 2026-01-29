import sys
from pathlib import Path


APP_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP_DIR))

from config.industry_config import get_all_industries, get_industry_config


def test_default_industry_is_new_energy_vehicle():
    config = get_industry_config()

    assert config.id == "new_energy_vehicle"
    assert config.app_title == "新能源汽车政策与产业信息分析助手"
    assert "补贴政策" in config.description


def test_new_energy_vehicle_policy_filters_and_questions_are_exposed():
    config = get_industry_config("new_energy_vehicle")

    assert config.policy_filter_fields == ["region", "publish_time", "policy_type"]
    assert any("上海" in question and "补贴" in question for question in config.example_questions)
    assert any("充电设施" in keyword for keyword in config.news_keywords)

    industries = get_all_industries()
    first = industries[0]
    assert first["id"] == "new_energy_vehicle"
    assert first["app_title"] == "新能源汽车政策与产业信息分析助手"
    assert first["policy_filter_fields"] == ["region", "publish_time", "policy_type"]


if __name__ == "__main__":
    test_default_industry_is_new_energy_vehicle()
    test_new_energy_vehicle_policy_filters_and_questions_are_exposed()
    print("industry config tests passed")

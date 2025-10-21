# Copyright © 2026 深圳市深维智见教育科技有限公司 版权所有
# 未经授权，禁止转售或仿制。

"""
行业配置 - 定义各行业的搜索关键词
"""
import logging
from typing import Dict, List, Optional
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)


@dataclass
class IndustryConfig:
    """行业配置"""
    id: str
    name: str
    description: str
    news_keywords: List[str]
    bidding_keywords: List[str]
    research_keywords: List[str]
    app_title: str = ""
    policy_filter_fields: List[str] = field(default_factory=list)
    example_questions: List[str] = field(default_factory=list)


# 预定义的行业配置
INDUSTRY_CONFIGS: Dict[str, IndustryConfig] = {
    "new_energy_vehicle": IndustryConfig(
        id="new_energy_vehicle",
        name="新能源汽车",
        app_title="新能源汽车政策与产业信息分析助手",
        description="面向补贴政策、地方准入、充电设施规划、竞品技术路线和产业链信息整理的行业信息助手",
        news_keywords=[
            "新能源汽车 补贴政策 最新",
            "新能源汽车 地方准入 牌照规则",
            "上海 新能源汽车 补贴政策 充电设施规划",
            "新能源汽车 充电设施 规划 政策",
            "智能网联汽车 准入 试点 政策",
            "新能源汽车 产业链 动力电池 电驱 电控",
            "比亚迪 特斯拉 蔚来 理想 技术路线 对比",
            "新能源汽车 出口 市场 产业政策",
        ],
        bidding_keywords=[
            "新能源汽车采购",
            "新能源公交车采购",
            "充电桩 招标",
            "充电设施 建设 招标",
            "换电站 招标",
            "动力电池 回收 招标",
            "智能网联汽车 示范区",
            "车路协同 新能源汽车",
        ],
        research_keywords=[
            "新能源汽车政策",
            "新能源汽车补贴",
            "充电基础设施",
            "动力电池产业链",
            "智能网联汽车",
            "竞品技术路线",
        ],
        policy_filter_fields=["region", "publish_time", "policy_type"],
        example_questions=[
            "上海新能源汽车补贴政策和充电设施规划有哪些最新变化？",
            "对比比亚迪、特斯拉、蔚来、理想的新能源技术路线和竞争优势。",
            "新能源汽车地方准入、牌照规则和充电基础设施政策应该如何检索和归纳？",
        ],
    ),
    "smart_transportation": IndustryConfig(
        id="smart_transportation",
        name="智慧交通",
        app_title="智慧交通行业信息助手",
        description="智能交通系统、车路协同、自动驾驶等领域",
        news_keywords=[
            "智慧交通 政策",
            "智慧交通 市场",
            "交通运输部 通知",
            "智能网联汽车",
            "自动驾驶 政策",
            "新能源汽车 政策",
            "交通大数据",
            "车路协同",
        ],
        bidding_keywords=[
            "智慧交通",
            "智能交通",
            "交通信息化",
            "车路协同",
            "自动驾驶",
            "智能网联",
        ],
        research_keywords=["智慧交通", "智能交通", "车路协同", "自动驾驶"],
        policy_filter_fields=["region", "publish_time", "policy_type"],
        example_questions=[
            "智慧交通市场规模和车路协同建设趋势是什么？",
            "自动驾驶地方试点政策有哪些差异？",
            "交通信息化招投标机会主要集中在哪些区域？",
        ],
    ),
    "finance": IndustryConfig(
        id="finance",
        name="金融科技",
        app_title="金融科技行业信息助手",
        description="银行、保险、证券、支付等金融领域",
        news_keywords=[
            "金融科技 政策",
            "数字人民币",
            "银行数字化转型",
            "保险科技",
            "证券 金融科技",
            "支付 监管",
            "金融大数据",
            "智能风控",
        ],
        bidding_keywords=[
            "银行",
            "金融",
            "保险",
            "证券",
            "支付平台",
            "风控系统",
            "信贷系统",
            "银行核心系统",
        ],
        research_keywords=["金融科技", "数字金融", "银行数字化", "智能风控"],
        policy_filter_fields=["region", "publish_time", "policy_type"],
        example_questions=[
            "金融科技监管政策最近有哪些变化？",
            "银行数字化转型主要采购哪些系统？",
            "智能风控在信贷场景的落地路径是什么？",
        ],
    ),
    "healthcare": IndustryConfig(
        id="healthcare",
        name="医疗健康",
        app_title="医疗健康行业信息助手",
        description="医疗信息化、智慧医院、医药研发等领域",
        news_keywords=[
            "医疗信息化 政策",
            "智慧医院",
            "医保 政策",
            "药品集采",
            "医疗大数据",
            "互联网医疗",
            "AI医疗",
            "医药研发",
        ],
        bidding_keywords=[
            "医院信息化",
            "智慧医疗",
            "HIS系统",
            "医疗设备",
            "医药采购",
            "医保系统",
        ],
        research_keywords=["医疗信息化", "智慧医疗", "医药研发", "互联网医疗"],
        policy_filter_fields=["region", "publish_time", "policy_type"],
        example_questions=[
            "智慧医院建设政策和招投标机会有哪些？",
            "医保控费政策对医疗信息化有什么影响？",
            "互联网医疗监管和商业化趋势如何？",
        ],
    ),
    "energy": IndustryConfig(
        id="energy",
        name="能源电力",
        app_title="能源电力行业信息助手",
        description="新能源、电力系统、储能等领域",
        news_keywords=[
            "新能源 政策",
            "碳中和",
            "光伏 市场",
            "风电 政策",
            "储能 市场",
            "电力市场化",
            "智能电网",
            "充电桩",
        ],
        bidding_keywords=[
            "新能源项目",
            "光伏电站",
            "风电项目",
            "储能系统",
            "智能电网",
            "充电设施",
        ],
        research_keywords=["新能源", "碳中和", "储能", "智能电网"],
        policy_filter_fields=["region", "publish_time", "policy_type"],
        example_questions=[
            "储能市场政策和商业模式有哪些变化？",
            "光伏、风电和智能电网的投资机会如何比较？",
            "充电设施和电力市场化政策如何影响能源企业？",
        ],
    ),
}

# 默认行业
DEFAULT_INDUSTRY_ID = "new_energy_vehicle"


def get_industry_config(industry_id: Optional[str] = None) -> IndustryConfig:
    """
    获取行业配置

    Args:
        industry_id: 行业ID，如果为空则返回默认行业

    Returns:
        行业配置
    """
    if not industry_id:
        industry_id = DEFAULT_INDUSTRY_ID

    config = INDUSTRY_CONFIGS.get(industry_id)
    if not config:
        logger.warning(f"[industry_config] 未找到行业配置: {industry_id}, 使用默认行业")
        config = INDUSTRY_CONFIGS[DEFAULT_INDUSTRY_ID]

    logger.info(f"[industry_config] 获取行业配置: {config.name} ({config.id})")
    return config


def get_all_industries() -> List[Dict]:
    """
    获取所有行业列表

    Returns:
        行业列表
    """
    return [
        {
            "id": config.id,
            "name": config.name,
            "app_title": config.app_title or f"{config.name}行业信息助手",
            "description": config.description,
            "research_keywords": config.research_keywords,
            "policy_filter_fields": config.policy_filter_fields,
            "example_questions": config.example_questions,
        }
        for config in INDUSTRY_CONFIGS.values()
    ]

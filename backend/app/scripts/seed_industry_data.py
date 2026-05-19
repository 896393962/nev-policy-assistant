"""
行业数据库初始化脚本 - 新能源汽车行业示例数据

用于 Text2SQL、数据库探索和图表演示。数据字段贴合简历中的
"地区 + 时间 + 政策类型" 政策检索，以及竞品技术路线和产业链分析场景。
"""
import os
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.database import Base, SessionLocal, engine
from models.industry_data import CompanyData, IndustryStats, PolicyData


INDUSTRY_NAME = "新能源汽车"


def seed_industry_stats(db):
    """插入新能源汽车行业统计数据"""
    stats_data = [
        {"industry_name": INDUSTRY_NAME, "metric_name": "销量", "metric_value": 688.7, "unit": "万辆", "year": 2022, "region": "全国", "source": "公开资料整理", "notes": "示例数据，用于功能演示"},
        {"industry_name": INDUSTRY_NAME, "metric_name": "销量", "metric_value": 949.5, "unit": "万辆", "year": 2023, "region": "全国", "source": "公开资料整理", "notes": "示例数据，用于功能演示"},
        {"industry_name": INDUSTRY_NAME, "metric_name": "销量", "metric_value": 1286.6, "unit": "万辆", "year": 2024, "region": "全国", "source": "公开资料整理", "notes": "示例数据，用于功能演示"},
        {"industry_name": INDUSTRY_NAME, "metric_name": "渗透率", "metric_value": 25.6, "unit": "%", "year": 2022, "region": "全国", "source": "公开资料整理"},
        {"industry_name": INDUSTRY_NAME, "metric_name": "渗透率", "metric_value": 31.6, "unit": "%", "year": 2023, "region": "全国", "source": "公开资料整理"},
        {"industry_name": INDUSTRY_NAME, "metric_name": "渗透率", "metric_value": 40.9, "unit": "%", "year": 2024, "region": "全国", "source": "公开资料整理"},
        {"industry_name": INDUSTRY_NAME, "metric_name": "充电基础设施保有量", "metric_value": 520.0, "unit": "万台", "year": 2022, "region": "全国", "source": "公开资料整理"},
        {"industry_name": INDUSTRY_NAME, "metric_name": "充电基础设施保有量", "metric_value": 859.6, "unit": "万台", "year": 2023, "region": "全国", "source": "公开资料整理"},
        {"industry_name": INDUSTRY_NAME, "metric_name": "充电基础设施保有量", "metric_value": 1281.8, "unit": "万台", "year": 2024, "region": "全国", "source": "公开资料整理"},
        {"industry_name": INDUSTRY_NAME, "metric_name": "动力电池装机量", "metric_value": 294.6, "unit": "GWh", "year": 2022, "region": "全国", "source": "公开资料整理"},
        {"industry_name": INDUSTRY_NAME, "metric_name": "动力电池装机量", "metric_value": 387.7, "unit": "GWh", "year": 2023, "region": "全国", "source": "公开资料整理"},
        {"industry_name": INDUSTRY_NAME, "metric_name": "动力电池装机量", "metric_value": 548.4, "unit": "GWh", "year": 2024, "region": "全国", "source": "公开资料整理"},
        {"industry_name": INDUSTRY_NAME, "metric_name": "地方充电桩建设目标", "metric_value": 76.0, "unit": "万台", "year": 2025, "region": "上海", "source": "地方公开政策整理"},
        {"industry_name": INDUSTRY_NAME, "metric_name": "地方充电桩建设目标", "metric_value": 70.0, "unit": "万台", "year": 2025, "region": "北京", "source": "地方公开政策整理"},
        {"industry_name": INDUSTRY_NAME, "metric_name": "地方充电桩建设目标", "metric_value": 450.0, "unit": "万台", "year": 2025, "region": "广东", "source": "地方公开政策整理"},
    ]

    for data in stats_data:
        db.add(IndustryStats(**data))

    db.commit()
    print(f"✓ 插入 {len(stats_data)} 条新能源汽车行业统计数据")


def seed_company_data(db):
    """插入企业与产业链样例数据"""
    companies = [
        {"company_name": "比亚迪", "stock_code": "002594.SZ", "industry": INDUSTRY_NAME, "sub_industry": "整车+动力电池", "revenue": 7771.0, "net_profit": 402.5, "gross_margin": 20.2, "market_cap": 8200, "employees": 900000, "market_share": 31.0, "year": 2024, "quarter": 4, "data_source": "公开财报/行业资料整理", "extra_data": {"technology_route": "刀片电池、DM-i、e平台"}},
        {"company_name": "特斯拉中国", "stock_code": "TSLA", "industry": INDUSTRY_NAME, "sub_industry": "整车+智能驾驶", "revenue": None, "net_profit": None, "gross_margin": None, "market_cap": None, "employees": None, "market_share": 7.1, "year": 2024, "quarter": 4, "data_source": "行业资料整理", "extra_data": {"technology_route": "纯电平台、FSD、超级充电"}},
        {"company_name": "蔚来", "stock_code": "NIO", "industry": INDUSTRY_NAME, "sub_industry": "整车+换电服务", "revenue": 657.3, "net_profit": -224.0, "gross_margin": 9.9, "market_cap": None, "employees": 32800, "market_share": 1.8, "year": 2024, "quarter": 4, "data_source": "公开财报/行业资料整理", "extra_data": {"technology_route": "换电体系、高端纯电"}},
        {"company_name": "理想汽车", "stock_code": "LI", "industry": INDUSTRY_NAME, "sub_industry": "整车+增程式", "revenue": 1445.0, "net_profit": 80.0, "gross_margin": 20.5, "market_cap": None, "employees": 31500, "market_share": 3.9, "year": 2024, "quarter": 4, "data_source": "公开财报/行业资料整理", "extra_data": {"technology_route": "增程式、家庭SUV"}},
        {"company_name": "小鹏汽车", "stock_code": "XPEV", "industry": INDUSTRY_NAME, "sub_industry": "整车+智能驾驶", "revenue": 408.7, "net_profit": -58.0, "gross_margin": 14.3, "market_cap": None, "employees": 15000, "market_share": 1.5, "year": 2024, "quarter": 4, "data_source": "公开财报/行业资料整理", "extra_data": {"technology_route": "智能驾驶、800V平台"}},
        {"company_name": "宁德时代", "stock_code": "300750.SZ", "industry": INDUSTRY_NAME, "sub_industry": "动力电池", "revenue": 3620.0, "net_profit": 507.0, "gross_margin": 25.0, "market_cap": 11000, "employees": 110000, "market_share": 37.0, "year": 2024, "quarter": 4, "data_source": "公开财报/行业资料整理", "extra_data": {"technology_route": "磷酸铁锂、三元、麒麟电池"}},
        {"company_name": "亿纬锂能", "stock_code": "300014.SZ", "industry": INDUSTRY_NAME, "sub_industry": "动力电池", "revenue": 487.0, "net_profit": 40.5, "gross_margin": 18.0, "market_cap": 850, "employees": 28000, "market_share": 4.0, "year": 2024, "quarter": 4, "data_source": "公开财报/行业资料整理", "extra_data": {"technology_route": "动力电池、储能电池"}},
        {"company_name": "国轩高科", "stock_code": "002074.SZ", "industry": INDUSTRY_NAME, "sub_industry": "动力电池", "revenue": 320.0, "net_profit": 9.5, "gross_margin": 17.0, "market_cap": 430, "employees": 23000, "market_share": 3.2, "year": 2024, "quarter": 4, "data_source": "公开财报/行业资料整理", "extra_data": {"technology_route": "磷酸铁锂、储能"}},
        {"company_name": "特来电", "stock_code": "未上市", "industry": INDUSTRY_NAME, "sub_industry": "充电运营", "revenue": None, "net_profit": None, "gross_margin": None, "market_cap": None, "employees": None, "market_share": 8.0, "year": 2024, "quarter": 4, "data_source": "行业资料整理", "extra_data": {"technology_route": "公共充电网络、群管群控"}},
        {"company_name": "星星充电", "stock_code": "未上市", "industry": INDUSTRY_NAME, "sub_industry": "充电运营", "revenue": None, "net_profit": None, "gross_margin": None, "market_cap": None, "employees": None, "market_share": 7.5, "year": 2024, "quarter": 4, "data_source": "行业资料整理", "extra_data": {"technology_route": "公共充电、能源管理"}},
    ]

    for data in companies:
        db.add(CompanyData(**data))

    db.commit()
    print(f"✓ 插入 {len(companies)} 条新能源汽车企业数据")


def seed_policy_data(db):
    """插入政策样例数据"""
    policies = [
        {
            "policy_name": "新能源汽车产业发展规划（2021-2035年）",
            "policy_number": "国办发〔2020〕39号",
            "department": "国务院办公厅",
            "level": "国家级",
            "publish_date": date(2020, 10, 20),
            "effective_date": date(2021, 1, 1),
            "category": "发展规划",
            "industry": INDUSTRY_NAME,
            "summary": "提出新能源汽车产业发展方向，推动电动化、网联化、智能化融合发展。",
            "key_points": ["产业规划", "电动化", "智能网联", "基础设施"],
            "impact_level": "重大",
            "affected_entities": ["整车企业", "动力电池企业", "充电运营商"],
        },
        {
            "policy_name": "关于进一步构建高质量充电基础设施体系的指导意见",
            "policy_number": "国办发〔2023〕19号",
            "department": "国务院办公厅",
            "level": "国家级",
            "publish_date": date(2023, 6, 8),
            "effective_date": date(2023, 6, 8),
            "category": "充电设施规划",
            "industry": INDUSTRY_NAME,
            "summary": "要求建设覆盖广泛、规模适度、结构合理、功能完善的高质量充电基础设施体系。",
            "key_points": ["公共充电", "居住区充电", "高速公路充电", "农村地区"],
            "impact_level": "重大",
            "affected_entities": ["充电运营商", "车企", "电网企业"],
        },
        {
            "policy_name": "关于开展智能网联汽车准入和上路通行试点工作的通知",
            "policy_number": "工信部联通装〔2023〕217号",
            "department": "工业和信息化部等四部门",
            "level": "国家级",
            "publish_date": date(2023, 11, 17),
            "effective_date": date(2023, 11, 17),
            "category": "准入规则",
            "industry": INDUSTRY_NAME,
            "summary": "组织开展智能网联汽车准入和上路通行试点，推动自动驾驶产品化和商业化验证。",
            "key_points": ["准入试点", "上路通行", "自动驾驶", "安全责任"],
            "impact_level": "重大",
            "affected_entities": ["整车企业", "自动驾驶方案商", "地方政府"],
        },
        {
            "policy_name": "上海市鼓励购买和使用新能源汽车实施办法",
            "policy_number": "沪府办规〔2023〕7号",
            "department": "上海市人民政府办公厅",
            "level": "市级",
            "publish_date": date(2023, 12, 13),
            "effective_date": date(2024, 1, 1),
            "category": "补贴政策",
            "industry": INDUSTRY_NAME,
            "summary": "围绕新能源汽车购买、使用、牌照和充电设施配套，延续和调整地方支持政策。",
            "key_points": ["地方补贴", "牌照规则", "充电配套", "上海"],
            "impact_level": "重大",
            "affected_entities": ["消费者", "整车企业", "经销商"],
        },
        {
            "policy_name": "北京市新能源汽车推广应用实施方案",
            "policy_number": "京政办发〔2024〕示例",
            "department": "北京市人民政府办公厅",
            "level": "市级",
            "publish_date": date(2024, 3, 15),
            "effective_date": date(2024, 4, 1),
            "category": "地方准入",
            "industry": INDUSTRY_NAME,
            "summary": "围绕小客车指标、公共领域车辆电动化和充电基础设施布局推进新能源汽车应用。",
            "key_points": ["地方准入", "指标政策", "公共领域电动化", "北京"],
            "impact_level": "一般",
            "affected_entities": ["消费者", "公交企业", "出租车企业"],
        },
        {
            "policy_name": "广东省加快新能源汽车产业高质量发展行动计划",
            "policy_number": "粤府办〔2024〕示例",
            "department": "广东省人民政府办公厅",
            "level": "省级",
            "publish_date": date(2024, 5, 20),
            "effective_date": date(2024, 5, 20),
            "category": "产业扶持",
            "industry": INDUSTRY_NAME,
            "summary": "支持整车、动力电池、智能网联和充换电基础设施协同发展，推动产业集群升级。",
            "key_points": ["产业集群", "动力电池", "智能网联", "充换电"],
            "impact_level": "重大",
            "affected_entities": ["整车企业", "零部件企业", "充电运营商"],
        },
        {
            "policy_name": "动力电池回收利用管理办法（征求意见稿）",
            "policy_number": "工信部公告〔2024〕示例",
            "department": "工业和信息化部",
            "level": "国家级",
            "publish_date": date(2024, 8, 10),
            "effective_date": date(2024, 8, 10),
            "category": "技术标准",
            "industry": INDUSTRY_NAME,
            "summary": "规范动力电池溯源、回收、梯次利用和再生利用流程，提升产业链闭环能力。",
            "key_points": ["电池回收", "溯源", "梯次利用", "再生利用"],
            "impact_level": "一般",
            "affected_entities": ["动力电池企业", "回收企业", "整车企业"],
        },
        {
            "policy_name": "公共领域车辆全面电动化先行区试点通知",
            "policy_number": "工信部联通装〔2023〕示例",
            "department": "工业和信息化部等八部门",
            "level": "国家级",
            "publish_date": date(2023, 2, 3),
            "effective_date": date(2023, 2, 3),
            "category": "试点通知",
            "industry": INDUSTRY_NAME,
            "summary": "推动公交、出租、环卫、邮政快递等公共领域车辆电动化，形成可复制推广经验。",
            "key_points": ["公共领域", "车辆电动化", "示范试点"],
            "impact_level": "一般",
            "affected_entities": ["公交企业", "出租车企业", "环卫企业"],
        },
    ]

    for data in policies:
        db.add(PolicyData(**data))

    db.commit()
    print(f"✓ 插入 {len(policies)} 条新能源汽车政策数据")


def main():
    """主函数"""
    print("开始初始化新能源汽车行业数据库...")

    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        db.query(IndustryStats).delete()
        db.query(CompanyData).delete()
        db.query(PolicyData).delete()
        db.commit()
        print("✓ 清空现有行业样例数据")

        seed_industry_stats(db)
        seed_company_data(db)
        seed_policy_data(db)

        print("\n数据库初始化完成!")
        print(f"  - 行业统计: {db.query(IndustryStats).count()} 条")
        print(f"  - 企业数据: {db.query(CompanyData).count()} 条")
        print(f"  - 政策数据: {db.query(PolicyData).count()} 条")
    except Exception as exc:
        db.rollback()
        print(f"✗ 初始化失败: {exc}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()

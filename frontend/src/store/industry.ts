/**
 * Copyright © 2026 深圳市深维智见教育科技有限公司 版权所有
 * 未经授权，禁止转售或仿制。
 */

/**
 * 全局行业状态管理
 */
import { proxy, subscribe } from 'valtio'

// 行业配置类型
export interface IndustryConfig {
  id: string
  name: string
  appTitle: string
  description: string
  // 资讯搜索关键词
  newsKeywords: string[]
  // 招投标搜索关键词
  biddingKeywords: string[]
  // 研究相关关键词
  researchKeywords: string[]
  // 政策检索过滤字段
  policyFilterFields: string[]
  // 推荐问题
  exampleQuestions: string[]
}

// 预定义的行业配置
export const INDUSTRY_CONFIGS: IndustryConfig[] = [
  {
    id: 'new_energy_vehicle',
    name: '新能源汽车',
    appTitle: '新能源汽车政策与产业信息分析助手',
    description: '补贴政策、地方准入、充电设施规划、竞品技术路线和产业链信息整理',
    newsKeywords: [
      '新能源汽车 补贴政策 最新',
      '新能源汽车 地方准入 牌照规则',
      '上海 新能源汽车 补贴政策 充电设施规划',
      '新能源汽车 充电设施 规划 政策',
      '智能网联汽车 准入 试点 政策',
      '新能源汽车 产业链 动力电池 电驱 电控',
      '比亚迪 特斯拉 蔚来 理想 技术路线 对比',
      '新能源汽车 出口 市场 产业政策',
    ],
    biddingKeywords: [
      '新能源汽车采购',
      '新能源公交车采购',
      '充电桩 招标',
      '充电设施 建设 招标',
      '换电站 招标',
      '动力电池 回收 招标',
      '智能网联汽车 示范区',
      '车路协同 新能源汽车',
    ],
    researchKeywords: [
      '新能源汽车政策',
      '新能源汽车补贴',
      '充电基础设施',
      '动力电池产业链',
      '智能网联汽车',
      '竞品技术路线',
    ],
    policyFilterFields: ['region', 'publish_time', 'policy_type'],
    exampleQuestions: [
      '上海新能源汽车补贴政策和充电设施规划有哪些最新变化？',
      '对比比亚迪、特斯拉、蔚来、理想的新能源技术路线和竞争优势。',
      '新能源汽车地方准入、牌照规则和充电基础设施政策应该如何检索和归纳？',
    ],
  },
  {
    id: 'smart_transportation',
    name: '智慧交通',
    appTitle: '智慧交通行业信息助手',
    description: '智能交通系统、车路协同、自动驾驶等领域',
    newsKeywords: [
      '智慧交通 政策',
      '智慧交通 市场',
      '交通运输部 通知',
      '智能网联汽车',
      '自动驾驶 政策',
      '新能源汽车 政策',
      '交通大数据',
      '车路协同',
    ],
    biddingKeywords: [
      '智慧交通',
      '智能交通',
      '交通信息化',
      '车路协同',
      '自动驾驶',
      '智能网联',
    ],
    researchKeywords: ['智慧交通', '智能交通', '车路协同', '自动驾驶'],
    policyFilterFields: ['region', 'publish_time', 'policy_type'],
    exampleQuestions: [
      '智慧交通市场规模和车路协同建设趋势是什么？',
      '自动驾驶地方试点政策有哪些差异？',
      '交通信息化招投标机会主要集中在哪些区域？',
    ],
  },
  {
    id: 'finance',
    name: '金融科技',
    appTitle: '金融科技行业信息助手',
    description: '银行、保险、证券、支付等金融领域',
    newsKeywords: [
      '金融科技 政策',
      '数字人民币',
      '银行数字化转型',
      '保险科技',
      '证券 金融科技',
      '支付 监管',
      '金融大数据',
      '智能风控',
    ],
    biddingKeywords: [
      '银行信息化',
      '金融科技',
      '核心银行系统',
      '保险系统',
      '证券交易系统',
      '支付系统',
    ],
    researchKeywords: ['金融科技', '数字金融', '银行数字化', '智能风控'],
    policyFilterFields: ['region', 'publish_time', 'policy_type'],
    exampleQuestions: [
      '金融科技监管政策最近有哪些变化？',
      '银行数字化转型主要采购哪些系统？',
      '智能风控在信贷场景的落地路径是什么？',
    ],
  },
  {
    id: 'healthcare',
    name: '医疗健康',
    appTitle: '医疗健康行业信息助手',
    description: '医疗信息化、智慧医院、医药研发等领域',
    newsKeywords: [
      '医疗信息化 政策',
      '智慧医院',
      '医保 政策',
      '药品集采',
      '医疗大数据',
      '互联网医疗',
      'AI医疗',
      '医药研发',
    ],
    biddingKeywords: [
      '医院信息化',
      '智慧医疗',
      'HIS系统',
      '医疗设备',
      '医药采购',
      '医保系统',
    ],
    researchKeywords: ['医疗信息化', '智慧医疗', '医药研发', '互联网医疗'],
    policyFilterFields: ['region', 'publish_time', 'policy_type'],
    exampleQuestions: [
      '智慧医院建设政策和招投标机会有哪些？',
      '医保控费政策对医疗信息化有什么影响？',
      '互联网医疗监管和商业化趋势如何？',
    ],
  },
  {
    id: 'energy',
    name: '能源电力',
    appTitle: '能源电力行业信息助手',
    description: '新能源、电力系统、储能等领域',
    newsKeywords: [
      '新能源 政策',
      '碳中和',
      '光伏 市场',
      '风电 政策',
      '储能 市场',
      '电力市场化',
      '智能电网',
      '充电桩',
    ],
    biddingKeywords: [
      '新能源项目',
      '光伏电站',
      '风电项目',
      '储能系统',
      '智能电网',
      '充电设施',
    ],
    researchKeywords: ['新能源', '碳中和', '储能', '智能电网'],
    policyFilterFields: ['region', 'publish_time', 'policy_type'],
    exampleQuestions: [
      '储能市场政策和商业模式有哪些变化？',
      '光伏、风电和智能电网的投资机会如何比较？',
      '充电设施和电力市场化政策如何影响能源企业？',
    ],
  },
]

// 行业状态
export interface IndustryState {
  currentIndustryId: string
  industries: IndustryConfig[]
}

// 从 localStorage 读取
const getStoredIndustryId = (): string => {
  if (typeof window !== 'undefined') {
    const stored = localStorage.getItem('selected_industry_id')
    console.log('[industry store] 从 localStorage 读取行业:', stored)
    return stored || 'new_energy_vehicle'
  }
  return 'new_energy_vehicle'
}

// 创建状态
export const industryState = proxy<IndustryState>({
  currentIndustryId: getStoredIndustryId(),
  industries: INDUSTRY_CONFIGS,
})

// 订阅变化，保存到 localStorage
subscribe(industryState, () => {
  if (typeof window !== 'undefined') {
    console.log('[industry store] 保存行业到 localStorage:', industryState.currentIndustryId)
    localStorage.setItem('selected_industry_id', industryState.currentIndustryId)
  }
})

// 获取当前行业配置
export const getCurrentIndustry = (): IndustryConfig => {
  const industry = industryState.industries.find(
    (i) => i.id === industryState.currentIndustryId
  )
  console.log('[industry store] 获取当前行业:', industry?.name)
  return industry || INDUSTRY_CONFIGS[0]
}

// 切换行业
export const setCurrentIndustry = (industryId: string) => {
  console.log('[industry store] 切换行业:', industryId)
  industryState.currentIndustryId = industryId
}

// 获取行业列表（用于选择器）
export const getIndustryOptions = () => {
  return industryState.industries.map((i) => ({
    value: i.id,
    label: i.name,
    description: i.description,
  }))
}

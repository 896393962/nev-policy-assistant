# Copyright © 2026 深圳市深维智见教育科技有限公司 版权所有
# 未经授权，禁止转售或仿制。

from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class WebSearchRequest(BaseModel):
    """Web搜索请求模型"""
    query: str = Field(..., description="搜索查询文本")
    gl: str = Field("cn", description="兼容字段，Bocha 搜索默认按中文行业场景处理")
    hl: str = Field("zh-cn", description="兼容字段，默认中文")
    autocorrect: bool = Field(True, description="兼容字段")
    page: int = Field(1, description="搜索结果页码")
    search_type: str = Field("search", description="兼容字段，默认网页搜索")


class SearchResultItem(BaseModel):
    """搜索结果项模型"""
    type: str
    title: Optional[str] = None
    link: Optional[str] = None
    snippet: Optional[str] = None
    position: Optional[int] = None
    description: Optional[str] = None
    source: Optional[str] = None
    summary: Optional[str] = None
    published_at: Optional[str] = None
    attributes: Optional[Dict[str, Any]] = None
    question: Optional[str] = None
    queries: Optional[List[str]] = None


class WebSearchResponse(BaseModel):
    """Web搜索响应模型"""
    success: bool
    message: Optional[str] = None
    query: str
    results: List[SearchResultItem] = []
    raw_results: Optional[Dict[str, Any]] = None 

# examples.py
# InfoStats 模块使用示例
# 展示如何调用模块提供的各种方法
import asyncio
from ErisPulse import sdk

async def example_usage():
    """
    InfoStats 模块使用示例
    演示如何调用模块提供的各种方法
    """
    try:
        # 初始化 SDK
        sdk.init()
        
        # 启动适配器
        await sdk.adapter.startup()
        
        # 示例：获取总体统计信息
        sdk.logger.info("=== 获取总体统计信息 ===")
        try:
            total_stats = sdk.InfoStats.get_total_stats()
            sdk.logger.info(f"总体统计: {total_stats}")
        except Exception as e:
            sdk.logger.error(f"获取总体统计信息失败: {e}")
        
        # 示例：获取平台分类统计
        sdk.logger.info("=== 获取平台分类统计 ===")
        try:
            platform_stats = sdk.InfoStats.get_platform_stats()
            sdk.logger.info(f"平台统计: {platform_stats}")
        except Exception as e:
            sdk.logger.error(f"获取平台统计失败: {e}")
        
        # 示例：获取最近的事件记录
        sdk.logger.info("=== 获取最近事件记录 ===")
        try:
            recent_events = sdk.InfoStats.get_recent_events(10)  # 获取最近10条
            sdk.logger.info(f"最近事件数量: {len(recent_events)}")
            for i, event in enumerate(recent_events[:3]):  # 只打印前3条
                sdk.logger.info(f"事件 {i+1}: {event}")
        except Exception as e:
            sdk.logger.error(f"获取最近事件失败: {e}")
        
        # 示例：获取时间范围内的事件统计
        sdk.logger.info("=== 获取时间范围统计 ===")
        try:
            time_range_stats = sdk.InfoStats.get_events_in_time_range(5)  # 最近5分钟
            sdk.logger.info(f"最近5分钟统计: {time_range_stats}")
        except Exception as e:
            sdk.logger.error(f"获取时间范围统计失败: {e}")
        
        # 示例：获取每分钟事件统计
        sdk.logger.info("=== 获取每分钟事件统计 ===")
        try:
            per_minute_stats = sdk.InfoStats.get_events_per_minute(5)  # 最近5分钟
            sdk.logger.info(f"每分钟统计: {per_minute_stats}")
        except Exception as e:
            sdk.logger.error(f"获取每分钟统计失败: {e}")
        
        # 示例：搜索事件
        sdk.logger.info("=== 搜索事件 ===")
        try:
            search_results = sdk.InfoStats.search_events(keyword="test", limit=5)
            sdk.logger.info(f"搜索结果数量: {len(search_results)}")
            for i, event in enumerate(search_results):
                sdk.logger.info(f"搜索结果 {i+1}: {event}")
        except Exception as e:
            sdk.logger.error(f"搜索事件失败: {e}")
        
        # 示例：获取用户统计（使用当前用户ID作为示例）
        sdk.logger.info("=== 获取用户统计 ===")
        try:
            # 这里使用一个示例用户ID，实际使用时应替换为真实用户ID
            user_stats = sdk.InfoStats.get_user_stats("example_user_id")
            sdk.logger.info(f"用户统计: {user_stats}")
        except Exception as e:
            sdk.logger.error(f"获取用户统计失败: {e}")
        
        # 示例：获取群组统计（使用示例群组ID）
        sdk.logger.info("=== 获取群组统计 ===")
        try:
            # 这里使用一个示例群组ID，实际使用时应替换为真实群组ID
            group_stats = sdk.InfoStats.get_group_stats("example_group_id")
            sdk.logger.info(f"群组统计: {group_stats}")
        except Exception as e:
            sdk.logger.error(f"获取群组统计失败: {e}")
        
        # 示例：重置统计数据
        sdk.logger.info("=== 重置统计数据 ===")
        try:
            # 注意：这将清除所有统计数据，仅作演示用
            # sdk.InfoStats.reset_stats()
            sdk.logger.info("重置功能已展示（实际未执行）")
        except Exception as e:
            sdk.logger.error(f"重置统计失败: {e}")
            
        sdk.logger.info("InfoStats 模块示例执行完成")
        
    except Exception as e:
        sdk.logger.error(f"执行示例时发生错误: {e}")
    finally:
        # 关闭适配器
        await sdk.adapter.shutdown()

if __name__ == "__main__":
    asyncio.run(example_usage()) 
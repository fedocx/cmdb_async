from celery import Celery

cele = Celery('AsyncCelery')                                # 创建 Celery 实例
cele.config_from_object('AsyncCelery.celery_config')         # 通过 Celery 实例加载配置模块
# 定义数据处理操作的接口
class DataProcessor:
    def process(self, data):
        pass

# 具体的筛选操作类
class FilterProcessor(DataProcessor):
    def process(self, data):
        # 进行筛选操作
        filtered_data = [item for item in data if item > 0]
        return filtered_data

# 具体的删除操作类
class DeleteProcessor(DataProcessor):
    def process(self, data):
        # 进行删除操作
        cleaned_data = [item for item in data if item % 2 == 0]
        return cleaned_data

# 管道类
class Pipeline:
    def __init__(self, processors):
        self.processors = processors

    def process_data(self, data):
        for processor in self.processors:
            data = processor.process(data)
        return data

# 使用管道模式处理数据
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filter_processor = FilterProcessor()
delete_processor = DeleteProcessor()

pipeline = Pipeline([filter_processor, delete_processor])

result = pipeline.process_data(data)
print(result)  # 输出: [2, 4, 6, 8, 10]